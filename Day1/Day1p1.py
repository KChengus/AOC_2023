# DAY 1 PART 1

def main():
    s = input()
    res = 0
    while True:
        left = 0
        right = len(s)-1

        while (not s[left].isnumeric()):
            left += 1
        
        while (not s[right].isnumeric()):
            right -= 1

        res += int(s[left] + s[right]) 
        print(res)
        try:
            s = input()
        except EOFError:
            break

main()
