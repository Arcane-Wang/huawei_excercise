# 输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
# 本题含有多组样例输入

while True:
    try:
        line = input().strip()
        line_set = set(list(line))
        count_dic = []
        for item in line_set:
            count_dic.append({"item": item, "count": line.count(item)})
        count_dic.sort(key=lambda x: 200*x["count"]+ord('z')-ord(x["item"]), reverse=True)
        res = []
        for i, item in enumerate(count_dic):
            res.append(item["item"])
        print(''.join(res))

    except:
        break
