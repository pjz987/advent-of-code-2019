def lists_of_four(intcode_list):
    intcode_fours = []
    slice1 = 0
    slice2 = 4
    while len(intcode_fours) < (len(intcode_list) / 4):
        intcode_fours.append(intcode_list[ slice1 : slice2 ])
        slice1 = slice2
        slice2 += 4
    return intcode_fours

def flat_list(intcode_fours):
    intcode_list = []
    for four in intcode_fours:
        for i in four:
            intcode_list.append(i)
    return intcode_list

def instruction(opcode, p1, p2, p3):
    pass

def noun_and_verb(intcode_list):
    pass

def decoder(intcode_list):
    intcode_fours = lists_of_four(intcode_list)
    four_list = 0
    while four_list < (len(intcode_list) / 4):
    # for four in intcode_fours:
        four = intcode_fours[four_list]
        opcode = four[0]

        if opcode == 99: #end program if 99
            # print(intcode_list) #test print
            return intcode_list[0]

        input1 = four[1]
        input2 = four[2]
        output = four[3]

        if opcode == 1: #add if 1
            intcode_list[output] = intcode_list[input1] + intcode_list[input2]

        if opcode == 2: #multiply if 2
            intcode_list[output] = intcode_list[input1] * intcode_list[input2]

        intcode_fours = lists_of_four(intcode_list)
        four_list += 1

with open("day02input.txt", 'r') as raw_txt:
    string_intcode = raw_txt.read()
intcode_list = string_intcode.split(',')
for i, integer in enumerate(intcode_list):
    intcode_list[i] = int(integer)
intcode_list1 = intcode_list

for i in range(0, 100):
    for j in range(0, 100):
        intcode_list = intcode_list1
        intcode_list[1] = i
        intcode_list[2] = j
        try:
            if decoder(intcode_list) == 19690720:
                print(f"noun = {intcode_list[1]} verb = {intcode_list[2]}")
        except:
            pass
                # print(f"noun = {intcode_list[1]} verb = {intcode_list[2]}")

intcode_list[1] = 12
intcode_list[2] = 2

# print(decoder(intcode_list))

# if decoder(intcode_list) == 6730673:
#     print(True)
#print tests:     
# print(intcode_list)
# print(lists_of_four(intcode_list))
# print(flat_list(lists_of_four(intcode_list)))

# test_list1 = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
# print(decoder(test_list1))

# test_list2 = [1,0,0,0,99]
# print(decoder(test_list2))

# test_list3 = [2, 3, 0, 3, 99]
# print(decoder(test_list3))

# test_list4 = [2,4,4,5,99,0]
# print(decoder(test_list4))

# test_list5 = [1,1,1,4,99,5,6,0,99]
# print(decoder(test_list5))