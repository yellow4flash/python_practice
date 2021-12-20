# pregunta test
tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
# print(tup)
# pregunta test
lst=[[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print(lst[r][c])
            print("#")
# print(lst)