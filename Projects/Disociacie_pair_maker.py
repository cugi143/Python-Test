import string


def my_to_list(filef):
    list_f = []
    list_f = filef.readlines()
    for i in range(len(list_f)):
        list_f[i] = list_f[i].split()
    return list_f

def find_in_model(string1, string2, filef):
        for line in filef:
            list_d = line.split()
            state1,state2 = False, False
            list_return = []
            if string1 == list_d[0]:
                state1 = True
                list_return.append(list_d)
            if string2 == list_d[0]:
                state2 = True
                list_return.append(list_d)
            if state1 and state2:
                return list_return

def point_to_vec(listf):
    vec_list = []
    vec_list[0] = listf[0][0] + "-->" + listf[1][0]
    for i in range(1,len(listf[0])):
        coord = listf[1][i] - listf[0][i]
        vec_list.append(coord)
    return vec_list

def abs_vec(list_vec):
    sum = 0
    for i in range(1, len(list_vec)):
        sum += float(list_vec[i]) ** 2
    dist = sum ** (1/2)
    return dist

with open ("disociacie.txt","r", encoding="utf-8") as file_d:
    list_input = my_to_list(file_d)

with open("model2.txt", "r", encoding="utf-8") as file_m:
    for i in range(len(list_input)):
        print(list_input[i])
        list_points = find_in_model(list_input[i][1], list_input[i][2], file_m)
        vector = point_to_vec(list_points)
        distance = abs_vec(vector)

        print(vector[0] + "distance: ", distance)
