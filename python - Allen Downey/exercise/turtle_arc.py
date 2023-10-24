import turtle
import math

def polygon(t,n,length,angleVal):
  t.Turtle()
  t.pendown()

  # the exterior angle of an n-sided polygon is 360/n 
  for i in range(n):
      angle = angleVal / n
      t.fd(length)
      t.lt(angle)
    
  t.mainloop()

def circle(t,r,n,angleVal):
   circumference = 2 * math.pi * r
   length = circumference / n
   polygon(t,n,length,angleVal)
  
def arc(t,r,n,angle):
  circle(t,r,n,angle)

arc(turtle,60,60,180)

    
    
    