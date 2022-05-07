# license_plate = "41245432 2210"
#
# print(license_plate[-4: ])
#
# string = "홀짝홀짝홀짝"
# print(string[::2])

# string = 'PYTHON'
# print(string[::-1])

# phone_number = "010-1111-2222"
# print(phone_number.replace('-',' '))

# string = 'abcdefe2a354a32a'
# string = string.replace('a', 'A')
# print(string)
#
# t1 = 'python'
# t2 = 'java'
# t = t1 + " " + t2 + " "
# print(t*4)

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
#%
# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))
#format 메쏘드
# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}" .format(name2, age2))
#f-string
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# 상장주식수 = "5,969,782,550"
# 상장주식수.replace(',',' ')
# print(상장주식수)


# data = "....삼성.전자..."
# print(data.strip('.'))
# print(data.rstrip('.'))
# print(data.lstrip('.'))

# a = int(input())
# print(a+10)

#a = int(input())
# if a % 2 ==0:
#     print("짝수")
# else:
#     print("홀수수)

# a = int(input())
# if 235 < a:
#     print("255")
# else:
#     print(a + 20)

# a = int(input())
# if 275 < a:
#     print("255")
# elif 20 > a:
#     print(0)
# else:
#     print(a - 20)

# fruit = ["사과", "포도", "홍시"]
# a = input("좋아하는 과일은?")
# if a in fruit:
#     print("정답입니다")
# else:
#     print("오답입니다")

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# a = input("제가 좋아하는 계절은:")
#
# if a in fruit.keys():
#     print("정답입니다")
# else:
#     print("오답입니다")
#
# for i in range(1,4):
#     print(i*10)

# for i in range(1,4):
#       print(i*10)
#       print("-------")

# a = 1
# while True:
#     if a%3 == 0:
#         print(a)
#     a = a+1
#     if a == 31:
#         break

for in i range(3,31,3)
    print(i)
a = [" "," "," "," "," "," "," "," "," "," "]
def tictacto():
    print(a[1] + "  ㅣ  " + a[2] + " ㅣ  " + a[3])
    print(" ㅡㅡㅡㅡㅡㅡㅡ")
    print(a[4] + "  ㅣ  " + a[5] + " ㅣ  " + a[6])
    print(" ㅡㅡㅡㅡㅡㅡㅡ")
    print(a[7] + "  ㅣ  " + a[8] + " ㅣ  " + a[9])
import random
tictacto()
jungbok = [1,2,3,4,5,6,7,8,9]
while True:
    b = int(input())
    a[b] = "O"
    tictacto()
    jungbok.remove(b)
    c = random.randrange(1,10)
    print("상대:",c)
    a[c] = "X"
    tictacto()
    jungbok.remove()








