import re

class Solution():
    def __init__(self):
        self.grid = []
    def solve(self):
        pass

    def handle_input(self):
        s = input()

        while s:
            self.grid.append(list(s))
            try:
                s = input()

            except EOFError:
                break
            
    def expand(self):
        l = []
        self.print_grid()

        # cols
        for j in range(len(self.grid[0])):
            for i in range(len(self.grid)):
                if self.grid[i][j] != '.':
                    break
            else:
                l.append(j)

        for i in range(len(self.grid)):

            for index in l[::-1]:
                self.grid[i].insert(index, '.')

        # rows
        l = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] != '.':
                    break
            else:
                l.append(i)
        for index in l[::-1]:
            self.grid.insert(index, self.grid[index])

        self.print_grid()


    def run(self):
        self.handle_input()
        self.expand()
        self.solve()

    
    def print_grid(self):
        print()
        for r in self.grid:
            print("".join(r))
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.run())