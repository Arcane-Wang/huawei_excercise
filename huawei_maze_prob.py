# 个人思路：将问题拆分为小问题： 从左上角到格点(x,y)处的最短步长由与其相邻的四个格点决定
# 先判断周围格点没有不能走的，然后更新结果
# 为 min(f(x-1,y),f(x+1,y),f(x,y+1),f(x,y-1))+1，append()被选中的路径格点
# 建立 visit[[]]矩阵记录是否访问过该格点，初始化为-1，1代表访问过，0代表没有
# 同时建立steps[[]]矩阵记录各个格点所用的最小步数，初始化为m*n
# 直到要判断的格点坐标为(n,n)为止
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 注意以下代码只有当仅存在一种可行路径时有效，因为未对步长做限制
def targetPath(current, orig_mat, visited_mat, path):
    # if current == [m-1, n-1]:
    #     return
    global optimal_path
    for (x, y) in [(current[0]+1,current[1]), (current[0]-1,current[1]),
                  (current[0],current[1]+1), (current[0],current[1]-1)]:
        path.append((x,y))
        old_pathLen = len(path)
        if 0 <= x < m and 0 <= y < n and orig_mat[x][y] != 1 and visited_mat[x][y] != 1:
            visited_mat[x][y] = 1
            if (x, y) == (m-1, n-1):
                # print("best path found!")
                if len(path) < len(optimal_path):
                    optimal_path = path
                return
            targetPath((x, y), orig_mat, visited_mat, path)
            if old_pathLen == len(path): # 这一步的目的是当试完该格点处所有的可能后，如果路径长度并没有增加，即所有可能均不可行，故将该点的坐标也从路径中删除
                path.pop()
        else:
            path.pop() # 尝试添加一个点，不满足边界或访问矩阵或原矩阵限制时，将之前添加的该点的路径删除


while True:
    try:
        m, n = list(map(int, input().split()))
        orig_mat = [list(map(int, input().split())) for _ in range(m)]
        start_point = (0, 0)
        end_point = (m-1,n-1)
        visited_mat = [[0]*n for _ in range(m)]
        visited_mat[0][0] = 1
        steps_mat = [[m*n]*n for _ in range(m)]
        steps_mat[0][0] = 1
        path = [(0, 0)]
        optimal_path = [path]*m*n
        targetPath(start_point, orig_mat, visited_mat, path)
        [print(str(optimal_path[i]).replace(' ', '')) for i in range(len(path))]

    except:
        break
