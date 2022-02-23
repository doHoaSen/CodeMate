#양의 정수 n의 각 자리수 제곱의 합을 계산한다. 그렇게 해서 나온 합도 각 자리수의 제곱의 합을 계산한다.
#이렇게 반복해서 1이 나온다면, 해당 수는 상근수 라고 한다.
#양의 정수 N이 입력으로 주어졌을 때, N보다 작거나 같은 모든 상근수를 구해 출력 해 보세요.
def findnum(n):
    n = str(n)
    number=[]
    number.append(n)
    for m in number:  
        result=0
        for i in range(len(m)):
            num = m[i]
            result=result + (int(num) ** 2)
        result = str(result)
        if result == '1':
            return True
        elif result in number:
            break
        number.append(result)



num = int(input("Enter a number: "))



#Print Answer
for i in range(1, num+1):
    if findnum(i) == True:
        print(i, end =" ")