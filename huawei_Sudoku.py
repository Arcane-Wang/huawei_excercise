# 问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，并且满足每一行、每一列、每一个粗线宫内的数字均含1-9，并且不重复。
# 输入：
# 包含已知数字的9X9盘面数组[空缺位以数字0表示]
# 输出：
# 完整的9X9盘面数组
#
# 个人思路： 每次检查每行每列，尝试将只缺一个数的行或列补全，可以递归调用
# 对于行列有多个空缺的情况，将可能的值依次尝试，最后一起递归，直到所有要求都满足为止

import copy


def check_valid(mat):
    for i in range(9):
        if set(mat[i]) == NUMS2:
            continue
        else:
            return False
    mat_T = transpose_mat(mat)
    for j in range(9):
        if set(mat_T[j]) == NUMS2:
            continue
        else:
            return False
    return True


def find_indices(line):
    res = []
    for i, item in enumerate(line):
        if item == 0:
            res.append(i)
    return res


def filling_sudoku(mat, mat_copy):
    l = len(mat)
    find_flag = False
    for i in range(l):

        if 0 not in mat[i]:
            pass
        elif mat[i].count(0) == 1:
            mat[i][mat[i].index(0)] = list(NUMS - set(mat[i]))[0]
        else:
            mat_copy = copy.deepcopy(mat)
            possible_nums = list(NUMS - set(mat[i]))
            locations = find_indices(mat[i])
            for j, item in enumerate(locations):
                mat[i][locations[0]] = possible_nums[j]
                # print("Row Num: ", i, " location: ", locations[0])
                if filling_sudoku(mat, mat_copy):
                    return True
                else:
                    mat = copy.deepcopy(mat_copy)

    if check_valid(mat):
        for i in range(9):
            line = ' '.join(list(map(str, mat[i])))
            print(line)
        exit()
        return True
    else:
        return False


NUMS = set(list(range(10)))
NUMS2 = set(list(range(1, 10)))
matrix = [list(map(int, input().split())) for _ in range(9)]
matrix_copy = copy.deepcopy(matrix)
res = filling_sudoku(matrix, matrix_copy)
print(matrix)
