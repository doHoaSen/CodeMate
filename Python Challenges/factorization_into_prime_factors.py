#소인수분해 프로그램 작성하기
#def
def factorization(n):
    while n != 1:
        for factor in range(2, n+1):
            if n % factor == 0:
                n //= factor
                print(factor)
                break   #break가 들어가야 하는 이유: '소인수'로 분해하기 위해

#main
num = int(input("숫자를 입력해주세요: "))
factorization(num)
