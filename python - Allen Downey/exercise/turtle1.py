import turtle

def square(bob,t,length):
  bob =  t.Turtle()
  bob.pendown()

  for i in range(4):
      bob.fd(length)
      bob.lt(90)
    
  t.mainloop()

square("bob",turtle,200)


    
    