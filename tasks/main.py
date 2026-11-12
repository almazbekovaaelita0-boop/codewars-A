# Задача 1

def get_middle(s):
    index = len(s) // 2
    if len(s) % 2 == 0:
        return s[index - 1 : index + 1]
    else:
        return s[index]

print(get_middle("test"))    
print(get_middle("testing"))
 