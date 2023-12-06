def run():
    s = input()
    # [blue, red, green]
    mp = {'red':0, 'green':1, 'blue':2}
    minimum = [0, 0, 0]
    ret = 0
    def func(st):
        # print(st)
        for cube in st.split(','):
            st_amount, st_color = cube.strip().split(' ')
            minimum[mp[st_color]] = max(int(st_amount), minimum[mp[st_color]])
    while True:
        minimum = [0,0,0]
        s_split = s.split(';')
        s_split[0] = s_split[0].split(':')[1].strip()
        # print(s_split)
        for elem in s_split:
            func(elem)
        val = 1
        print(minimum)
        for elem in minimum:
            val *= elem 
        ret += val
        print(ret)

        try:
            s = input()
        except EOFError:
            break

run()