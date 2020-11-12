class Component(object):
    def __init__(self, index, conc, name, umax, ks, kci=None, khi=None, knc=None, yield_mass=None):
        self.index = index
        self.ks = ks
        self.conc = conc
        self.name = name
        self.umax = umax
        self.kci = kci
        self.khi = khi
        self.knc = knc
        self.yield_mass = yield_mass
