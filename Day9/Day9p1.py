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
                seq[i-1] = seq[i] - seq[i-1]
                if (seq[i-1] != 0):
                    flag = True
            length -= 1
        # print(len(seq) - length)
        for i in range(length, len(seq)):
            seq[i] = seq[i] + seq[i - 1]
        return seq[-1]

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