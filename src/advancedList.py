import random

class List:
    #some basic stuff
    def __init__(self, ls=[]):
        self.core = ls

    def __len__(self):
        return len(self.core)

    def __str__(self):
        return str(self.core)

    def __repr__(self):
        return self.core

    def __eq__(self, other):
        return self.core == other

    #convert a slice into a list
    def __unrelativateIndex(self, s, relativeindex):
        s = int(s)
        if isinstance(s, int):
            s = s + relativeindex
            return s
        else:
            return s

    def __sliceSlicer(self, theslice):
        if type(theslice) is int:
            theslice = [str(theslice), str(theslice), "None"]
        else:
            theslice = str(theslice).replace(" ","").split("(")[1].split(")")[0].split(",")
        return theslice[0], theslice[1], theslice[2]

    def __validateIndex(self, s):
        lenght = len(self.core)
        if s > 0:
            while s > lenght:
                s = s - lenght
        elif s < 0:
            while s < 0:
                s = s + lenght
        return s

    def __totalSteps(self, s0, s1):
        totalsteps = s1 - s0 + 1
        return totalsteps

    def __getitem__(self, item):
        relativeindex = int(item[1])
        s0, s1, s2 = self.__sliceSlicer(item[0])
        s0 = self.__unrelativateIndex(s0, relativeindex)  # add the relative index to the index list
        s1 = self.__unrelativateIndex(s1, relativeindex)  #add the relative index to the index list
        totalsteps = self.__totalSteps(s0, s1)  #calculate the total steps between the two indexes
        s0_reduced = self.__validateIndex(s0)  #reduce the indexes to indexes from 0 to the lenght of the list-1

        #reduce overflowing indexes
        returnlist = []
        indexreset = 0
        for i in range(s0_reduced, s0_reduced+totalsteps):
            if i+indexreset > len(self.core)-1:
                indexreset = indexreset - len(self.core)
            i = i + indexreset
            returnlist.append(self.core[i])

        if len(returnlist) == 1:
            return returnlist[0]
        else:
            return returnlist

    def randomize(self):
        return random.shuffle(self.core)

    def poprandom(self):
        return self.core.pop(random.randint(0, len(self.core)))
