#알파벳 거리란, 'A' = 1, 'B' = 2, ... 'Z' = 26과 같은 방식으로 알파벳에 숫자를 할당한 뒤 계산되는 거리를 의미한다.

#예를 들어, 'B'와 'D'의 거리는 4-2 = 2 이다.
#길이가 같은 두 단어가 주어졌을 때, 각 단어에 포함된 모든 글자의 알파벳 거리의 합을 구하세요.

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', \
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
    'U', 'V', 'W', 'X', 'Y', 'Z']

#Distance of alphabets
distofal = {}
for alphabet in alphabets:
    dofa = alphabets.index(alphabet) + 1
    distofal[alphabet] = dofa
#print(distofal) ````check


def caldist(a):
    sum_dist = 0
    for letter in a:
        distance = distofal[letter]
        sum_dist += distance
    return sum_dist

def calfinal(n1, n2):
    if n1 >= n2:
        return n1 - n2
    else:
        return n2 - n1

#main
user1, user2 = list(map(str, input("Enter alphabets seperated by space: ").upper().split()))
user1_dist = caldist(user1)
user2_dist = caldist(user2)
result = calfinal(user1_dist, user2_dist)
print(result)