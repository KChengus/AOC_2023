
import re
import math
def main():

    pattern = r'[ ]+'


    times = list(map(int, re.split(pattern, input())[1:]))
    dists = list(map(int, re.split(pattern, input())[1:]))
    print(times, dists)

    ret = 1
    length = len(times)
    for i in range(length):
        time = times[i]
        dist = dists[i]
        count = 0
        for t in range(1, time):
            race_dist = (time - t) * t
            if (race_dist > dist):
                count += 1
        ret *= count
    return ret

print(main())