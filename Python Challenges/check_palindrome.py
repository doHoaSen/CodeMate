#1
word = input("원하는 단어를 입력하세요: ")
word = list(word)

if len(word) % 2 == 0:    #문자열이 짝수인 경우는 회문이 될 수 없음
    print("회문이 아닙니다.")
else:     #문자열이 홀수인 경우
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            print("회문이 아닙니다.")
            break
    if len(word) == 1:
        print("회문이 맞습니다.")



#2
word = input("원하는 단어를 입력하세요: ")
length = len(word)

for i in range(length):
    if word[i] == word[-i-1]:
        check = 0
    else:
        check = 1
if check == 0:
    print("회문이 맞습니다.")
else:
    print("회문이 아닙니다.")