# def is_symmetric(strr):
#     ll = len(strr)
#     if ll == 1 or ll == 2:
#         return True
#     flag = True
#     if ll % 2 == 0:
#         for i in range(int(ll / 2)):
#             if strr[i] != strr[ll - i - 1]:
#                 flag = False
#                 return flag
#         return flag
#     else:
#         for i in range(int((ll - 1) / 2)):
#             if strr[i] != strr[ll - i - 1]:
#                 flag = False
#                 return flag
#         return flag
#
#
# def num_of_longest_sym(string):
#     l = len(string)
#     window = 1
#     head = 0
#     res_len = 0
#     while head + window <= l:
#         temp = is_symmetric(string[head:(head + window)])
#         if temp:
#             res_len = window
#             window += 1
#             head = 0
#             continue
#         else:
#             if head + window < l:
#                 head += 1
#             else:
#                 head = 0
#                 window += 1
#     return res_len
#
#
# while True:
#     try:
#         line = input().strip()
#         print(num_of_longest_sym(line))
#     except:
#         break

# 以上为自己写的，太慢了。。。
###################################################################################################################
# 以下为高效写法
def max_len(s):
    abba = []
    aba = []
    for i in range(len(s) - 1): # 找到两种类型 “aba" 和 "abba" 的中心点，之后以这些中心点为中心，逐步向两边扩展，找到最大长度
        current = i
        next_one = i + 1
        if s[current] == s[next_one]:
            abba.append(i)
        elif s[current - 1] == s[next_one]:
            aba.append(i)
    length = []
    for j in abba:
        first = j
        last = j + 1
        while first >= 0 and last < len(s) and s[first] == s[last]:
            first += -1
            last += 1

            length.append(last - first - 1)
    for k in aba:
        first = k - 1
        last = k + 1
        while first >= 0 and last < len(s) and s[first] == s[last]:
            first += -1
            last += 1
            length.append(last - first - 1)
    if len(length) == 0:
        return 0
    else:
        return max(length)


while True:
    try:
        s = input()
        print(max_len(s))
    except:
        break
