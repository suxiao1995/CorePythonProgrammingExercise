__author__ = 'lihui'
# Let computer guess a number

# Get correct number from user
while True:
    try:
        num = int(raw_input('Enter a number(1~10000): '))
    except ValueError:
        print "The input must be a number!"
        continue

    if num < 10000:
        break
    else:
        print "The number must be in 1~10000!"

guess = 5000
center = 2500
step = 0

while guess != num:
    if num > guess:
        guess += center
        print "I gusee: ", guess
    elif num < guess:
        guess -= center
        print "I gusee: ", guess
    center /= 2
    if center == 0:
        center = 1
    step += 1

print "Aha! The answer is: ", guess
print "I totally use %d steps." % step
