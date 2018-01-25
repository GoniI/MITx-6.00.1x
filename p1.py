# problem 1
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
s = 'alsisjsissdab'
vowels = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowels += 1
print ("Number of vowels: " + str(vowels))
