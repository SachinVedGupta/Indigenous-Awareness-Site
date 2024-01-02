#Site with animated image of leaf to represent indigenous people and spread awareness

import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor('orange')
t.speed(0)

'''Above: Setting things up.'''

def intro():
  t.penup()
  t.goto(0, 305)
  t.pendown()
  t.color('white')
  t.write('www.indigenousreconcilliation.com', font=('times new roman', 20), align='center')
  t.hideturtle()

  t.penup()
  t.goto(0, -45)
  t.pendown()
  t.color('white')
  t.write('THE EAGLE FEATHER', font=('times new roman', 25), align='center')
  t.hideturtle()


  t.penup()
  t.goto(0, -75)
  t.pendown()
  t.color('white')
  t.write('Please transfer your attention to the console.', font=('times new roman', 8), align='center')
  t.hideturtle()

  return ' '


'''Above: The function will make the turtle write the introduction text.'''

def eag():
  t.penup()
  t.goto(0, 0)
  t.pendown()
  width_one = 2
  degrees_one = 0
  degrees_two = 0
  degrees_three = 0
  zigzagdegree = 170
  twozigzagdegree = 170
  one_forward = 10
  two_forward = 50
  degrees_four = 0
  width_two = 2

  t.pencolor('white')
  t.width(2)
  t.lt(90)
 
#Above: Defining variables and setting things up for the function.

  for i in range(34):
    t.fd(8)
    t.rt(degrees_one)
    degrees_one = degrees_one + 0.05
    width_one = width_one + 0.06
    t.width(width_one)
  t.width(1.5)

#Above: First white stem.

  t.penup()
  t.goto(41.8108307287, 270.675839304)
  t.rt(62.27)
  t.lt(31.27)
  t.pendown()
  t.width(3)

#Above: Going to the start spot for the feathers.

  t.rt(50)
  t.fd(10)

  for i in range(20):
    #if i >=5:
     # t.width(widdy)
      #widdy = widdy + 1

    if i >= 0 and i <=14:
      t.pencolor('black')
      t.rt(170)
      t.fd(one_forward)
      t.lt(zigzagdegree)
      zigzagdegree = zigzagdegree + 0.055
      t.fd(one_forward)
      one_forward = one_forward + 2
      t.pencolor('white')

    else:
      t.pencolor('white')
      t.rt(170)
      t.fd(one_forward)
      t.lt(zigzagdegree)
      zigzagdegree = zigzagdegree + 0.055
      t.fd(one_forward)
      one_forward = one_forward + 2

  t.rt(9)
  for i in range(25):
    t.rt(170)
    t.fd(two_forward)
    t.lt(twozigzagdegree)
    twozigzagdegree = twozigzagdegree + 0.02
    t.fd(two_forward)
    two_forward = two_forward - 1.5

#Above: Making the feathers and the black top it has.

  t.pencolor(244, 240, 219)
  t.lt(11.28)  
  t.penup()
  t.goto(0, 0) 
  t.pendown()
  t.width(2)
  t.lt(90)

  for i in range(34):
    t.fd(8)
    t.rt(degrees_four)
    degrees_four = degrees_four + 0.05
    width_two = width_two + 0.06
    t.width(width_two)

#Above: Making the stem which goes on top of the feather and is coloured offwhite or beige.

  t.penup()
  t.fd(100)
  t.pendown()

  return ' '

#Above: Moves the turtle out of the way for better viewing of the eagle feather.

(intro())
(eag())

print("THE EAGLE FEATHER\n")
print("The eagle and therefore the eagle’s feather symbolizes the indigenous people of Canada, though mainly is a symbol for the First Nations. In first nation culture they recognize the eagle as being the bravest, highest, and strongest bird. As well, the eagle’s feather is believed to be the link between the people and the creator (he can fly up to the creator and can dive down to the people). The eagle feather is also used in religious practices with the eagle feather being worn by those awarded with the privilege to wear it. Together, the eagle’s feather is highly appraised by the First Nations which is why receiving it (from a selected few elders) is such a sought after honour.\n")
print("Fun Fact: The middle vane of the eagle’s feather represents the path you take in your life, with each barb/fiber there representing the choices you make and that they can change the direction of your life’s path.\n")
print("The eagle’s feather represents the truth of what indiginous people stand for. It is contributing and helping with indigenous reconciliation in Canada. For example, many courts in Canada are including the option to have an eagle’s feather thus, incorporating more of the indigenous traditions into the system in Canada. In a way the eagle’s feather is a small thing but that represents and means so much. Therefore, many places can have an eagle’s feather which will lead to more awareness of the past treatment of the indigenous people, which can lead to even bigger steps in reconciliation with the indigenous people in Canada.\n\n")
print("From the creators of this page: Sachin Gupta - We hope this page has helped in educating you on indigenous truth and reconciliation in Canada. Please take action in helping with this issue at hand and even do something as small as sharing this page with a friend to help raise awareness.\n")

'''Above: Calls the feather and text to be drawn by the turtle.'''
'''Above: Prints the eagle feather story to the console.'''

#This the the repl.it which is found with the following link: https://replit.com/join/cqwwigbtqc-sachin9 
#Please click on the repl.it link above because the code doesn't work (on my) IDLE for
#some reason but it does work in the python turtle repl.it
#Thanks, from Sachin Gupta.
 
#Assignment is: The land acknowledgment assignment.
#Date is: July 22, 2021.
#MAde by: Sachin Gupta.
