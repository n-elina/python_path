
s = "Hello, world!"
b = 'Hello, world!'
c = 'Hello, "world!"'
d = "Hello, 'world!'"
e = 'Hello, \'world!\''
f = "Hello, \"world!\""
g = """Hello, ""''''""world!"""
h = '''Hello, ""''''""world!'''

n = """Hello, 
world!"""
print(n)

n1 = "Hello, \nworld!"
print(n1)

email = "user@domain.com"

print(email[4])
print(email[-2])
print(email[0:4])
print(email[0:15:2])
print(email[::-1])
print(email[0:100])

print(email.split("@"))

s1 = "Hello"
s2 = 'world'
print(s1 + ", " + s2 + "!")
print("{a}, {b}!".format(a=s1, b=s2))
print(f"{s1}, {s2}!")
print(f"{s1}, {s2.upper()}!")

s = "1234"
n = 1234
assert s.isdigit()
# assert s == str(n)
assert int(s) == n




