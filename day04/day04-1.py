with open('day04-input.txt', 'r') as raw:
    raw_range = raw.read()
list_range_string = raw_range.split('-')
list_range = []
for number in list_range_string:
    int_number = int(number)
    list_range.append(int_number)
# print(list_range)
count = 0
for number in range(list_range[0], list_range[1]):
    double_digit = False #double digits like 11, 22, 33, etc. in number
    no_decrease = True #digits increase from left to right
    for i in range(5):
        if double_digit == False:
            if int(str(number)[i]) == int(str(number)[i + 1]):
                double_digit = True
        if no_decrease == True:
            if int(str(number)[i]) > int(str(number)[i + 1]):
                no_decrease = False
                break
    if double_digit == True and no_decrease == True:
        count += 1
        print(number)
print(count)