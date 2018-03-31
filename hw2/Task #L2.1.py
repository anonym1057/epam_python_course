def union(list1, *args):
    list_union = list(set(list1))
    for lst in args:
        for ch in lst:
            if ch not in list_union:
                list_union += [ch]
    return list_union


def intersect(list1, *args):
    list_intersect = []
    for ch in list1:
        in_all = True
        for lst in args:
            if ch not in lst:
                in_all = False
                break
        if in_all:
            list_intersect += [ch]
    return list_intersect


lst1 = ['A', 'B', 'C', 'D', 'E']
lst2 = ['A', 'E', 'F']
lst3 = ['A', 'F', 'G']

print("Lists:", lst1, lst2, lst3)
print("Union: {}".format(union(lst1, lst2, lst3)))
print("Intersect: {}".format(intersect(lst1, lst2, lst3)))
