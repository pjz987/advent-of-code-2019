# test = [1,2,2,3,3,3]
test = [1,1,1,2,2,2]
# test = [1,2,3,4,5,6]
# count = 0
rd = []
for i in range(5):
    if i != 0:
        if j > i:
            i = j
    j = i
    r = 1
    if i ==5:
        break
    if test[i] == test[i + 1]:
        r += 1
        j += 1
        while j < 5:
            if test[j] == test[j + 1]:
                r += 1
                j += 1
            else:
                rd.append(r)
                break
        if j == 5:
            rd.append(r)
    else:
        j += 1
if 2 in rd:
    print(True)

print(rd)