set1 = {1,2,3}
set2 = {3,4}

set1.update(set2)
print(set1)

# new_set = set1.union(set2)
new_set = set1 | set2

print(new_set)