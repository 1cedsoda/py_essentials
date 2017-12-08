import advancedList
ls1 = advancedList.List()  #first way to generate ...
ls1.core = [0,1,2,3,4]  # ...and fill the object.
print("[0,1,2,3,4]")
print("[index1 : index2, relativeIndex]")
print("[1,0]    ",ls1[1,0])
print("[1:1,0]  ",ls1[1:1,0])
print("[1:1,3]  ",ls1[1:1,3])
print("[1:1,-1] ",ls1[1:1,-1])
print("[0:4,1]  ",ls1[0:4,1])
print("[0:4,-5] ",ls1[0:4,-5])
print("[0:6,0]  ",ls1[0:6,0])
print("[-9:-4,5]",ls1[-9:-4,5])

print("")
ls2 = advancedList.List([0,1,2,3,4]) #second way to generate and fill the Object
ls2.core.append(5) #Basic list-edits like append, pop and more have to be used with the core variable.
print("printing the object:",ls2)
print("printing the core:  ",ls2.core)
print("mirror the List:", ls2.mirror())  # Mirror the core. True or False to keep changes. True is default.
print("randomize the List:", ls2.randomize())  # Randomize the order. True or False to keep changes. True is default.
print("pop a random value:", ls2.poprandom())  # Pop a random value. True or False to keep changes. True is default.

