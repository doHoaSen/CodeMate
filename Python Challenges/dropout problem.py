"""
수많은 사람이 모각코에 참여했고, 단 한 명을 제외한 모두가 수료함
수료하지 못한 사람의 이름 리턴
조건: 동명이인 존재


함수호출예시
solution(['곰', '김변수', '망고'], ['망고', '김변수'])
출력예시
곰
"""



#def 작성
def solution(a, b):
    for i in b:
        if i in a:
            a.remove(i)
    print(a[0])


#main
applicant = input("참여자 이름을 공백을 기준으로 입력하세요: ").split()
successful = input("수료자 이름을 공백을 기준으로 입력하세요: ").split()
solution(applicant, successful)


