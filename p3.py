x = [1, 4, 4, 4, 4, 10, 15, 15, 14, 13, 12, 11]
li = []
g = []
count = 1
tempcount = 1
dis = 0
cc = 0
for k in range(len(x)):
    for i in range(len(x)):
        try:
            if x[cc + 1] - x[cc] >= 0:  # only having trouble at indexing otherwise it would work
                g.append(x[i])
                g.append(x[i + 1])
                tempcount += 1
        except(IndexError):
            pass
        cc += 1
        print g

    if tempcount > count:
        li = g
        count = tempcount
    g = []
    tempcount = 1
# if tempcount > count l = g
# g.remove everything g is just for temp listing the numbers
# if this count bigger than last one pop the entire list and add this new one instead
# try:
#     if li[len(li) - 2] == li[len(li) - 3]:
#         li.remove(len(li) - 2)
# except(IndexError):
#     pass


# for i in li:
#     if li[i] == li[i - 1]:
#         li.remove(i)

print li
print count


#NEED TO : REMOVE the number before the last number in the list, then start the remove double process
