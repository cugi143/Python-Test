import random

def create_list():
    list = []
    list_q = ['A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D']
    for i in range(40):
        list_person = []
        for j in range(10):
            list_person.append(random.choice(list_q))



        list.append(list_person)
    return list

def eval(list_in):
    list_out = []
    list_person = []
    list_eval = [0.6, 0.8, 0.7, 0.6, 0.5, 0.7, 0.5, 0.6, 0.9, 0.8]
    sum_eval = 6.7

    for i in range(40):
        sum = 0
        depressed = False
        for j in range(10):
            if list_in[i][j] == 'A':
                sum += 0
            elif list_in[i][j] == 'B':
                sum += list_eval[j] * 2
            elif list_in[i][j] == 'C':
                sum += list_eval[j] * 4
            elif list_in[i][j] == 'D':
                sum += list_eval[j] * 8
        score = sum / sum_eval
        if score >= 4.7:
            depressed = True
            print('KURVA')
        list_person.append(score)
        list_person.append(depressed)

        list_out.append(list_person)
    return list_out

def answer_count(list_in):
    list_out = []
    for i in range(10):
        list_question = [0, 0, 0, 0]
        for j in range(40):
            if list_in[j][i] == 'A':
                list_question[0] += 1
            elif list_in[j][i] == 'B':
                list_question[1] += 1
            elif list_in[j][i] == 'C':
                list_question[2] += 1
            elif list_in[j][i] == 'D':
                list_question[3] += 1
        list_out.append(list_question)
    return list_out



list_answers = create_list()
list_scores = eval(list_answers)
list_count = answer_count(list_answers)
print(list_count)
print(list_scores)