s = 'gvrmyrtxhtknpb'
count = 0
maxc = 0
lenx = 0
for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        count += 1
    else:
        count = 0
    if maxc < count:
        maxc = count
        lenx = i + 1


start = lenx - maxc
print("Longest substring in alphabetical order is: " + s[start:lenx + 1])
