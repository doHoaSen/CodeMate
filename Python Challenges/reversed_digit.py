# 어떤 수 X가 주어졌을 때, X의 모든 자리수를 뒤집은 수를 r(X)라고 하자.
# 예를 들어, X가 123일 때 r(X)는 321이다.
# 두 양의 정수 X, Y가 입력으로 주어질 때 r( r(X) + r(Y) )를 구하세요.


x, y = input("Enter two numbers: ").split()
rx, ry = x[::-1], y[::-1]
num = int(rx) + int(ry)
result = str(num)[::-1]
print(result)