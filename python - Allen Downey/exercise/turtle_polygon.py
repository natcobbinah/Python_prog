import turtle

def polygon(t,n,length):
  t.Turtle()
  t.pendown()

  # the exterior angle of an n-sided polygon is 360/n 
  for i in range(n):
      angle = 360 / n
      t.fd(length)
      t.lt(angle)
    
  t.mainloop()

polygon(turtle,5,50)


    
    
    