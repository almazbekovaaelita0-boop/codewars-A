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



    # Задача 9

    def good_vs_evil(good_input, evil_input):
    # Worth values for each race
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]
    
    # Convert input strings into lists of integers
    good_counts = list(map(int, good_input.split()))
    evil_counts = list(map(int, evil_input.split()))
    
    # Calculate total worth for each side using zip and sum
    total_good = sum(g * w for g, w in zip(good_counts, good_worth))
    total_evil = sum(e * w for e, w in zip(evil_counts, evil_worth))
    
    # Compare totals and return the appropriate result
    if total_good > total_evil:
        return "Battle Result: Good triumphs over Evil"
    elif total_evil > total_good:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1')) 
print(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))
print(good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))



    # Задача 10 

    def count(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

print(count("aba")) 



# Задача 11 

def delete_nth(order, max_e):
    counts = {}
    result = []
    
    for num in order:
    
        current_count = counts.get(num, 0)
        
        if current_count < max_e:
            result.append(num)
            counts[num] = current_count + 1
            
    return result 

print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3,], 2))



# Задача 12

def int32_to_ip(int32):
    return f"{(int32 >> 24) & 255}.{(int32 >> 16) & 255}.{(int32 >> 8) & 255}.{int32 & 255}" 

print(int32_to_ip(2149583361))
print(int32_to_ip(32))
print(int32_to_ip(0))



# Задача 13 

regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9]{6,}$" 

print(re.fullmatch(regex, "fjd3IR9")) 
print(re.fullmatch(regex, "fjd3IR9")) 
print(bool(re.fullmatch(regex, "fjd3IR9"))) 



# Задача 14 

def perimeter(n):
    
    a, b = 1, 1
    total_sum = 0
    
    for _ in range(n + 1):
        total_sum += a
        a, b = b, a + b
        
    return 4 * total_sum 

print(perimeter(5)) 



# Задача 15 

def fibonacci(n):
    
    cache = {0: 0, 1: 1}
    
    def fib_memo(x):
        if x in cache:
            return cache[x]
        
        cache[x] = fib_memo(x - 1) + fib_memo(x - 2)
        return cache[x]
        
    return fib_memo(n) 

print(fibonacci(10)) 



# Задача 16 

def rot13(message):
    result = []
    for char in message:
        if 'a' <= char <= 'z':
            
            shifted = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            
            shifted = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(shifted)
        else:
            
            result.append(char)
            
    return ''.join(result)

print(rot13("Hello, World!"))



# Задача 17 

def simple_assembler(program):
    registers = {}
    pc = 0  
    
    def resolve(val):
        """Helper to get the value of a constant or a register."""
        try:
            return int(val)
        except ValueError:
            return registers.get(val, 0)
            
    while pc < len(program):
        parts = program[pc].split()
        cmd = parts[0]
        
        if cmd == 'mov':
            reg, val = parts[1], parts[2]
            registers[reg] = resolve(val)
            pc += 1
        elif cmd == 'inc':
            reg = parts[1]
            registers[reg] += 1
            pc += 1
        elif cmd == 'dec':
            reg = parts[1]
            registers[reg] -= 1
            pc += 1
        elif cmd == 'jnz':
            x, y = parts[1], parts[2]
            if resolve(x) != 0:
                pc += resolve(y)  
            else:
                pc += 1
                
    return registers 

code = ["mov a 5", "inc a", "dec a", "dec a", "jnz a -1", "inc a"]
print(simple_assembler(code))

<<<<<<< HEAD


# Задача 18

def productFib(prod: int) -> list:
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    
    return [a, b, a * b == prod] 

print(productFib(714))
print(productFib(800))



# Задача 19

class SnakesLadders:
    def __init__(self):
        self.player1_pos = 0
        self.player2_pos = 0
        self.current_turn = 1  
        self.game_over = False
        
        
        self.ladders = {
            2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84,
            36: 44, 51: 67, 71: 91, 78: 98, 87: 94
        }
        self.snakes = {
            16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53,
            89: 68, 92: 88, 95: 75, 99: 80
        }

    def play(self, die1: int, die2: int) -> str:
        
        if self.game_over:
            return "Game over!"
        
        player = self.current_turn
        total_steps = die1 + die2
        
        
        if player == 1:
            self.player1_pos += total_steps
            pos = self.player1_pos
        else:
            self.player2_pos += total_steps
            pos = self.player2_pos
            
        
        if pos > 100:
            pos = 100 - (pos - 100)
            
        
        if pos in self.ladders:
            pos = self.ladders[pos]
        elif pos in self.snakes:
            pos = self.snakes[pos]
            
        
        if player == 1:
            self.player1_pos = pos
        else:
            self.player2_pos = pos
            
        
        if pos == 100:
            self.game_over = True
            return f"Player {player} Wins!"
            
        
        is_double = (die1 == die2)
        if not is_double:
            self.current_turn = 2 if self.current_turn == 1 else 1
            
        return f"Player {player} is on square {pos}" 

game = SnakesLadders()
print(game.play(1, 1))
print(game.play(1, 5))
print(game.play(6, 2))
print(game.play(1, 1))  


