# a = 0
# while True:
#     a = a + 1
#     if (a % 10 == 3 or a % 10 == 6 or a % 10 == 9)and(a // 10 == 3 or a // 10 == 6 or a // 10 == 9):
#         print("**")
#     elif a % 10 == 3 or a % 10 == 6 or a % 10 == 9:
#         print("*")
#     elif a // 10 == 3 or a // 10 == 6 or a // 10 == 9:
#         print("*")
#     else:
#         print(a)
#     if a == 100:
#         break
# a= [1,2,3,4,5]
# print(a)
#
# a= [1,2,3]
# print(a[0] + a[2])
# print(a[-2])
# a= [1,2,3,['a','b','c']]
# print(a[3])
# print(a[3][0])
# print(a[-1][0])
# a = [1,2,['a','b',['life', 'is' ]]]
# print(a[2][2][0])
# print(a[2][2][1])
# a = [1,2,3,4,5]
# print(a[0:2])
# b = a[:2]
# print(b)
# c = a[2:]
# print(c)
# a= [1,2,3,['a','b','c'],4,5]
# print(a[2:5])
# print(a[3][:2])
#  a = [1,2,3]
#  b = [4,5,6]
#  print(a+b)
#  print(a*3)
#  print(len(a))
#
#  a = [1,2,3]
#  print(a[2]+"hi")
#  print(str(a[2])+"hi")
#  print(str(a[2])+"hi")
#
#  # 리스트의 수정
#  a= [1,2,3]
#  print(a)
#  a[2] = 4
#  print(a)
#  a[1] = 5
#  print(a)
#  del a[1] #제거하는것
#  print(a)
# b = []
# a = int(input())
# b.append(a)#삽입
# print(b)
# a = [1,2,3]
# a.append(4)
# print(a)
#
# a = [1,2,3,4]
# a.sort
# print(a)
# a = ['a','c','b']
# print(a)
# a.reverse()   #뒤집는거
# print(a)
# a.sort(reverse=False)#그대로 정렬
# print(a)
# a.sort(reverse=True)#거꾸로 정렬
# print(a)
# a.sort()#그대로 정렬
# print(a)
#
# a= [1,2,3]
# a.index(0) -> #리스트 안에 없어서 에러
# print(a)
#
# a= [1,2,3]
# a.insert(0,4) #삽입
# print(a)
# a.insert(1,7)
# print(a)
#
# a = [1,2,3,1,2,3]
# a.remove(3)  #제거
# print(a)
# a.remove(3)
# print(a)
#
# a = [1,2,3]
# a.remove(2)
# print(a)
# a = [4,5,6]
# a.pop(2)         #제거
# print(a)
# a.pop(0)
# print(a)
#
# a = [1,2,3,1]
# print(a.count(1))         #개수 세는거
# print(a.count(2))
#
# a = [1,2,3]
# a.extend(4,5) #확장
# print(a)
# movie = ["avengers", 'six sense', 'starwars']
# print(movie)
# movie.append("dmdkkdk")
# print(movie)
# movie.remove("six sense")
# print(movie)
#
# data = [2,4,3,1,5,10,9]
# data.sort()
# print(data)
# data.sort(reverse=True)
# print(data)
# #백준10818
# n = int(input())
# b = 1
# data = [int(input())]
# while True:
#     data.append(int(input()))
#     b = b+1
#     if n == b:
#         break
# data.sort()
# print(data[0], data[b-1])

# #1546
# a = int(input())    #과목의 개수수l = []     #리스트 원래점수
# L = []    #다른 리스트 바뀐 점수
# anw = 0    #정답변주를 0으로 초기화시켜놓음
# for i in range(a):    #a번만큼 반복
#     b = int(input())    #b값에 숫자를 입력하고
#     l.append(b)  #리스트에 b를 넣어줘
# M = max(l)
# for j in range(len()): #리스트의 길이만큼 반복 = 점수가 나와있는 과목의 개수
#     c = l[j]/M*100  #점수를 높게 조작하는 수식
#     L.append(c)     #조작된 점수를 L이라는 리스트에 넣어줘
#     anw = sum(L)/len(L)  #평균값을 anw라는 변수에 대입
# print(anw)   #anw를 출력

# t1 = ()
# t2 = (1,)  #1개의 요소만을 가질 때는 요소 뒤에 , 를 붙여야함
# t3 = (1,2,3)
# t4 = 1,2,3
# t5 = ('a','b',('ab','cd'))

# t1 = ('a', 'b', 'c')
# print(t1)
# t1 = ('a', 'b', 'd')
# print(t1)
#
# t1 = (1,2,'a','b')
# t2 = (3,4)
# print(t1= t2)
# print(t2*3)
# print(len(t1))

# Sport = {"김연아":"피겨스케이팅","류현진":"야구","손흥민":"축구}
# print(sport)
# print(type(sport))    #딕셔너리엿나

# a = {1:'hi'}
# a = {'a':[1,2,3]}
# print(a)
# print(a1)

# a = {1:'a'}
# print(a)
# a[2] = 'b'          #[]안의 값은 key, =오른쪽값은 value 가 된다
# a['name']='son'
# a[3] = [1,2,3]          #이것도 딕션얼이
# print(a)
# del a[1]
# print(a)
# print(len(a))
#
# grade = {'Son':7, 'kane':10}
# print(grade['Son'])
# print(gradep'Kane')
#
# a = {1:'a'. 2:'b'}
# print(a[1])
# print(a[2])
#
# a = {'a':1, 'b:2'}
# print(a['a'])
# print(a['b'])