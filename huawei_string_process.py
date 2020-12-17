r = list("0123456789abcdefABCDEF")

def reverse_bits_4(n):
    return "{:x}".format(int("{:04b}".format(n)[::-1], base=2)).upper()
    # "{:04b}".format(n)[::-1] 将十进制的 n 按照“四位二进制数表示，不足补零” 的方式表示，并逆序。 "base = 2" 又将逆序后的二进制数转为10进制
    # {:x} 将得到的十进制数又用十六进制的字符表示出来，即使为数字，比如"5"时，upper() 也可返回“5”，字母则按照大小写转化


while True:
    try:
        a, b = input().split()
        s = list(a + b)
        s_odd = s[::2]
        s_even = s[1::2]

        s_odd.sort()
        s_even.sort()

        s[::2] = list(s_odd)
        s[1::2] = list(s_even)

        res = ""
        for i in range(len(s)):
            if s[i] in r:
                res += reverse_bits_4(int(s[i], base=16))
            else:
                res += s[i]
        print(res)
    except:
        break




