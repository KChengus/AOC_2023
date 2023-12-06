
def category_map(seeds):
    ranges = []
    input()
    s = input()
    while (s):
        r = list(map(int, s.split(' ')))
        ranges.append(r)
        try:
            s = input()
        except EOFError:
            break

    for i in range(len(seeds)):
        seed = seeds[i]
        for j in range(len(ranges)):
            dest, src, r = ranges[j]
            if (r+src > seed >= src):
                seeds[i] = seed - src + dest
                break

                

def run():

    seeds = list(map(int, input().split(' ')[1:]))
    input() # remove empty line
    
    # get map values
    i = 7
    while i:
        category_map(seeds)
        i -= 1
    return min(seeds)

print(run())