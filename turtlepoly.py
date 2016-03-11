import turtle

bob = turtle.Pen()

num_sides_inp = raw_input("Enter the number of sides:")
num_sides = int(num_sides_inp)

side_len_inp = raw_input("Enter the length of each side:")
side_len = int(side_len_inp)


for side in range(num_sides):
    bob.forward(side_len)
    bob.left(360.0/num_sides)

inp = raw_input("hit <enter> to quit")

turtle.bye()
