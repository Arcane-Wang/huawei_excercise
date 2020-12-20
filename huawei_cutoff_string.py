while True:
    try:
        string = input().strip()
        l = int(input().strip())
        print(string[:l])
    except:
        break
