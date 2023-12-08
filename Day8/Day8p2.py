import re
from math import gcd
translate = {
    'L':0,
    'R':1
}

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm(numbers):
    lcm_value = numbers[0]
    for i in range(1, len(numbers)):
        lcm_value = lcm(lcm_value, numbers[i])
    return lcm_value

class Solution():
    def __init__(self):
        self.move = "" 
        self.cur = []
        self._map = dict()

    def handle_input(self):
        pattern = r"[ =(),]+"
        self.move = input()
        input()
        s = input()

        while s:
            splitted = re.split(pattern, s)
            self._map[splitted[0]] = (splitted[1], splitted[2])
            if (splitted[0][-1] == "A"):
                self.cur.append(splitted[0])
            try:
                s = input()

            except EOFError:
                break


    def run(self):
        self.handle_input()
        print(self._map)
        print(self.cur)
        i = 0
        count = 0
        flag = True
        visited = dict()
        fin = [0] * len(self.cur)
        while flag:
            flag = False
            mv = self.move[i]
            for j in range(len(self.cur)):
                self.cur[j] = self._map[self.cur[j]][translate[mv]]
                if (self.cur[j][-1] != 'Z'):
                    flag = True
                else:
                    if (self.cur[j] in visited and visited[self.cur[j]][0] == i):
                        fin[j] = count - visited[self.cur[j]][1] 
                    visited[self.cur[j]] = (i, count)
            for val in fin:
                if val == 0:
                    break
            else:
                break
            i = (i+1) % len(self.move)
            count += 1
        
        res = find_lcm(fin)

        return res

    

if __name__ == "__main__":
    sol = Solution()
    print(sol.run())