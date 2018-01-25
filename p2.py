# problem 2
# Write a program that prints the number of times the string 'bob' occurs in s.
s = "bwqbwqbobbobobqwwoqsbob"
bobs = list(s)
count = 0
bobsc = 0
for i in bobs:
    try:
        if bobs[count] + bobs[count + 1] + bobs[count + 2] == "bob":
            bobsc += 1
    except(IndexError):
        pass
    count += 1

print ("Number of times bob occurs is: " + str(bobsc))
