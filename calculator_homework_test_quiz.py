'''
Anas Albedaiwi
albedaiwi1994@gmail.com
'''

Homework_max = [40, 40, 40, 40, 40, 5]
Homework_score = [39, 40, 29, 40, 0, 5]
Quizzes_max = [10, 10, 10, 10, 10, 10, 10]
Quizzes_score = [10, 10, 9, 2, 10, 10, 10]
Tests_max = [300, 300, 300]
Tests_score = [293, 284, 300]

score_list = [sum(Homework_score), sum(Quizzes_score), sum(Tests_score)]
max_list = [sum(Homework_max), sum(Quizzes_max), sum(Tests_max)]


def average(score_list, max_list):
    print('Score: ' + str(score_list / max_list))


def letter_grade(percent):
    if percent >= .9:
        print('A')
    elif percent >= .8:
        print('B')
    elif percent >= .7:
        print('C')
    elif percent >= .6:
        print('D')
    else:
        print('F')


def average_weighted(score_list, max_list):
    homework_weight = (score_list[0] / max_list[0])*.2
    quizzes_weight = (score_list[1] / max_list[1])*.2
    test_weight = (score_list[2] / max_list[2])*.6
    total_weighted = homework_weight + quizzes_weight + test_weight
    print ('Final Score: ' + str(total_weighted))


def main():
    print('Homework:')
    average(score_list[0], max_list[0])
    percent = score_list[0] / max_list[0]
    letter_grade(percent)
    print('Quizzes:')
    average(score_list[1], max_list[1])
    percent = score_list[1] / max_list[1]
    letter_grade(percent)
    print('Tests:')
    average(score_list[2], max_list[2])
    percent = score_list[2] / max_list[2]
    letter_grade(percent)
    average_weighted(score_list, max_list)
    percent = sum(score_list) / sum(max_list)
    letter_grade(percent)

main()

