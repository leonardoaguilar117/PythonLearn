from collections import deque

# Deque is a library that contains a class deque, this will help us to implements lines
line_A = deque([1, 2, 3, 4, 5, 6, 7, 8])

# Append method inserts at the end of the line a new value
line_A.append(3)

# To act like a line is necessary make a pop from the left side, becouse this is how work lists
line_A.popleft()

# Adicionaly methods we have
# clear()
# count(x)
# rotate(n=1)

print(line_A)
