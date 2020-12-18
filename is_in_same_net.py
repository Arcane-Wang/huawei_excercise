# 基本判断
def is_vaild(s):
    list0 = list(map(int, s.split(".")))
    if len(list0) != 4:
        return False
    elif list0[0] == 0:
        return False
    else:
        for i in list0:
            if i < 0 or i > 255:
                return False
        return True


def isLegalMaskCode(Mask):
    if not Mask:
        return False
    if not is_vaild(Mask):
        return False
    binaryMask = "".join(map(lambda x: bin(int(x))[2:].zfill(8), Mask.split(".")))
    indexOfFirstZero = binaryMask.find("0")
    indexOfLastOne = binaryMask.rfind("1")
    if indexOfLastOne > indexOfFirstZero:
        return False
    return True


def subnet(ip, mask):
    ip_list = ip.split('.')
    mask_list = mask.split('.')

    s_ip = s_mask = ''
    for i in ip_list:
        tmp = bin(int(i))[2:].zfill(8)
        s_ip += tmp
    for i in mask_list:
        tmp = bin(int(i))[2:].zfill(8)
        s_mask += tmp
    res = ''
    for i in range(32):
        tmp = int(s_ip[i]) & int(s_mask[i])
        res += str(tmp)
    subnet_list = [str(int(res[x * 8:(x + 1) * 8], 2)) for x in range(4)]
    return '.'.join(subnet_list)


if __name__ == '__main__':
    while 1:
        try:
            mask = input().strip()
            ip1 = input().strip()
            ip2 = input().strip()
            if isLegalMaskCode(mask) and is_vaild(ip1) and is_vaild(ip2):
                if subnet(ip1, mask) == subnet(ip2, mask):
                    print(0)
                else:
                    print(2)
            else:
                print(1)
        except:
            break