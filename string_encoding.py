while True:
    try:
        key = list(input().strip().upper())
        word = list(input().strip())
        key_processed = list()
        for i in range(len(key)):
            if key[i] not in key_processed:
                key_processed.append(key[i])
        alpha_list = [chr(ord('A')+i) for i in range(26)]
        alpha_list_remain = list(sorted(set(alpha_list)-set(key_processed)))
        key_processed.extend(alpha_list_remain)
        for i, item in enumerate(word):
            if item.isupper():
                word[i] = key_processed[ord(item)-ord('A')]
            elif item.islower():
                word[i] = key_processed[ord(item)-ord('a')].lower()
        print(''.join(word))

    except:
        break