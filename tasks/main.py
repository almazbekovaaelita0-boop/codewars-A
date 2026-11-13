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



# Задача 20 

def pick_peaks(arr):
    pos = []
    peaks = []
    
    if len(arr) <= 2:
        return {"pos": pos, "peaks": peaks}
        
    peak_pos = -1
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            
            peak_pos = i
        elif arr[i] < arr[i - 1]:
            
            if peak_pos != -1:
                pos.append(peak_pos)
                peaks.append(arr[peak_pos])
                peak_pos = -1  # Reset after confirming the peak
        
        
        
    return {"pos": pos, "peaks": peaks}


print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
print(pick_peaks([1, 2, 2, 2, 1])) 



# Задача 21

def zeros(n: int) -> int:
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


print(zeros(6))   
print(zeros(12))  
print(zeros(1000)) 



 # Задача 22

 def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    
    
    
    T = '#'.join('^' + s + '$')
    n = len(T)
    P = [0] * n  
    C = 0       
    R = 0       
    
    max_len = 0
    center_index = 0
    
    for i in range(1, n - 1):
        i_mirror = 2 * C - i  
        
        if R > i:
            P[i] = min(R - i, P[i_mirror])
        else:
            P[i] = 0
            
        
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1
            
        
        if i + P[i] > R:
            C = i
            R = i + P[i]
            
        
        if P[i] > max_len:
            max_len = P[i]
            center_index = i
            
    
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

print(longest_palindrome("babad"))
print(longest_palindrome("abababa")) 
print(longest_palindrome("cbbd"))    
print(longest_palindrome("ab"))       



# Задача 23

import re

def solve_runes(runes: str) -> int:
    
    used_digits = set(re.findall(r'[0-9]', runes))
    
    
    for d in range(10):
        digit_char = str(d)
        if digit_char in used_digits:
            continue
            
        
        candidate = runes.replace('?', digit_char)
        
        
        
        
        match = re.match(r'^([+-]?[0-9]+)([\+\-\*])([+-]?[0-9]+)=([+-]?[0-9]+)$', candidate)
        if not match:
            continue
            
        s1, op, s2, s3 = match.groups()
        
        
        if has_invalid_leading_zero(s1) or has_invalid_leading_zero(s2) or has_invalid_leading_zero(s3):
            continue
            
        n1, n2, n3 = int(s1), int(s2), int(s3)
        
        
        if op == '+' and n1 + n2 == n3:
            return d
        elif op == '-' and n1 - n2 == n3:
            return d
        elif op == '*' and n1 * n2 == n3:
            return d
            
    return -1

def has_invalid_leading_zero(s: str) -> bool:
    
    if s.startswith('0') and len(s) > 1:
        return True
    if s.startswith('-0') and len(s) > 2:
        return True
    return False 

print(solve_runes("1+1=?")) 
print(solve_runes("123*45?=5?088")) 
print(solve_runes("-5?*-1=5?")) 
print(solve_runes("19--45=5?")) 
print(solve_runes("??*??=302?")) 
print(solve_runes("?*11=??")) 



# Задача 24

from itertools import combinations_with_replacement

def find_all(sum_val, count):
    
    valid_combs = [
        "".join(map(str, c)) 
        for c in combinations_with_replacement(range(1, 10), count) 
        if sum(c) == sum_val
    ]
    
    
    if not valid_combs:
        return []
    
    
    return [len(valid_combs), int(valid_combs[0]), int(valid_combs[-1])] 

print(find_all(10, 3)) 
print(find_all(27, 3)) 
print(find_all(84, 4)) 
print(find_all(35, 6)) 



# Задача 25 

def solution(string, markers):
    lines = string.split('\n')
    result_lines = []
    
    for line in lines:
        
        min_idx = len(line)
        for marker in markers:
            idx = line.find(marker)
            if idx != -1 and idx < min_idx:
                min_idx = idx
        

        result_lines.append(line[:min_idx].rstrip())
        
    return '\n'.join(result_lines) 

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])) 



# Задача 26

