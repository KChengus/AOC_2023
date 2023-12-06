def run():
    s = input()
    # [blue, red, green]
    maximum = {'red':12, 'green':13, 'blue':14}
    ret = 0
    game_num = 1
    
    def func(st):
        for cube in st.split(','):
            st_amount, st_color = cube.strip().split(' ')
            if (maximum[st_color] < int(st_amount)):
                return True
        return False


    while s:
        s_split = s.split(';')
        s_split[0] = s_split[0].split(':')[1].strip()
        # print(s_split)
        for elem in s_split:
            if func(elem):
                break
        else:
            ret += game_num
        game_num += 1
        try:
            s = input()
        except EOFError:
            break
    return ret

print(run())