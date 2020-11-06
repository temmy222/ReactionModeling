class BiomassMonod(object):
    def __init__(self, umax, Ks, S, **kwargs):
        self.umax = umax
        self.Ks = Ks
        self.S = S
        self.Knc = kwargs.get('KNC')
        self.Kc = kwargs.get('KC')
        self.Kh = kwargs.get('KH')

    def growth_rate(self):
        if self.Knc is not None and self.Kc is None and self.Kh is None:
            Inc = 1 + self.S / self.Knc
            growth = (self.umax * self.S / (self.Ks + self.S)) / Inc
        elif self.Kc is not None and self.Knc is None and self.Kh is None:
            Ic = 1 + self.S / self.Kc
            growth = self.umax * self.S / ((self.Ks * Ic) + self.S)
        elif self.Kh is not None and self.Knc is None and self.Kc is None :
            Ih = (self.S ** 2) / self.Kh
            growth = self.umax * self.S / (self.Ks + self.S + Ih)
        elif self.Kh is not None and self.Kc is not None and self.Knc is not None:
            Inc = 1 + self.S / self.Knc
            Ic = 1 + self.S / self.Kc
            Ih = (self.S ** 2) / self.Kh
            growth = (self.umax * self.S) / ((self.Ks * Ic) + self.S + Ih) / Inc
        else:
            growth = self.umax * self.S / (self.Ks + self.S)
        return growth