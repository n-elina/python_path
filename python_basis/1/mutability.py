from copy import deepcopy

l1 = [1, 2, 3, [5, 6, 7]]
#l2 = l1.copy()
l2 = deepcopy(l1)
l2[-1].append(8)
l2.append(4)

print(l1)
print(l2)

# картежи
t = (1, 2, 3, 4, 5) # работает, как обычные списки, но они неизменяемые

# frozenset
frozenset({1, 2, 3, 4, 5, 5, 5, 5}) # работает, как множество, но неизменямое

