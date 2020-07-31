from Converter.Restrictions import *
from Converter.Losses import *
from scipy.optimize import minimize
import numpy as np

Losses = []
Losses.extend(TransformerLosses)
Losses.extend(EntranceInductorLosses)
Losses.extend(AuxiliaryInductorLosses)
Losses.extend(CapacitorLosses)
Losses.extend(DiodeLosses)
Losses.extend(SwitchLosses)

Restrictions = [dIin_max, bmax_Li, bmax_Lk]


class BoostHalfBridgeInverter:

    def __init__(self, transformer, entrance_inductor, auxiliary_inductor, circuit_features, switches, diodes, capacitors, dissipators=None):
        self.ConverterLosses = []
        self.CalculatedValues = {}
        for loss in Losses:
            self.ConverterLosses.append({'active': True, 'function': loss})
        self.ConverterRestrictions = []
        for restriction in Restrictions:
            self.ConverterRestrictions.append({'active': True, 'function': restriction, 'type': 'inequation'})
        self.Features = circuit_features
        self.Transformer = transformer
        self.EntranceInductor = entrance_inductor
        self.AuxiliaryInductor = auxiliary_inductor
        self.Capacitors = capacitors
        self.Diodes = diodes
        self.Switches = switches
        self.first_run = True
        self.Dissipators = dissipators
        self.feasibility = False

    def optimize(self, epochs=100, algorithm='SLSQP'):
        self.first_run = True
        x0 = [40e3, 1e8*0.0002562, 1e10*1e-6]
        bounds = ((10e3, 100e3), (1e4, 1e6), (1e10*1e-7, 1e10*1e-5))
        eps = [1e1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
        solution = minimize(
                            self.compensated_total_loss,
                            x0,
                            method=algorithm,
                            options={'maxiter': epochs, 'disp': True, 'ftol': 1e-6, 'eps': 1e-4},
                            bounds=bounds,
                            constraints={'fun': self.total_constraint, 'type': 'ineq'}
        )
        print(solution)
        print([solution.x[0], solution.x[1]/1e8, solution.x[2]/1e10])
        self.feasibility = solution.success
        return [solution.x[0], solution.x[1]/1e8, solution.x[2]/1e10]

    """ 
    Calculates the objective function, defined by the ALAG Method
    :input:
        X: list containing in order: frequency, Li, Lk.
        rk: scaling factor of the k-iteration of the ALAG method.
    :return: a single float value.
    """
    def slackness(self, X, rk):
        slack = self.compensated_total_loss(X)
        for restriction in self.ConverterRestrictions:
            if restriction['type'] is 'eq':
                slack = slack + (restriction['function'](self, X)) ** 2 / rk
            if restriction['type'] is 'inequation':
                slack = slack - np.log(restriction['function'](self, X)) * rk
        return slack

    """
    Calculates the total converter loss, iterating to obtain the real efficiency.
    This iteration is due to the fact that the efficiency actually changes the input current of the converter.
    :input:
        X: list containing in order: frequency, Li, Lk.
    :return: a single float value.
    """
    def compensated_total_loss(self, X):
        efficiency = 0.8
        po = self.Features['Po']
        loss = po * (1 - efficiency) / efficiency
        error = 2
        while error > 0.01:
            loss_last = loss
            loss = self.total_loss([X[0], X[1], X[2], efficiency])
            efficiency = po / (po + loss)
            error = abs(loss_last - loss)
        if self.first_run:
            self.first_run = False
        self.CalculatedValues['efficiency'] = efficiency
        return loss

    def compensated_total_loss_vector_input(self, frequency, Li, Lk=None):
        size = np.size(frequency)
        loss = np.zeros(size)
        po = self.Features['Po']
        for i in range(0, size):
            efficiency = 0.8
            error = 2
            loss_last = po * (1 - efficiency) / efficiency
            while error > 0.01:
                loss[i] = self.total_loss([frequency[i], Li, Lk, efficiency])
                efficiency = po / (po + loss[i])
                error = abs(loss_last - loss[i])
                loss_last = loss[i]
        return loss

    """
    Calculates the total_loss of the converter, given a frequency, gap widths and efficiency
    :input:
        X: list containing in order: frequency, Li, Lk and the efficiency.
    :return: a single float value.
    """
    def total_loss(self, X):
        output = 0
        self.CalculatedValues = SimulateCircuit(self, X)
        for loss in self.ConverterLosses:
            if loss['active']:
                partial = loss['function'](self, X)
                output = output + partial
        return output

    """
    Calculates all the M constraints and returns them in a M sized vector.
    The variable first_run guarantees that you only simulate the circuit in this function if the
    circuit wasn't already simulated in the compensated_total_loss function.
    This is done to save, so the circuit is only simulated once.
    :input:
        X: list containing in order: frequency, Li, Lk and the efficiency.
    :return: a list containing M floats.
    """
    def total_constraint(self, X):
        constraints = []
        eff = 0.8
        if self.first_run:
            self.CalculatedValues = SimulateCircuit(self, [X[0], X[1], X[2], eff])
            self.first_run = False
        else:
            eff = self.CalculatedValues['efficiency']
        for restriction in self.ConverterRestrictions:
            func = restriction['function']
            constraints.append(func(self, [X[0], X[1], X[2], eff], self.CalculatedValues))
        return constraints

    """return: the feasibility of the circuit as a boolean"""
    def solution_is_feasible(self):
        return self.feasibility

    def get_parameter(self, name):
        if name == 'primary_cable':
            return self.Transformer.Primary.Cable                       # ok
        elif name == 'secondary_cable':
            return self.Transformer.Secondary.Cable                     # ok
        elif name == 'transformer_core':
            return self.Transformer.Core                                # ok
        elif name == 'primary_winding':
            return self.Transformer.Primary.N                           # ok
        elif name == 'secondary_winding':
            return self.Transformer.Secondary.N                         # ok
        elif name == 'primary_parallel_wires':
            return self.Transformer.Primary.Ncond                       # ok
        elif name == 'secondary_parallel_wires':
            return self.Transformer.Secondary.Ncond                     # ok
        elif name == 'entrance_inductor_cable':
            return self.EntranceInductor.Cable                          # ok
        elif name == 'entrance_inductor_winding':
            return self.EntranceInductor.N                              # ok
        elif name == 'entrance_inductor_parallel_wires':
            return self.EntranceInductor.Ncond                          # ok
        elif name == 'entrance_inductor_core':
            return self.EntranceInductor.Core                           # ok
        elif name == 'auxiliary_inductor_cable':
            return self.AuxiliaryInductor.Cable                         # ok
        elif name == 'auxiliary_inductor_winding':
            return self.AuxiliaryInductor.N                             # ok
        elif name == 'auxiliary_inductor_parallel_wires':
            return self.AuxiliaryInductor.Ncond                         # ok
        elif name == 'auxiliary_inductor_core':
            return self.AuxiliaryInductor.Core                          # ok
        elif name == 'c1' or name == 'C1':
            return self.Capacitors[0]                                   # ok
        elif name == 'c2' or name == 'C2':
            return self.Capacitors[1]                                   # ok
        elif name == 'c3' or name == 'C3':
            return self.Capacitors[2]                                   # ok
        elif name == 'c4' or name == 'C4':
            return self.Capacitors[3]                                   # ok
        elif name == 'd3' or name == 'D3':
            return self.Diodes[0]                                       # ok
        elif name == 'd4' or name == 'D4':
            return self.Diodes[1]                                       # ok
        elif name == 's1' or name == 'S1':
            return self.Switches[0]                                     # ok
        elif name == 'S2' or name == 'S2':
            return self.Switches[1]                                     # ok
        else:
            raise Exception(name + " is not a defined parameter")

    def set_parameter(self, name, value):
        if name == 'primary_cable':
            self.Transformer.Primary.Cable = value
        elif name == 'secondary_cable':
            self.Transformer.Secondary.Cable = value
        elif name == 'transformer_core':
            self.Transformer.Core = value
        elif name == 'primary_winding':
            self.Transformer.Primary.N = value
        elif name == 'secondary_winding':
            self.Transformer.Secondary.N = value
        elif name == 'primary_parallel_wires':
            self.Transformer.Primary.Ncond = value
        elif name == 'secondary_parallel_wires':
            self.Transformer.Secondary.Ncond = value
        elif name == 'entrance_inductor_cable':
            self.EntranceInductor.Cable = value
        elif name == 'entrance_inductor_winding':
            self.EntranceInductor.N = value
        elif name == 'entrance_inductor_parallel_wires':
            self.EntranceInductor.Ncond = value
        elif name == 'entrance_inductor_core':
            self.EntranceInductor.Core = value
        elif name == 'auxiliary_inductor_cable':
            self.AuxiliaryInductor.Cable = value
        elif name == 'auxiliary_inductor_winding':
            self.AuxiliaryInductor.N = value
        elif name == 'auxiliary_inductor_parallel_wires':
            self.AuxiliaryInductor.Ncond = value
        elif name == 'auxiliary_inductor_core':
            self.AuxiliaryInductor.Core = value
        elif name == 'c1' or name == 'C1':
            self.Capacitors[0] = value
        elif name == 'c2' or name == 'C2':
            self.Capacitors[1] = value
        elif name == 'c3' or name == 'C3':
            self.Capacitors[2] = value
        elif name == 'c4' or name == 'C4':
            self.Capacitors[3] = value
        elif name == 'd3' or name == 'D3':
            self.Diodes[0] = value
        elif name == 'd4' or name == 'D4':
            self.Diodes[1] = value
        elif name == 's1' or name == 'S1':
            self.Switches[0] = value
        elif name == 'S2' or name == 'S2':
            self.Switches[1] = value
        else:
            raise Exception(name + " is not a defined parameter")
