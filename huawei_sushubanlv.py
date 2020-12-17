# 先把所给的数分为奇数和偶数两部分
def split_to_odd_and_even(nums):
    even, odd = [], []
    for _, item in enumerate(nums):
        if item%2 == 0:
            even.append(item)
        else:
            odd.append(item)
    return even, odd

# 判断是否为素数
def isprime(num,primes,notprimes):
    import math
    if num in primes:
        return True
    elif num in notprimes:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                notprimes.append(num)
                return False
        return True


nums = [1,2,3,4,5,43,2]
primes, notprimes = [], []
even, odd = split_to_odd_and_even(nums)
# print(even,odd)

# 听说要用匈牙利算法，我放弃了。。。