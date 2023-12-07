
m = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
}

conv = {
    '2':2, '3':3, '4':4,
    '5':5, '6':6, '7':7, 
    '8':8, '9':9, 'T':10,
    'J':11, 'Q':12, 'K':13,
    'A':14,
}

def compare(s1, s2):
    for i in range(len(s1)):
        c1, c2 = conv[s1[i]], conv[s2[i]]
        if (c1 > c2):
            return True
        elif (c1 < c2):
            return False
    return False


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and compare(arr[j][0], key[0]):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def handle_card_event(track, cards, bid):

    unique = set(cards)
    if len(unique) == 5:
        m[6].append((cards, bid))
    elif len(unique) == 4:
        m[5].append((cards, bid))
    elif len(unique) == 1:
        m[0].append((cards, bid))
    else:
        # some other
        for card in cards:
            card_val = conv[card]
            track[card_val] += 1
        if len(unique) == 2:
            # either four of a kind or fullhouse
            for card in unique:
                card_val = conv[card]
                if (track[card_val] == 4):
                    # 4 of a kind
                    m[1].append((cards,bid))
                    break
            else:
                # full house
                m[2].append((cards,bid))
        else:
            # length 3
            # other 3 of a kind or 2 pair
            for card in unique:
                card_val = conv[card]
                if (track[card_val] == 3):
                    # 3 of a kind
                    m[3].append((cards,bid))
                    break
            else:
                # 2 pair
                m[4].append((cards,bid))
        # reset track
        # print(track)
        for card in cards:
            card_val = conv[card]
            track[card_val] -= 1


def func(x):
    ret = "" 
    for i in range(len(x[0])):
        ret += str(conv[x[0][i]])
    print(x[0], ret)
    return int(ret) 

def main():
    ret = 0
    track = [0] * 15
    s = input()
    while s:
        cards, bid = s.split(' ')
        bid = int(bid)
        handle_card_event(track, cards, bid)
        
        try:
            s = input()
        except EOFError:
            break
    print(m)
    i = 1
    for j in range(6, -1, -1):
        l = m[j]
        insertion_sort(l)
        print(l)
        for k in range(len(l)):
            val = (i+k) * l[k][1] 
            # print(val)
            ret += val
        i += len(l)
    
    return ret

print(main())