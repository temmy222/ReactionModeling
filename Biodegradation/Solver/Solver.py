import csv

import numpy as np
from scipy.integrate import odeint

from Biodegradation.Substrate.Monod import Monod
from Biodegradation.Substrate.inhibition import Inhibition
from Biodegradation.Substrate.solution import Solution
from Biodegradation.Substrate.substrate import Component


class Solver(object):
    def __init__(self, components, biomass, iscompeting, ishaldane, isnoncompetiting, react_to_react, react_to_product):

        self.biomass = biomass
        self.components = components
        self.iscompeting = iscompeting
        self.ishaldane = ishaldane
        self.isnoncompetiting = isnoncompetiting
        self.react_to_react = react_to_react
        self.react_to_product = react_to_product

    def getParams(self):
        param = []
        for i in range(len(self.components)):
            param.append(self.components[i].umax)
            param.append(self.components[i].ks)
            param.append(self.components[i].kci)
            param.append(self.components[i].khi)
            param.append(self.components[i].knc)
        for i in range(len(self.biomass)):
            param.append(self.biomass[i].yield_mass)
            param.append(self.biomass[i].death_rate)
        return param

    def getInitConc(self):
        param = []
        for i in range(len(self.components)):
            param.append(self.components[i].conc)
        for i in range(len(self.biomass)):
            param.append(self.biomass[i].init_conc)
        return param

    def computeDerivative(self, reactants, product, all_components, biomass_conc):
        soln = Solution(all_components, self.iscompeting, self.ishaldane, self.isnoncompetiting)
        inhibit = Inhibition(soln)
        monods = self.computeAllMonods(all_components, inhibit)
        reac = 0
        prod = 0
        if len(reactants) != 0:
            for i in range(len(reactants)):
                index = reactants[i].index - 1
                reac = reac + (-monods[index] * biomass_conc)
        if len(product) != 0:
            for i in range(len(product)):
                index = product[i].index - 1
                prod = prod + (monods[index] * biomass_conc)
        deriv = reac + prod
        return deriv

    def getRelevantDict(self, all_values, component):
        if type(all_values) == list:
            for i in range(len(all_values)):
                temp = list(all_values[i].keys())[0]
                if temp.name == component.name:
                    outputter = all_values[i]
                    break
        else:
            outputter = {}
        return outputter

    def computeAllMonods(self, all_comp, inhibit):
        monods = []
        for i in range(len(all_comp)):
            monods.append(Monod().growth_rate_new(all_comp[i], inhibit))
        return monods

    def getReactants(self, component):
        temp = self.getRelevantDict(self.react_to_react, component)
        reactant = temp[list(temp.keys())[0]]
        return reactant


    def getProducts(self, component):
        temp = self.getRelevantDict(self.react_to_product, component)
        product = temp[list(temp.keys())[0]]
        return product

    def mult_five(self, y, t, params):
        S1, S2, S3, S4, S5, X = y
        umax1, Ks1, Kci1, Khi1, Knci1, umax2, Ks2, Kci2, Khi2, Knci2, umax3, Ks3, Kci3, Khi3, Knci3, umax4, Ks4, Kci4, Khi4, Knci4, umax5, Ks5, Kci5, Khi5, Knci5, yieldmass, death_rate = params
        S_all = S1 + S2 + S3 + S4 + S5
        c1 = Component(1, S1, 'PCE', umax1, Ks1, Kci1, Khi1, Knci1)
        c2 = Component(2, S2, 'TCE', umax2, Ks2, Kci2, Khi2, Knci2)
        c3 = Component(3, S3, 'DCE', umax3, Ks3, Kci3, Khi3, Knci3)
        c4 = Component(4, S4, 'VC', umax4, Ks4, Kci4, Khi4, Knci4)
        c5 = Component(5, S5, 'ETH', umax5, Ks5, Kci5, Khi5, Knci5)
        all_comp = [c1, c2, c3, c4, c5]
        deriv = []
        for component in all_comp:
            derivative = self.computeDerivative(self.getReactants(component), self.getProducts(component), all_comp, X)
            deriv.append(derivative)
            if component.name =='ETH':
                print(derivative)
        deriv.append(yieldmass * S_all - death_rate * X)
        return deriv

    def solve(self, end_time, time_inc):
        t = np.arange(0., end_time, time_inc)
        y0 = self.getInitConc()
        params = self.getParams()
        psoln = odeint(self.mult_five, y0, t, args=(params,))
        return psoln
