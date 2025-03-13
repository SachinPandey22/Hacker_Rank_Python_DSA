def good_pairs(pile1, pile2, k):
    count = 0
    mp = [k * pile for pile in pile2]
    for p in range(len(pile1)):
        for q in range(len(mp)):
            if pile1[p] % mp[q] == 0:
                count += 1
    return count


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))