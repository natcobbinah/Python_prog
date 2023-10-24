import turtle
import math

def polygon(t,n,length):
  t.Turtle()
  t.pendown()

  # the exterior angle of an n-sided polygon is 360/n 
  for i in range(n):
      angle = 360 / n
      t.fd(length)
      t.lt(angle)
    
  t.mainloop()

def circle(t,r,n):
   circumference = 2 * math.pi * r
   length = circumference / n
   polygon(t,n,length)

circle(turtle,60,60)


    
    
    