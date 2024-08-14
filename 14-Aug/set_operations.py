

d1 = {1,2,3,4,5, 10}
d2 = {6,7,8,9,10, 5}

result = d1.union(d2)
print("union : ", result)

result = d1.intersection(d2)
print("intersection :", result)

result = d1.difference(d2)
print("difference :: ", result)

result = d1.symmetric_difference(d2)
print("symmetric_difference :: ", result)