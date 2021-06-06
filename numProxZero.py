"""
    To find the temperature closest to zero
"""
temp = [2, 15, -1, 0, -3]
idealTemp=temp[0]
for t in temp:
    mem = t
    for t in temp:
        # temperature positive
        if (mem > t > 0):
            idealTemp = mem
        # temperature negative
        elif (mem <= 0) and (((mem*(-1)) < idealTemp) or mem == 0):
            idealTemp = mem

print(idealTemp)

