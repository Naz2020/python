'''
Anas Albedaiwi
albedaiwi1994@gmail.com
'''

def to_percent(score_list, max_list):
    perc_list=[]
    for i in range(0, len(score_list)):
        perc = round(score_list[i]/max_list[i],2)
        perc_list.append(perc)
    return perc_list
def median(score_list, max_list):
    perc_list=to_percent(score_list, max_list)
    perc_list.sort()
    half = len(perc_list) // 2

        
    if not len(perc_list) % 2:
        return (perc_list[half - 1] + perc_list[half]) / 2.0
    return perc_list[half]

score_list = [100,100]
max_list = [61,85]
to_percent(score_list, max_list)
med=median(score_list, max_list)
print(med)
