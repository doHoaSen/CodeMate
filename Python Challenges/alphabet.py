#알파벳 대소문자로 된 문장이 주어질 때, 가장 많이 사용된 알파벳 무엇인지 출력하기
#조건1: 대소문자 구분 x --> lower() 이용
#가장 많이 사용된 알파벳 여러개일 때 모두 출력하기

def alphabets(s):
    s = s.lower()   #대소문자 구분 X
    s_list = list(set(s))   #중복제거
    cnt_list = []
    for i in s_list:
        cnt = s.count(i)
        cnt_list.append(cnt)
    
    alphabet = []
    for i in range(len(cnt_list)):
        if cnt_list[i] == max(cnt_list):
            alphabet.append(s_list[i])

    print(alphabet)

    

#main
sentence = input()
alphabets(sentence)