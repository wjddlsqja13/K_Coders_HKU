import sys

problem = sys.argv[1]

if len(sys.argv) != 2:
    print("Please Input Problem No.")
    sys.exit()




problems_set = {
    #문제코드 : [문제 요약, 카테고리, 링크, 출처, 난이도]
    'H123456':['Defining', 'BFS', 'http...', 'HakerRank', 'Hard']
}





if problem == "All":
    print(problems_set)
else:
    if problem not in problems_set.keys():
        print("No such problem number exists")
    else:
        print('Summary: {}\nCategory: {}\nURL: {}\nPlatform: {}\nDifficulty: {}'.format(problems_set[problem][0], problems_set[problem][1], problems_set[problem][2], problems_set[problem][3], problems_set[problem][4]))