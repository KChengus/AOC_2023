import re

translate = {
    'L':0,
    'R':1
}

class Solution():
    def __init__(self):
        self.move = "" 
        self._map = dict()

    def handle_input(self):
        pattern = r"[ =(),]+"
        self.move = input()
        input()
        s = input()

        while s:
            splitted = re.split(pattern, s)
            self._map[splitted[0]] = (splitted[1], splitted[2])
            try:
                s = input()

            except EOFError:
                break

    def run(self):
        self.handle_input()
        cur = "AAA"
        goal = "ZZZ"
        i = 0
        count = 0
        while (cur != goal):
            mv = self.move[i]
            cur = self._map[cur][translate[mv]]
            i = (i+1) % len(self.move)
            count += 1
        return count

    

if __name__ == "__main__":
    sol = Solution()
    print(sol.run())