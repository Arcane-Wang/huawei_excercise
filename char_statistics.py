while True:
    try:
        line = list(input())
        num_alpha, num_space, num_num, num_else = 0, 0, 0, 0
        for _, item in enumerate(line):
            if item.isalpha():
                num_alpha += 1
            elif item.isdigit():
                num_num += 1
            elif item == ' ':
                num_space += 1
            else: num_else += 1
        print(num_alpha)
        print(num_space)
        print(num_num)
        print(num_else)
    except:
        break