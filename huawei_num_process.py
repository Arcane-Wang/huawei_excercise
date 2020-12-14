while True:
    try:
        I = input().strip().split()[1:]
        R = set(input().strip().split()[1:])
        R = [int(r) for r in R]
        R = sorted(R)
        out = []
        for j, r in enumerate(R):
            countnum = 0
            single_content = []
            existFlag = False
            for i, item in enumerate(I):
                if str(r) in item:
                    single_content.extend([str(i), item])
                    existFlag = True
                    countnum += 1
            if existFlag:
                out.extend([str(r), str(countnum)])
                out.extend(single_content)
        out.insert(0, str(len(out)))
        print(' '.join(out))
    except:
        break
