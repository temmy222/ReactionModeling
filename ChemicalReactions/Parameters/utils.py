import os
import re


def slicing(pattern, array, start_point=None):
    many = []
    index = []
    if start_point is None:
        start_point = 0
    for i in range(start_point, len(array)):
        if re.match(pattern, array[i]):
            many.append(array[i])
            index.append(i)
    return many, index


def split(array):
    m = {}
    for i in range(0, len(array)):
        n = array[i].split()
        m[i] = n
    return m


def getCompNames(dict_of_species_props):
    list_of_species = []
    for i in range(0, len(dict_of_species_props)):
        dict_of_species_props[i][0].strip("'")
        list_of_species.append(dict_of_species_props[i][0])
    return list_of_species


def convertToFloat(values):
    for i in range(0, len(values)):
        values[i] = float(values[i])
    return values


def searchComp(comp_name, list_of_components):
    list_of_components = getCompNames(list_of_components)
    var2 = "'"
    comp_name = var2 + comp_name + var2
    strep = []
    for i in range(0, len(list_of_components)):
        if list_of_components[i] == comp_name:
            strep.append(i)
    return strep


def getComponents(dest, file):
    os.chdir(dest)
    f = open(file, 'r')
    m = f.readlines()
    for i in range(len(m) - 1, -1, -1):
        if re.match(r'\s', m[i]):
            del m[i]
    pattern = r"[^'#]"
    pattern = r"['#]"  # means string that contains any of ' or # (the [] means that)
    pattern2 = r'^#######'  # ^ is used to check if a string starts with a certain character. https://www.programiz.com/python-programming/regex
    nextpattern = r'[^#]'  # means string that does not contain the #
    nextpattern2 = r'[^null]'

    listt, mache = slicing(pattern, m)
    many, index = slicing(pattern2, listt)

    aqueous = listt[index[1] + 1:index[2]]
    mineral = listt[index[3] + 1:index[4]]
    gas = listt[index[5] + 1:len(listt)]

    aqueous2, num = slicing(nextpattern, aqueous)
    mineral2, num = slicing(nextpattern, mineral)
    gas2, num = slicing(nextpattern, gas)

    aqueousfinal, num2 = slicing(nextpattern2, aqueous2)
    mineralfinal, num2 = slicing(nextpattern2, mineral2)
    gasfinal, num2 = slicing(nextpattern2, gas2)

    gases = split(gasfinal)
    aqueouss = split(aqueousfinal)
    minerals = split(mineralfinal)

    return gases, aqueouss, minerals


def diff_list(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif
