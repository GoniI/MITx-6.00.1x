print ("Please think of a number between 0 and 100!")
print ("Is your secret number 50 ?")
print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

num = 50
while True:
    user = raw_input("")
    if user != 'h' and user != 'l' and user != 'c':
        print ("Sorry, I did not understand your input.")
        print ("Is your secret number {}".format(num))
        print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    else:
        break
gt = []
lt = []

while True:
    if user == 'l':
        if len(lt) == 0:
            gt.append(num)
            num = num + (num / 2)
        else:
            gt.append(num)
            num = (lt[len(lt) - 1] - num) / 2 + num
    if user == 'h':
        if len(gt) == 0:
            lt.append(num)
            num = num / 2
        else:
            lt.append(num)
            num = (num - gt[len(gt) - 1]) / 2 + gt[len(gt) - 1]
    if user == 'c':
        print ('Game over. Your secret number was: {}'.format(num))
        break
    if num > 100:
        x = num - 100
        num = num - x

    print ("Is your secret number {}?".format(num))
    print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while True:
        user = raw_input("")
        if user != 'h' and user != 'l' and user != 'c':
            print ("Sorry, I did not understand your input.")
        else:
            break
