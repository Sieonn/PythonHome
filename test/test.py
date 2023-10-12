# #        sui = []
# #        for i in range(0, len(my_string),4):
# #               sui.append(my_string[i:i+4]
# #                          return sui
          
# # my_string = "asdfghjlk;zx"
# # print(solution(my_string))
# def solution(my_string, m, c):
#     # for i in range(0, len(my_string), m):
#     #     print(my_string[i:i+m][2])
#     # return 
#         # sui.append(my_string[i:i+m])
#     cun = 0
#     for i  in range(len(my_string)):
#         if i % 4 == 0 and i != 0:
#             print(my_string[i], end=' ')
#         else:
#             print(chr(i),end=' ') 
#         cun += 1 
#         if cun % 5 == 0:
#             print()

# my_string = "asdfghjlk;zx"
# m =  4
# c = 2
# print(solution(my_string, m, c))

# def solution(my_string, m, c):
#     return my_string[c-1::m]
# my_string = "asdfghjlk;zx"
# m =  4
# c = 2
# print(solution(my_string, m,c))

# def sol(s,m):
#     s.split('',m)
#     print(s)
# s = "12345678"
# m = 4
# c = 2
           
# print(sol(s,m)) 


# def solution(my_string):
#     answer=[0]*52
#     for x in my_string:
#         if x.isupper():
#             answer[ord(x)-65]+=1
#         else:
#             answer[ord(x)-71]+=1
#     return answer
# my_string= "Programmers"
# print(solution(my_string))

# list = [123]*3
# print(list)

# def solution(n, k):
#     a = []
#     for i in range(1, n+1):
#         if i % k == 0:
#             a.append(i)
#     return a
# n = 10
# k = 3
# print(solution(n, k))

# def solution(my_string, indices):
#     new_str = ''
#     for v in my_string:
#         for i in indices:
#             if v != my_string[i]:
#                 new_str += v
#     return new_str
# my_string = "apporoograpemmemprs"
# indices = [1, 16, 6, 15, 0, 10, 11, 3]

# print(solution(my_string, indices))

# def solution(my_string, indices):
#     new = ''
#     for i in range(len(my_string)):
#         if i not in indices:
#             new += my_string[i]
                     
#     return new
# my_string = "apporoograpemmemprs"
# indices = [1, 16, 6, 15, 0, 10, 11, 3]

# print(solution(my_string,indices))

def solution(arr, idx):
    for i in range(len(arr)):
        if i >= idx and arr[i] == 1 :
            return i
    if i < idx or arr[i] != 1:
        return -1
arr = [0, 0, 0 , 1]
idx = 1
print(solution(arr, idx))