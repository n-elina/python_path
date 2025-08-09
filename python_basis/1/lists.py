# списки

l = [1, 2, 3, "a", "b", "c", [4, 5, 6]]
print(l[0])
print(l[-1])
print(l[-1][0])
print(l[::-1])

l.append("new element")
l.extend([7, 8, 9, "another element"])
print(l)
print(len(l))
l.reverse()
l[0] = 200
print(l)

# множества

s1 = {1, 2, 3, 3, 3, 4, 4}
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 8}
print(s1)
print("--------")
print(s2)
print("--------")
print(s1.intersection(s2))
print("--------")
print(s2 - s1)