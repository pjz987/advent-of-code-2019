def decoder(input, address, intcode_list, output_list):
    instruction = intcode_list[address]
    opcode = instruction % 100
    p1mode = instruction % 1000 // 100
    p2mode = instruction % 10000 // 1000
    p3mode = instruction // 10000
    halt = False

    if opcode in range(1, 3):
        parameters = intcode_list[address + 1 : address + 4]
        jump_forward = 4

        if p1mode:
            p1 = intcode_list[parameters[0]]
        else:
            p1 = parameters[0]
        if p2mode:
            p2 = intcode_list[parameters[1]]
        else:
            p2 = parameters[1]
        if p3mode:
            p3 = intcode_list[parameters[2]]
        else:
            p3 = parameters[2]


        if opcode % 10 == 1:
            intcode_list[p3] = p1 + p2
        elif opcode % 10 == 2:
            intcode_list[p3] = p1 * p2

    elif opcode in range(3,5):
        parameter = intcode_list[address + 1]
        # if p1mode:
        #     p = parameter
        # else:
        #     p = intcode_list[parameter]
        p = parameter
        jump_forward = 2

        if opcode == 3:
            intcode_list[p] = input
        elif opcode == 4:
            output_list.append(intcode_list[p])
            # print(parameter)

    elif opcode == 99:
        halt = True
        jump_forward = 0

    return intcode_list, jump_forward, output_list, halt



with open('day05-input.txt', 'r') as puzzle_input:
    input_string = puzzle_input.read()
string_list = input_string.split(',')
intcode_list = []
for string in string_list:
    integer = int(string)
    intcode_list.append(integer)
# print(intcode_list)
# print(len(intcode_list))
# while True:
#     index = int(input("Index: "))
#     print(intcode_list[index])

#test
# intcode_list = [3, 0, 4, 0, 99]
address = 0
input = 1
output_list = []
jump_forward_total = 0
count = 0
while jump_forward_total < len(intcode_list):
    print(count)
    count += 1
    intcode_list, jump_forward, output_list, halt = decoder(input, address, intcode_list, output_list)
    if halt == True:
        break
    else:
        jump_forward_total += jump_forward
        address += jump_forward
print(output_list)
