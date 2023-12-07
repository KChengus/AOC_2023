
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
    print(x)
    return x[0]

def main():
    ret = 0
    track = [0] * 15
    s = input()
    while s:
        cards, bid = s.split(' ')
        bid = int(bid)
        handle_card_event(track, cards, bid)
        i = 1
        
        try:
            s = input()
        except:
            break
    print(m)
    for j in range(6, -1, -1):
        l = sorted(m[j], key=func)
        # print(l)
        for k in range(len(l)):
            val = (i+k) * l[k][1] 
            print(l[k][0])
            ret += val
        i += len(l)
    
    return ret

print(main())