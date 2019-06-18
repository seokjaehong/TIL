# A Counter is a dict subclass for counting hashable objects.
# It is an unordered collection where elements are stored
# as dictionary keys and their counts are stored as dictionary values.
# Counts are allowed to be any integer value including zero or negative counts.
# The Counter class is similar to bags or multisets in other languages.


a = [1, 2, 3, 1, 5, 3, 2, 2, 4, 5, 5]
print(max(set(a), key=a.count))
print(min(set(a), key=a.count))

from collections import Counter

# 1.list
a = [1, 2, 3, 1, 5, 3, 2, 2, 4, 5, 5]
print("1.list")
print(Counter(a), "\n")

# 2.dict
print("2.dict")
b = {'가': 3, '나': 2, '다': 4}
cnt = Counter(b)
print(cnt, "\n")

# 3.value=count
print("3.value=count")
c = Counter(a=2, b=3, c=2)
print(Counter(c))
print(sorted(c.elements()), "\n")

# 4.string
print("4.string")
container = Counter()
print(container)
container.update("aabcdeffgg")
print(container)
for k, v in container.items():
    print(k, ':', v)

# 5.elements
print("5.elements")
import collections
c = collections.Counter("Hello Python")
print(list(c.elements()))
print(sorted(c.elements()))

# 6.most_commons
print("6.most_commons")
c2 = collections.Counter('apple, orange, grape')
print(c2.most_common())
print(c2.most_common(3))

# 7.subtract
print("7.subtract")
c3 = collections.Counter('hello python')
print(c3)
c4 = collections.Counter('i love python')
print(c4)
c3.subtract(c4)
print(c3)


