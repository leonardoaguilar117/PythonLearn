# we have two options to sort a list

# First is with .sort, the inconvenient is that this function realize changes in the same list
A = [54, 68, 446, -99, 23]
# A.sort()
print(A)

# Besides, sorted function, return a new list, this for save initial list and don´t create changes in them
B = sorted(A)
print(B)

# Similary, exist a second parameter in sorted, it is the order, higher to lower
C = sorted(A, reverse=True)
print(C)


# This functions are efectives, but, not in all cases, so, it´s important that we learn sort methods
sorty = [5, 9, 3, 1, 2, 8, 4, 7, 6]

# Burble sort
n = len(sorty)
while n > 1:
    for i in range(0, len(sorty)-1):
        if sorty[i] > sorty[i+1]:
            sorty[i], sorty[i+1] = sorty[i+1], sorty[i]
    n -= 1


print(sorty)
