

conv = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def main():
    s = input()
    res = 0
    while True:
        # print(s)
        all_nums = []
        strings = []
        for c in s:
            print(strings)
            if c.isnumeric():
                all_nums.append(c)
                continue
            
            for i in range(len(strings)):
                strings[i] += c
            strings.append(c)

            for num in conv.keys():
                for string in strings:
                    if num.startswith(string):
                        if (string == num):
                            all_nums.append(num)
                        break

        # print(all_nums)
        val = ""
        if (len(all_nums[0]) == 1):
            val += all_nums[0]
        else:
            val += conv[all_nums[0]]
        if (len(all_nums[-1]) == 1):
            val += all_nums[-1]
        else:
            val += conv[all_nums[-1]]

        res += int(val)
        print(res)
        s = input()

main()