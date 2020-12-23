# 给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。
# 要求输出所有火车出站的方案，以字典序排序输出。

# 思路：建立三个列表：train_in 为给定的顺序， train_out 为输出的出站顺序， train_station 为在站内的车号
# 当train_station 和 train_in 均为空时输出对应的train_out
# 在进出站时遵循先进后出的原则
import copy


def find_out_order(t_in, t_station, t_out):
    # 此处因为之后用了 append 和 pop 这样的可以改变原列表值的函数，所以复制了两次，分别给到出站/进站的情况！！！！
    train_in1 = copy.deepcopy(t_in)
    train_in2 = copy.deepcopy(t_in)
    train_station1 = copy.deepcopy(t_station)
    train_station2 = copy.deepcopy(t_station)
    train_out = copy.deepcopy(t_out)
    # train_out2 = copy.deepcopy(t_out)
    if t_in != [] or t_station != []:
        is_train_in_empty = (t_in == [])
        is_train_station_empty = (t_station == [])
        # 决定是否出站，0为不出，1为出
        for if_out in range(2):
            if if_out == 0:
                if is_train_in_empty:
                    continue
                elif not is_train_in_empty:
                    train_station1.append(train_in1.pop(0))
                    find_out_order(train_in1, train_station1, train_out)
            elif if_out == 1:
                if is_train_station_empty:
                    continue
                elif not is_train_station_empty:
                    train_out.append(train_station2.pop())
                    find_out_order(train_in2, train_station2, train_out)
    else:
        RES_OUT.append(train_out)
    return


while True:
    try:
        n, tr_in = int(input()), list(map(int, input().strip().split()))
        # tr_in.reverse()
        tr_out, tr_station = [], []
        RES_OUT = []
        find_out_order(tr_in, tr_station, tr_out)
        RES_OUT = sorted(RES_OUT)
        for i in range(len(RES_OUT)):
            out = list(map(str, RES_OUT[i]))
            print(' '.join(out))
        #print(RES_OUT)





    except:
        break
