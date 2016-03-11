import turtle

n = raw_input("Enter the number of points:")
n = int(n)

while n < 5.0:
    n = raw_input("Nah dude has to be greater than 5")
    n = int(n)

side_len = raw_input("Enter the length of each line:")
side_len = int(side_len)

bob = turtle.Pen()
for j in range (n):
    bob.forward(side_len)
    bob.left(1800.0/n)



inp = raw_input("hit <enter> to quit")

turtle.bye()
