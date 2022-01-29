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
#  del a[1]
#  print(a)
# b = []
# a = int(input())
# b.append(a)
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
# a.reverse()
# print(a)
# a.sort(reverse=False)
# print(a)
# a.sort(reverse=True)
# print(a)
# a.sort()
# print(a)
#
# a= [1,2,3]
# a.index(0) -> #리스트 안에 없어서 에러
# print(a)
#
# a= [1,2,3]
# a.insert(0,4)
# print(a)
# a.insert(1,7)
# print(a)
#
# a = [1,2,3,1,2,3]
# a.remove(3)
# print(a)
# a.remove(3)
# print(a)
#
# a = [1,2,3]
# a.remove(2)
# print(a)
# a = [4,5,6]
# a.pop(2)
# print(a)
# a.pop(0)
# print(a)
#
# a = [1,2,3,1]
# print(a.count(1))
# print(a.count(2))
#
# a = [1,2,3]
# a.extend(4,5)
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