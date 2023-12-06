import re
def main():

    pattern = r'[ ]+'


    time = int(re.split(pattern, input())[1])
    dist = int(re.split(pattern, input())[1])


    count = 0
    for t in range(1, time):

        race_dist = (time - t) * t
        if (race_dist > dist):
            count += 1

    return count 


print(main())

