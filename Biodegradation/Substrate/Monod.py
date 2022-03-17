import numpy as np

max_rate = 0.0000067
sub_conc = np.linspace(0, 0.00001, 10)
michaelis_constant = 0.00005

rate = np.zeros(len(sub_conc))
rate = (max_rate * sub_conc) / michaelis_constant + sub_conc


class Monod(object):
    def __init__(self):
        pass

    def growth_rate(self, umax, Ks, S, Knc=None, Kc=None, Kh=None):
        if Knc is not None and Kc is None and Kh is None:
            Inc = 1 + self.S / Knc
            growth = (self.umax * self.S / (self.Ks + self.S)) / Inc
        elif Kc is not None and Knc is None and Kh is None:
            if isinstance(Kc, list):
                Ic = []
                for i in range(len(list)):
                    Ic.append(self.S / Kc[i])
                pass
            else:
                Ic = 1 + self.S / Kc
                growth = self.umax * self.S / ((self.Ks * Ic) + self.S)
        elif Kh is not None and Knc is None and Kc is None:
            Ih = (self.S ** 2) / Kh
            growth = self.umax * self.S / (self.Ks + self.S + Ih)
        elif Kh is not None and Kc is not None and Knc is None:
            Ih = (self.S ** 2) / Kh
            Ic = 1 + self.S / Kc
            growth = self.umax * self.S / ((self.Ks * Ic) + self.S + Ih)
        elif Kh is not None and Kc is not None and Knc is not None:
            Inc = 1 + self.S / Knc
            Ic = 1 + self.S / Kc
            Ih = (self.S ** 2) / Kh
            growth = (self.umax * self.S) / ((self.Ks * Ic) + self.S + Ih) / Inc
        else:
            growth = self.umax * self.S / (self.Ks + self.S)
        return growth

    def growth_rate_new(self, component, inhibition):
        competitive = inhibition.computeCompetitiveInhibition(component)
        non_competitive = inhibition.computeNonCompetitiveInhibition(component)
        haldane = inhibition.computeHaldaneInhibition(component)
        numerator = (component.umax * component.conc)
        denominator = (component.ks + competitive + component.conc + haldane) * non_competitive
        # denominator = (component.ks + component.ks*competitive + component.conc + component.conc*haldane) * non_competitive
        growth = numerator/denominator
        return growth
