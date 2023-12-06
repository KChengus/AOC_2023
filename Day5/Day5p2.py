
import re
def category_map(seeds):
    ret = []
    ranges = []
    print(input())
    s = input()
    while (s):
        r = list(map(int, s.split(' ')))
        ranges.append(r)
        try:
            s = input()
        except EOFError:
            break
    
    while seeds:
        l = []
        for i in range(len(seeds)):
            start, end = seeds[i]
            if (end - start < 0):
                print("Error Detected")
            for j in range(len(ranges)):
                dest, src, r = ranges[j]
                src_end = src + r
                # All within bounds
                if (src <= start < src_end and end <= src_end):
                    ret.append([start - src + dest, end - src + dest])
                    break
                # Right out of bounds
                elif (src <= start < src_end and end > src_end):
                    ret.append([start - src + dest, dest+r])
                    l.append([src_end, end])
                    break
                # Left out of bounds
                elif (start < src and src < end <= src_end):
                    l.append([start, src])
                    ret.append([dest, end - src + dest])
                    break
                # Left and Right out of bounds
                elif (start < src and end > src_end):
                    l.append([start, src])
                    ret.append([dest, dest + r])
                    l.append([src_end, end])
                    break
            else:
                ret.append([start, end])
        # print(l)
        seeds = l

    # print(ret)
    return ret

def run():

    l = list(map(int, input().split(' ')[1:]))
    seeds = [(l[i], l[i] + l[i+1]) for i in range(0, len(l), 2)] # (start, range)

    print(len(seeds))
    input() # remove empty line
    
    # get map values
    i = 7
    while i:
        seeds = category_map(seeds)
        i -= 1
    
    print(seeds)
    return min(seeds)

print(run())
