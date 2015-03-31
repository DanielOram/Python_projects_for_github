__author__ = 'Administrator'



import turtle

t = turtle.Turtle()
t.color("white")
t.backward(450)
t.color("red")




def f2(length, depth):
   if depth == 0:
     t.forward(length)
   else:
     f(length/11, depth -1)
     t.left(135)
     f(length/11, depth -1)
     t.right(30)
     f(length/2, depth -1)
     t.right(15)
     f(length/11, depth -1)
     t.right(15)
     f(length/2, depth -1)
     t.right(30)
     f(length/11, depth -1)
     t.right(90)
     f(length/11, depth -1)
     t.right(30)
     f(length/11, depth -1)
     t.right(15)
     f(length/11, depth -1)
     t.right(15)
     f(length/11, depth -1)
     t.right(30)
     f(length/11, depth -1)
     #t.left(45)
     #t.forward(300)



def f(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        f(length/2, depth -1)
        t.left(60)
        f(length/2, depth -1)
        t.right(120)
        f(length/2, depth -1)

        f(length/2, depth -1)
        t.left(120)
        f(length/2, depth -1)
        t.right(60)
        f(length/2, depth -1)


def f2(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        f2(length/2, depth -1)
        t.left(135)
        f2(length/8, depth -1)
        t.right(90)
        f2(length/8, depth -1)
        t.right(90)
        f2(length/8, depth -1)
        t.right(90)
        f2(length/8, depth -1)
        t.left(135)
        f2(length/2, depth -1)


f2(100, 4)
#f2(400,4)




