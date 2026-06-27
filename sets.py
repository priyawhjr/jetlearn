"""
a set is an unordered collection of unique elements, whcih means it can't 
contain duplicate items, and the order of elements is not guaranteed
"""
#creating a set
set_1 = {'c','a','b','c','a'}
print(set_1)
print('\n')
#Sets automatically discard duplicate values,
my_set = {1,2,3,3,4}
print(my_set,'\n')

# Converting a list to a set 
sample_list = [1,1,2,2,3,3]
sample_set = set(sample_list)
print(sample_set,'\n')
#sets are not indexable.

# Check if an element exists in the set
if 4 in sample_set:
    print("Yes")
else :
    print("No")

# Adding an element to the set. it sorts the items in increasing orders
myset = set([4,7,6,5])
myset.add(3)
myset.add(3)
myset.add(2)
myset.add(1)

print(myset)


# Removing an element from the set
myset.remove(3)
print(myset,'\n')
