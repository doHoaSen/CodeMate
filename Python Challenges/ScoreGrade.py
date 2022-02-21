#시험 점수를 입력받고, 그에 따른 등급과 총 평균을 계산하는 프로그램을 작성해주세요.

#조건 1 : 시험 점수는 0에서 100점 사이입니다.
#조건 2 : 점수당 등급은 다음과 같습니다.
#90이상 100이하 : A, 80이상 90미만 : B, 70이상 80미만 : C, 60이상 70미만 : D, 60미만 : F

def cal_grade(n):
    if n <= 100 and n >= 90:
        grade = "A"
    elif n >= 80:
        grade = "B"
    elif n >= 70:
        grade = "C"
    elif n >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

numsubjcet = int(input("Enter number of subjects: "))
score_list = []
for i in range(numsubjcet):
    score = int(input("Enter a score of subject: "))
    score_list.append(score)
    scoreofgrade = cal_grade(score)
    print("Grade of the subject is ", scoreofgrade)


average = sum(score_list) / len(score_list)
print()
print("The average of the exam is", round(average, 2))