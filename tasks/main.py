# Задача 1

def get_middle(s):
    index = len(s) // 2
    if len(s) % 2 == 0:
        return s[index - 1 : index + 1]
    else:
        return s[index]

print(get_middle("test"))    
print(get_middle("testing"))



# Задача 2 

def solution(number):
    if number < 0:
        return 0
    target = number - 1
    
    def sum_to(k):
        n = target // k
        return k * n * (n + 1) // 2
    return sum_to(3) + sum_to(5) - sum_to(15)

print(solution(10))



# Задача 3

def solution(number):

    if number < 0:

        return 0

    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(solution(10))


# Задача 4

def stray(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

print(stray([1, 2, 1]))



# Задача 5

def descending_order(num):
    return int("".join(sorted(str(num) , reverse=True)))

print(descending_order(42145))



# Задача 6

def wave(people):
    result = []
    for i, char in enumerate(people):
        if char != " ":
            wave_step = people[:i] + char .upper() + people[i + 1:]
            result.append(wave_step)
    return result 

print(wave("hello"))



# Задача 7

def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}" 

print(make_readable(3665))



# Задача 8

import ipaddress

def is_valid_IP(strng):
    try:
        ipaddress.IPv4Address(strng)
        return True
    except ValueError:
        return False 

    print(is_valid_IP("192.168.1.1"))
    print(is_valid_IP("256.100.50.25"))
    print(is_valid_IP("12.34.56"))
    print(is_valid_IP("123.045.067.089")) 
    