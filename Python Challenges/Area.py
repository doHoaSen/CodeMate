#메뉴에 있는 도형 선택하고 길이를 입력받아 넓이를 구하는 코드 작성하기
#조건1: 도형은 원, 삼각형, 직사각형, 정사각형
#조건2: 도형의 넓이 계산은 무조건 함수로 정의
#조건3: 도형별로 필요한 길이 입력받아야
#(원: 반지름, 삼각형: 밑변과 높이, 직사각형: 가로와 세로, 정사각형: 한 변의 길이)

def Area_Circle():
    r = int(input("원의 반지름의 길이를 입력해주세요: "))
    PI = 3.1415
    area_circle = r * r * PI
    print("반지름이 {}인 원의 넓이는 약 {}입니다.".format(r, round(area_circle, 2)))

def Area_Triangle():
    s = int(input("삼각형의 밑변의 길이를 입력해주세요: "))
    h = int(input("삼각형의 높이의 길이를 입력해주세요: "))
    area_triangle = s * h / 2
    print("밑변이 {}이고 높이가 {}인 삼각형의 넓이는 {}입니다.".format(s, h, area_triangle))

def Area_Rec():
    a = int(input("직사각형의 가로 길이를 입력해주세요: "))
    b = int(input("직사각형의 세로 길이를 입력해주세요: "))
    area_rec = a * b
    print("가로가 {}이고 세로가 {}인 직사각형의 넓이는 {}입니다.".format(a, b, area_rec))

def Area_Sq():
    a = int(input("정사각형 한 변의 길이를 입력해주세요: "))
    area_sq = a * a
    print("한 변의 길이가 {}인 정사각형의 넓이는 {}입니다.".format(a, area_sq))
    


print("""==========도형 목록==========
1. 원
2. 삼각형
3. 직사각형
4. 정사각형
============================""")

usernum = int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해주세요: "))
if usernum == 1:
    Area_Circle()
elif usernum == 2:
    Area_Triangle()
elif usernum == 3:
    Area_Rec()
elif usernum == 4:
    Area_Sq()
else:
    print("Wrong number.")