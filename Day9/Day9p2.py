import re

class Solution():
    def __init__(self):
        pass

    def solve(self, seq):

        flag = True
        length = len(seq)
        while flag:
            flag = False
            for i in range(1, length):
                pos = len(seq)-i
                seq[pos] = seq[pos] - seq[pos-1]
                if (seq[pos] != 0):
                    flag = True
            length -= 1
        # print(len(seq) - length)
        for i in range(len(seq) - length, 0, -1):
            seq[i-1] = seq[i-1] - seq[i]
        return seq[0]

    def handle_input(self):
        s = input()

        ret = 0
        while s:
            seq = list(map(int, s.split(' ')))
            ret += self.solve(seq)
            try:
                s = input()
            except EOFError:
                break
        return ret
        
        

    def run(self):
        return self.handle_input()

    

if __name__ == "__main__":
    sol = Solution()
    print(sol.run())