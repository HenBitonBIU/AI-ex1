'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
from collections import namedtuple
from ways import load_map_from_csv
from collections import Counter
def map_roadTypes(roads):
    cnt = Counter()
    for type in roads.values():
        for y in type[3]:
            cnt[y[3]] += 1
    return cnt
def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    distSum = 0
    countSum = 0
    distMax=0
    distMin=10000000
    links=len(roads)
    sumOfLinks=sum(len(x[3]) for x in roads.values())
    max1=max(len(x[3]) for x in roads.values())
    min1=min(len(x[3]) for x in roads.values())

    for x in roads.values():
        for y in x[3]:
            distSum += y[2]
            countSum+=1
    avg=sumOfLinks/links
    for x in roads.values():
        for y in x[3]:
           if y[2] > distMax:
               distMax = y[2]
    for x in roads.values():
        for y in x[3]:
            if y[2] < distMin:
                distMin = y[2]

    return {
        'Number of junctions' :links,
        'Number of links' : sumOfLinks,
        'Outgoing branching factor' : Stat(max=max1, min=min1, avg=avg),
        'Link distance' : Stat(max=distMax, min=distMin, avg=distSum/countSum),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram' : map_roadTypes(roads),  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))

        
if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()
