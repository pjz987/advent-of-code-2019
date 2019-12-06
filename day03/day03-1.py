def pathfinder(move_list):#returns a path of every position in move list
    wire_path = []#empty list for the entire path of wire1
    wire_dict = {'X': 0, 'Y': 0}
    for move in move_list:

        if move[0] == 'R':
            for i in range(move[1]):
                append_list = [wire_dict['X'] + (i + 1), wire_dict['Y']]
                wire_path.append(append_list)
            wire_dict['X'] += move[1]

        if move[0] == 'L':
            for i in range(move[1]):
                append_list = [wire_dict['X'] - (i + 1), wire_dict['Y']]
                wire_path.append(append_list)
            wire_dict['X'] -= move[1]

        if move[0] == 'U':
            for i in range(move[1]):
                append_list = [wire_dict['X'], wire_dict['Y'] + (i + 1)]
                wire_path.append(append_list)
            wire_dict['Y'] += move[1]

        if move[0] == 'D':
            for i in range(move[1]):
                append_list = [wire_dict['X'], wire_dict['Y'] - (i + 1)]
                wire_path.append(append_list)
            wire_dict['Y'] -= move[1]

    return wire_path

def move_list_maker(wire_raw):#returns a move list of each wire
    move_list = [] #creates a list of lists with the direction ('R', 'L', 'U', 'D') string and integer
    for move in wire_raw:
        sub_list = [move[0], int(move[1:])]
        move_list.append(sub_list)
    return move_list

def list_splitter(string_with_commas):#splits comma string into list (used for tests)
    out_list = string_with_commas.split(',')
    return out_list

def nearest_crosspoint_finder(path1, path2):#returns manhattan distance
    cross_path_list = []
    for position in path1:
        if position in path2:
            cross_path_list.append(position)

    manhattan_list = []
    for crossing in cross_path_list:
        manhattan_list.append(abs(crossing[0]) + abs(crossing[1]))
    
    manhattan_distance = min(manhattan_list)
    return manhattan_distance


with open('day03input.txt', 'r') as all_input:
    input_string = all_input.read()
two_lists = input_string.split('\n')
wire1_raw = two_lists[0].split(',')
wire2_raw = two_lists[1].split(',')


#important keep
wire1 = move_list_maker(wire1_raw) 
wire2 = move_list_maker(wire2_raw)


path1 = pathfinder(wire1)
path2 = pathfinder(wire2)

print(nearest_crosspoint_finder(path1, path2))





# wire2 = [] #does the same for wire2
# for move in wire2_raw:
#     sub_list = [move[0], int(move[1:])]
#     wire2.append(sub_list)

# test_move_list = move_list_maker(['R8', 'U5' , 'L5', 'D3'])
# print(pathfinder(test_move_list))

# test1a = list_splitter('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51')
# test1b = list_splitter('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')

# move_list1a = move_list_maker(test1a)
# move_list1b = move_list_maker(test1b)

# path1a = pathfinder(move_list1a)
# path1b = pathfinder(move_list1b)

# print(nearest_crosspoint_finder(path1a, path1b))