def who_is_winner(pieces_position_list):
    
    board = [[None for _ in range(7)] for _ in range(6)]
    col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    
    
    col_heights = [5 for _ in range(7)]
    
    def check_winner():
        
        for r in range(6):
            for c in range(4):
                p = board[r][c]
                if p and p == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                    return p
                    
        
        for r in range(3):
            for c in range(7):
                p = board[r][c]
                if p and p == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    return p
                    
        
        for r in range(3):
            for c in range(4):
                p = board[r][c]
                if p and p == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                    return p
                    
        
        for r in range(3, 6):
            for c in range(4):
                p = board[r][c]
                if p and p == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3]:
                    return p
                    
        return None

    
    for move in pieces_position_list:
        col_char, color = move.split('_')
        c = col_map[col_char]
        r = col_heights[c]
        
        board[r][c] = color
        col_heights[c] -= 1  
        
        winner = check_winner()
        if winner:
            return winner
            
    return "Draw"

mover = [
    "A_Red", "B_Yellow", "A_Red", "B_Yellow",
    "A_Red", "B_Yellow", "G_Red", "B_Yellow"
]
print(who_is_winner(moves))



# Задача 27

def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    
    time_units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    ]
    
    parts = []
    for name, duration in time_units:
        count = seconds // duration
        if count > 0:
            seconds %= duration
            
            unit_str = f"{count} {name}" + ("s" if count > 1 else "")
            parts.append(unit_str)
            
    
    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    else:
        return ", ".join(parts[:-1]) + f" and {parts[-1]}" 

print(format_duration(0))   
print(format_duration(62)) 
print(format_duration(3662)) 



 # Задача 28

 import math

class Sudoku:
    def __init__(self, board):
        self.board = board

    def is_valid(self):
        if not self.board:
            return False
        
        N = len(self.board)
        
        
        for row in self.board:
            if not isinstance(row, list) or len(row) != N:
                return False
                
        
        root = int(math.isqrt(N))
        if root * root != N:
            return False
            
        expected_set = set(range(1, N + 1))
        
        
        for i in range(N):
            row = self.board[i]
            col = [self.board[r][i] for r in range(N)]
            
            if set(row) != expected_set or set(col) != expected_set:
                return False
                
        
        for sr in range(root):
            for sc in range(root):
                subgrid = []
                for r in range(root):
                    for c in range(root):
                        subgrid.append(self.board[sr * root + r][sc * root + c])
                        
                if set(subgrid) != expected_set:
                    return False
                    
        return True 

good_sudoku = Sudoku([,
 ,                    
 ,                     
                      
,                      
 ,                    
 ,                     
                  
,                  
 ,                 
   [1, 9, 5, 2, 8, 7, 6, 3, 4]                   
])    

print(good_sudoku.is_valid())



# Задача 29 

def high_and_low(numbers):
    
    nums = [int(x) for x in numbers.split()]
    
    
    return f"{max(nums)} {min(nums)}" 

print(high_and_low("1 2 3 4 5"))     
print(high_and_low("1 2 -3 4 5"))    
print(high_and_low("1 9 3 4 -5"))



 # Задача 30

 def make_negative(num):
    
    return -num if num > 0 else num


print(make_negative(1))   
print(make_negative(-5))  
print(make_negative(0))   



# Задача 31 

def xo(s):
    
    s = s.lower()
    return s.count('x') == s.count('o') 

print(xo("ooxx"))    
print(xo("xooxx"))    
print(xo("ooxXm"))    
print(xo("zpzpzpp")) 
print(xo("zzoo"))     



# Задача 32 

def get_sum(a, b):
    
    low = min(a, b)
    high = max(a, b)
    
    
    return sum(range(low, high + 1)) 

print(get_sum(1, 0))   
print(get_sum(1, 2))   
print(get_sum(0, 1))   
print(get_sum(1, 1))   
print(get_sum(-1, 0))   
print(get_sum(-1, 2))  



# Задача 33 

def filter_list(l):
    return [x for x in l if isinstance(x, int)] 


print("Привет, мир!")
print(42)
print("Имя:", "Анна", "Возраст:", 25)
name = "Алексей"
print(name)
