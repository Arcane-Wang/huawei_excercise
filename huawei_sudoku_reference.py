def check(matrix, row, col, value):
    """
    检测在(row,col)放value是否合适
    1.每行含1-9,不含重复值value
    2.每列含1-9,不含重复值value
    3.3*3区块含1-9,不含重复值value
    """
    # 检测每行
    for j in range(9):
        if matrix[row][j] == value:
            return False
    # 检测每列
    for i in range(9):
        if matrix[i][col] == value:
            return False
    # 检测元素所在3*3区域
    area_row = (row // 3) * 3
    area_col = (col // 3) * 3
    for i in range(area_row, area_row + 3):
        for j in range(area_col, area_col + 3):
            if matrix[i][j] == value:
                return False
    return True


def solveSudoku(matrix, count=0):
    """
    遍历每一个未填元素，遍历1-9替换为合适的数字
    """
    if (count == 81):  # 递归出口
        return True
    # 行优先遍历
    row = count // 9  # 行标
    col = count % 9  # 列标
    if matrix[row][col] != 0:  # 已填充
        return solveSudoku(matrix, count=count + 1)
    else:  # 未填充
        for i in range(1, 10):
            if check(matrix, row, col, i):  # 找到可能的填充数
                matrix[row][col] = i
                if solveSudoku(matrix, count=count + 1):  # 是否可完成
                    return True  # 可完成
                # 不可完成
                matrix[row][col] = 0  # 回溯
        return False  # 不可完成


while True:
    try:
        matrix = []
        for i in range(9):
            matrix.append([int(i) for i in input().split(' ')])  # 多维列表输入
        solveSudoku(matrix)
        for i in range(9):
            print(' '.join(map(str, matrix[i])))
    except:
        break