class Inhibition(object):
    def __init__(self, solution):
        self.solution = solution

    def computeCompetitiveInhibition(self, component):
        temp = self.getRelevantDict(self.solution.isCompeting, component)
        starter = 0
        if temp is not None:
            inhibitives = temp[component]
            if len(temp[component]) != 0:
                for i in range(len(inhibitives)):
                    interm = inhibitives[i]
                    starter = starter + ((component.ks * interm.conc) / interm.kci)
        return starter

    def computeHaldaneInhibition(self, component):
        temp = self.getRelevantDict(self.solution.isHaldane, component)
        starter = 0
        if temp is not None:
            haldanes = temp[component]
            if len(temp[component]) != 0:
                for i in range(len(haldanes)):
                    interm = haldanes[i]
                    starter = starter + ((component.conc ** 2) / interm.khi)
        return starter

    def computeNonCompetitiveInhibition(self, component):
        temp = self.getRelevantDict(self.solution.isNonCompetiting, component)
        if temp:
            non_competiting = temp[component]
            starter = 0
            if len(temp[component]) != 0:
                for i in range(len(non_competiting)):
                    interm = non_competiting[i]
                    starter = starter + ((component.ks * interm.conc) / interm.knc)
                    outputt = starter
            else:
                outputt = 1
        else:
            outputt = 1
        return outputt

    def getRelevantDict(self, all_values, component):
        outputt = None
        if type(all_values) == list:
            for i in range(len(all_values)):
                temp = list(all_values[i].keys())[0]
                if temp == component:
                    outputt = all_values[i]
                    break
        else:
            outputt = {}
        return outputt
