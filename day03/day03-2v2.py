def pathfinder2(move_list):#returns a path of every position in move list #v2 now with steps
    wire_path = []#empty list for the entire path of wire1
    wire_dict = {'X': 0, 'Y': 0, 'S': 0} #'S' for steps
    for move in move_list:

        if move[0] == 'R':
            for i in range(move[1]):
                append_list = [wire_dict['X'] + (i + 1), wire_dict['Y'], wire_dict['S'] + (i +1)]
                wire_path.append(append_list)
            wire_dict['X'] += move[1]
            wire_dict['S'] += move[1]

        if move[0] == 'L':
            for i in range(move[1]):
                append_list = [wire_dict['X'] - (i + 1), wire_dict['Y'], wire_dict['S'] + (i +1)]
                wire_path.append(append_list)
            wire_dict['X'] -= move[1]
            wire_dict['S'] += move[1]

        if move[0] == 'U':
            for i in range(move[1]):
                append_list = [wire_dict['X'], wire_dict['Y'] + (i + 1), wire_dict['S'] + (i +1)]
                wire_path.append(append_list)
            wire_dict['Y'] += move[1]
            wire_dict['S'] += move[1]

        if move[0] == 'D':
            for i in range(move[1]):
                append_list = [wire_dict['X'], wire_dict['Y'] - (i + 1), wire_dict['S'] + (i +1)]
                wire_path.append(append_list)
            wire_dict['Y'] -= move[1]
            wire_dict['S'] += move[1]

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

def nearest_crosspoint_finder2(path1, path2):#returns manhattan distance #v2 now for steps
    cross_path_list = []
    for position1 in path1:
        for position2 in path2:
            if position1[:2]  == position2[:2]:
                new_crosspoint = [position1, position2]
                cross_path_list.append(new_crosspoint)

    manhattan_list = []
    for crosspoint in cross_path_list:
        manhattan_distance =  crosspoint[0][2] + crosspoint[1][2]
        manhattan_list.append(manhattan_distance)
    
    shortest_manhattan_distance = min(manhattan_list)
    return shortest_manhattan_distance


with open('day03input.txt', 'r') as all_input:
    input_string = all_input.read()
two_lists = input_string.split('\n')
wire1_raw = two_lists[0].split(',')
wire2_raw = two_lists[1].split(',')

'''
Below is the actual problem.
Code out when doing test runs.
'''
#important keep
wire1 = move_list_maker(wire1_raw) 
wire2 = move_list_maker(wire2_raw)


path1 = pathfinder2(wire1)
path2 = pathfinder2(wire2)

print(nearest_crosspoint_finder2(path1, path2))




'''
Everything below is for test runs.
Code out when testing full program.
'''

# test_move_list = move_list_maker(['R8', 'U5' , 'L5', 'D3'])
# print(pathfinder(test_move_list))

# test1 = list_splitter('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51')
# test2 = list_splitter('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')

# move_list1 = move_list_maker(test1)
# move_list2 = move_list_maker(test2)

# path1 = pathfinder2(move_list1)
# path2 = pathfinder2(move_list2)

# print(nearest_crosspoint_finder2(path1, path2))