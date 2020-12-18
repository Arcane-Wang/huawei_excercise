while True:
    try:
        #输入一个ip地址，转换为整数
        line = input().strip().split('.')
        line_bins = ["{:08b}".format(int(item)) for item in line]
        print(int(''.join(line_bins), base=2))
        #输入一个长整数，转换为ip地址
        line2 = input().strip()
        line2_bins = str("{:032b}".format(int(line2)))
        line2_bins_splited = [str(int(line2_bins[i:i+8], base=2))+'.' for i in range(0, 32, 8)]
        line2_bins_splited[-1] = line2_bins_splited[-1].removesuffix('.')
        print(''.join(line2_bins_splited))
    except:
        break