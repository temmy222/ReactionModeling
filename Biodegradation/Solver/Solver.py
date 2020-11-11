from Biodegradation.Substrate.Monod import Monod
from Biodegradation.Substrate.inhibition import Inhibition
from Biodegradation.Substrate.solution import Solution
from Biodegradation.Substrate.substrate import Component


class Solver(object):
    def __init__(self, react_to_react, react_to_product):
        self.react_to_react = react_to_react
        self.react_to_product = react_to_product

    def mult_five(y, t, params):
        S1, S2, S3, S4, S5, X = y
        umax1, umax2, umax3, umax4, umax5, Ks1, Ks2, Ks3, Ks4, Ks5, Kci1, Kci2, Kci3,Kci4, Kci5, Khi1, Khi2, Khi3, Khi4,Khi5, Knci1, Knci2, Knci3,Knci4, Knci5, yieldmass, death_rate = params
        S_all = S1 + S2 + S3 + S4 + S5
        c_pce = Component(S1, 'PCE', umax1, Ks1, Kci1)
        c_tce = Component(S2, 'TCE', umax2, Ks2, Kci2, Khi2)
        c_dce = Component(S3, 'DCE', umax3, Ks3, Kci3, Khi3)
        c_vc = Component(S4, 'VC', umax4, Ks4, None, Khi4)
        c_eth = Component(S5, 'VC', umax5, Ks5)
        all_comp = [c_pce, c_tce, c_tce, c_vc, c_eth]
        iscompetiting = [{c_pce: []}, {c_tce: [c_pce]}, {c_dce: [c_tce]}, {c_vc: [c_tce, c_dce]}]
        ishaldane = [{c_pce: []}, {c_tce: [c_tce]}, {c_dce: [c_dce]}, {c_vc: [c_vc]}]
        soln = Solution(all_comp, iscompetiting, ishaldane)
        inhibit = Inhibition(soln)
        monod_PCE = Monod().growth_rate_new(c_pce, inhibit)
        monod_DCE = Monod().growth_rate_new(c_dce, inhibit)
        monod_TCE = Monod().growth_rate_new(c_tce, inhibit)
        monod_VC = Monod().growth_rate_new(c_vc, inhibit)
        derivs = [-monod_PCE * X,
                  -monod_TCE * X + monod_PCE * X,
                  -monod_DCE * X + monod_TCE * X,
                  -monod_VC * X + monod_DCE * X,
                  monod_VC * X,
                  yieldmass * S_all - death_rate * X
                  ]
        return derivs
