#-파이썬 300제 문제-
#111
# a = input()
# print(a*2)
#112
# a = int(input())
# print(a + 10)
#113
# a = int(input())
# if a%2 == 0:
#     print("짝수")
# else:
#     print("홀수")
#114
# a = int(input())
# if a >=235:
#     print(255)
# else:
#     print(a + 20)
# 115
# a = int(input())
# if a <= 20:
#     print(0)
# else:
#     print(a - 20)
#116
# a,b = input().split(":")
# if int(b) == 00:
#     print("정각입니다")
# else:
#     print("정각이 아닙니다")
#116re
# time = input("현재시간:")
# if time[-2:] == "00":
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다.")
#117
# fruit = ["사과", "포도", "홍시"]
# a = input("좋아하는 과일은? ")
# if a in fruit:
#     print("정답입니다")
# else:
#     print("오답입니다")
# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# a = input("투자종목  ")
# if a in warn_investment_list:
#     print("투자경고종목입니다")
# else:
#     print("투자경고종목이 아닙니다")\
#119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# a = input("제가 좋아하는 계절은? ")
# if a in fruit:
#     print("정답입니다")
# else:
#     print("오답입니다")
#119re(취지에 맞음)
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# a = input("제가 좋아하는 계절은? ")
# if a in fruit.keys():
#     print("정답입니다")
# else:
#     print("오답입니다")
#120
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# a = input("제가 좋아하는 과일은? ")
# if a in fruit.values():      #key값과 value값은 다른거(key는 앞에값 value는 뒤에값)
#     print("정답입니다")
# else:
#     print("오답입니다")
#121
# a = input("알파벳을 입력하세요. ")
# if a.islower() == True:
#     print(a.upper())
# else:
#     print(a.lower())
#122
# a = int(input())
# if a >= 81 and a <= 100:
#     print("A")
# elif a >=61 and a <= 80:
#     print("B")
# elif a >=41 and a <= 60:
#     print("C")
# elif a >=21 and a <= 40:
#     print("D")
# else:
#     print("E")
#123
# a,b = input().split()
# if b == "달러":
#     print(int(a)*1167)
# elif b == "엔":
#     print(int(a)*1.096)
# elif b == "유로":
#     print(int(a)*1268)
# else:
#     print(int(a)*171)
#124
# r = [int(input()),int(input()),int(input())]
# print(max(r))
#124 for문
# r = []
# for i in range(3):
#     r.append(int(input()))
# print(max(r))
#125
# a,b,c = input().split("-")
# if a == "011":
#     print("당신은 skt사용자입니다")
# elif a == "016":
#     print("당신은 kt사용자입니다")
# elif a == "019":
#     print("당신은 LGU사용자입니다")
# else:
#     print("당신은 알수없습니다.")
#125 slice
# a = input()
# if a[0:3] == "011":       #slice 대괄호 후 0부터 3까지 중간에 :붙이기.. 3개 ex 1:2:3 붙으면 마지막은 간격
#     print("skt")
# if a[0:3] == "016":
#     print("kt")
# if a[0:3] == "019":
#     print("LGU")
# else:
#     print("알수없음")
#126
# a = int(input())
# if a[4] == "0"or"1"or"2":
#     print("강북구")
# elif a[4] == "4"or"3"or"5":
#     print("도봉구")
# elif a[4] == "7"or"8"or"9"or"6":
#     print("노원구")
#127
# a,b = input().split("-")
# c = (b[0])
# if c == 1or 3:
#     print("남자입니다")
# else:
#     print("여자입니다")
#128
# a,b = input().split("-")
# c = (b[1]+b[2])
# if c > 8:
#     print("서울이 아닙니다")
# else:
#     print("서울입니다")
#129

