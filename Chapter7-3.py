a = [1, 2, 3]
print(id(a))
a = a + [4, 5]
print(id(a))

extend_a = [1, 2, 3]
print(id(extend_a))
extend_a = extend_a.extend([4, 5])
print(id(extend_a))