import math

# import pandas as pd
from scipy.stats import pearsonr
from scipy.spatial import distance

critics = {"Hans":{"A": 2.5,"B": 3.5,"C": 3.0,"D": 3.5,"E": 2.5,"F": 3.0},
         "Herta":{"A":3.0,"B":3.5,"C":1.5,"D":5.0,"E":3.5,"F":3.0},
		 "Willi":{"A": 2.5,"B": 3.0,"D": 3.5 ,"E": 4.0},
         "Beate":{"B": 3.5,	"C": 3.0,"D": 3.5,"E": 2.5},
         "Horst":{"A": 3.0,"B": 4.0,"C": 2.0,"D": 3.0,"E": 3.0,"F": 2.0},
         "Uschi":{"A": 3.0,"B": 4.0,"D": 5.0,"E": 3.5,"F": 3.0}}


#already exists in scipy.spatial but only for 1D arrays and not for dictionaries!
def euklid(p1, p2) -> float : 
    """ calculates the euklidean distance between two points
    Args:
                p1       - point one
                p2       - point two

    Return:     
                eukl     - euklidean distance between the two points

    """
    
    intersect_dict = p1.keys() & p2.keys() # when we iterate through our keys in the dict, we should iterate with keys which are in both dictionaries -> comparing the same dimensions !

    eukl = 0
    for key in intersect_dict: # we have to make n steps
        eukl += (p1[key] - p2[key])**2

    eukl = 1/(1+math.sqrt(eukl))
    return eukl


def pearson(p1, p2) -> float : 
    """ calculates the pearson coefficient

    Args:
                p1      - point one
                p2      - point two

    Return:     
                pearson     - pearson coefficient of the two points
    """

    intersect_dict = p1.keys() & p2.keys()

    p1_el = [0 for x in intersect_dict]
    p2_el = [0 for x in intersect_dict]
    i = 0

    for key in intersect_dict: # get the values of the same dimensions and put them accordingly into 1D arrays to use the pearson coefficient function
        p1_el[i] = p1[key]
        p2_el[i] = p2[key]
        i += 1
    pearson,_ = pearsonr(p1_el, p2_el)  # you a tuple returned from this function but we only want the pearson corr
    return pearson


def calc_pears_eukl(critics) -> dict:
    """ calculates the pearson coefficient and the euklidean distance of an nested dictionary.

    Args:
                critics     - a nested dictionary with the data

    Return:
                sim         - a nested dictionary with sorted compared pearson coefficient and euklidean distance and their parameters of critics as key(their names)
    """
    sim = {}
    sets = list()
    for key1 in critics:
        for key2 in critics:
            if(key1 != key2 and {key1,key2} not in sets):   # we don't want the combinations of someone with themself or combinations we already had!
                sets.append({key1,key2})
                eukl = euklid(critics[key1], critics[key2])
                pears = pearson(critics[key1], critics[key2])
                sim[f"{key1}, {key2}"] = {"euklid" : eukl, "pearson" : pears}

    sim = dict(sorted(sim.items(), key=lambda item: item[1]['pearson'],reverse=True)) #sort descending by pearson, https://www.geeksforgeeks.org/sort-a-nested-dictionary-by-value-in-python/
    
    return sim

print(calc_pears_eukl(critics))



    





