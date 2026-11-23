
# 1. Set Operations

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print("Set A:", a)
print("Set B:", b)

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# Add an element
a.add(50)
print("After Add:", a)

# Remove an element
a.remove(10)
print("After Remove:", a)


# 2. Frozen Set

x = frozenset([1, 2, 3, 4])

print("\nFrozen Set:", x)
print("Is 2 present?", 2 in x)

# Frozen set cannot be modified


# 3. For Loop

print("\nFor Loop:")
for i in range(1, 6):
    print(i)


# 4. While Loop

print("\nWhile Loop:")
i = 1

while i <= 5:
    print(i)
    i += 1
