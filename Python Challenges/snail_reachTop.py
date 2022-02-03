#높이 N인 나무
#낮에 A미터만큼 올라가고 밤에 B미터만큼 내려옴
#output: 며칠만에 정상으로? (정상 불가능시 -1 출력)

"""
input: A, B, N
output: date
"""

# write def
def ToTheTop(a, b, n):
    if a <= b:
        date = -1
    elif a >= n:
        date = 1
    else:
        met = 0
        date = 0
        while met < n:
            date += 1
            met += a
            if met >= n:
                break
            met -= b
    return date

#main
A, B, N = map(int, input("올라갈 높이, 내려갈 높이, 나무높이를 공백으로 구분해 입력하시오: ").split())
Date = ToTheTop(A, B, N)
print("소요일:", Date, "일")