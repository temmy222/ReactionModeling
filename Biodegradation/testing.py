from Biodegradation.Substrate.inhibition import Inhibition
from Biodegradation.Substrate.solution import Solution
from Biodegradation.Substrate.substrate import Component

c_pce = Component(0.2, 'PCE', 0.86, 13.6, 4.5, 5.7)
c_tce = Component(0.29, 'TCE', 0.86, 33.6, 4.5, 5.7)
c_dce = Component(0.2, 'DCE', 0.86, 23.6, 6.5, 5.7)
c_vc = Component(0.2, 'VC', 1.86, 13.6, 6.5, 5.7)
all_comp = [c_pce, c_tce, c_tce, c_vc]
iscompetiting = [{c_pce: []}, {c_tce: [c_pce]}, {c_dce: [c_tce]}, {c_vc: [c_tce, c_dce]}]
ishaldane = [{c_pce: []}, {c_tce: [c_tce]}, {c_dce: [c_dce]}, {c_vc: [c_vc]}]


soln = Solution(all_comp, iscompetiting, ishaldane)
# temp = list(iscompetiting[0].keys())
# print(temp[0])
inhibit = Inhibition(soln)
print(inhibit.computeCompetitiveInhibition(c_vc))
print(inhibit.computeHaldaneInhibition(c_tce))
