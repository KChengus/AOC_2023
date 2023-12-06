import re
def run():

    s = input()
    pattern = r'[ ]+'
    length = 300
    points = [1] * length
    i = 0 
    while s:
        winning, mine = s.split(' | ')
        winning = list(map(int, re.split(pattern, winning.strip())[2:]))
        mine = list(map(int, re.split(pattern, mine.strip())))
        
        val = 1
        for num in mine:
            if num in winning:
                points[i + val] += points[i]
                val += 1

        i += 1
        s = input()
    return sum(points[:203]) 

print(run())