class Solver(object):
    def __init__(self, react_to_react, react_to_product):
        self.react_to_react = react_to_react
        self.react_to_product = react_to_product

    def mult_five(y, t, params):
        S_PCE, S_TCE, S_DCE, S_VC,S_ETH, X = y
        umax_PCE, umax_TCE, umax_DCE, umax_VC, Ks_PCE, Ks_TCE, Ks_DCE, Ks_VC, Kci_PCE, Kci_TCE, Kci_DCE, Khi_TCE, Khi_DCE, Khi_VC = params
        monod_PCE = Monod(umax_PCE, Ks_PCE, S_PCE)
        miu_PCE = monod_PCE.growth_rate()
        monod_TCE = Monod(umax_TCE, Ks_TCE, S_TCE)
        miu_TCE = monod_TCE.growth_rate(Kc=Kci_PCE)
        monod_DCE = Monod(umax_DCE, Ks_DCE, S_DCE)
        miu_DCE = monod_DCE.growth_rate(Kc=Kci_TCE)
        monod_VC_DCE = Monod(umax_VC, Ks_VC, S_VC)
        miu_VC_DCE = monod_DCE.growth_rate(Kc=Kci_DCE)
