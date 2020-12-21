# 查找和排序
#
# 题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
# 都按先录入排列在前的规则处理。
#
# 例示：
# jack      70
# peter     96
# Tom       70
# smith     67
#
# 从高到低  成绩
# peter     96
# jack      70
# Tom       70
# smith     67
#
# 从低到高
#
# smith     67
#
# jack      70
#
# Tom       70
# peter     96
#
# 注：0代表从高到低，1代表从低到高


while True:
    try:
        n, way, data = int(input()), int(input()), []
        for i in range(n):
            line = input().split()
            data.append({"name": line[0], "score": int(line[1])})
        data.sort(key=lambda x: x["score"], reverse=False if way == 1 else True)
        for i in range(len(data)):
            print(data[i]["name"], data[i]["score"])

    except:
        break