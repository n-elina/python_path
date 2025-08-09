# словари

d = {
    "a": "1",
    "b": 2,
    "c": 3
}

user1 = {
    "name": "Vasya",
    "age": 22,
    "id": 25
}

user2 = {
    "name": "Petya",
    "age": 20
}

users = {
    25: user1,
    42: user2
}

print(users[42])
print(user1["name"])
print(user2["age"])

users[55] = {"name": "Oleg", "age": 18}
print(users)

print("-------")
from pprint import pprint
pprint(list(users.items()))

users.values()
users.keys()
print(users.get(60, {"name": "default user"}))
print(users[42])
