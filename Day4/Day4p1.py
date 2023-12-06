
import re
def run():

    s = input()
    pattern = r'[ ]+'
    ret = 0
    while s:
        winning, mine = s.split(' | ')
        winning = list(map(int, re.split(pattern, winning.strip())[2:]))
        mine = list(map(int, re.split(pattern, mine.strip())))
        
        val = -1
        for num in mine:
            if num in winning:
                val += 1
        if val >= 0:
            ret += 2 ** val

        try:
            s = input()
        except EOFError:
            break
    return ret

print(run())