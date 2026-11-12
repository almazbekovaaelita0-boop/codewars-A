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
