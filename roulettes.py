import turtle
import math as m

t = turtle.Turtle()

def hypocycloid(r,k,color1='blue',color2='red'):
  t.reset()
  t.hideturtle()
  #Big outer circle
  t.color(color1)
  t.penup()
  t.setpos(0,-r*k)
  t.pendown()
  t.circle(r*k)
  #Hypocycloid
  t.color(color2)
  t.penup()
  for theta in range(3600): #0.1° precission
    theta /= 10
    x = r*(k-1)*m.cos(theta)+r*m.cos((k-1)*theta)
    y = r*(k-1)*m.sin(theta)-r*m.sin((k-1)*theta)
    t.setpos(x,y)
    t.pendown()
    
def epicycloid(r,k,color1='blue',color2='red'):
  t.reset()
  t.hideturtle()
  #Circulo externo
  t.color(color1)
  t.penup()
  t.setpos(0,-r*k)
  t.pendown()
  t.circle(r*k)
  #Epicicloide
  t.color(color2)
  t.penup()
  for theta in range(3600):
    theta /= 10
    x = r*(k+1)*m.cos(theta)-r*m.cos((k+1)*theta)
    y = r*(k+1)*m.sin(theta)-r*m.sin((k+1)*theta)
    t.setpos(x,y)
    t.pendown()
    
def hypotrochoid(R,r,d,color1='blue',color2='red'):
  t.reset()
  t.hideturtle()
  #Circulo externo
  t.color(color1)
  t.penup()
  t.setpos(0,-R)
  t.pendown()
  t.circle(R)
  #Hipotrocoide
  t.color(color2)
  t.penup()
  for theta in range(3600):
    theta /= 10
    x = (R-r)*m.cos(theta) + d*m.cos(((R-r)/r)*theta)
    y = (R-r)*m.sin(theta) - d*m.sin(((R-r)/r)*theta)
    t.setpos(x,y)
    t.pendown()
    
def epitrochoid(R,r,d,color1='blue',color2='red'):
  t.reset()
  t.hideturtle()
  #Circulo externo
  t.color(color1)
  t.penup()
  t.setpos(0,-R)
  t.pendown()
  t.circle(R)
  #Epitrocoide
  t.color(color2)
  t.penup()
  for theta in range(3600):
    theta /= 10
    x = (R+r)*m.cos(theta) - d*m.cos(((R+r)/r)*theta)
    y = (R+r)*m.sin(theta) - d*m.sin(((R+r)/r)*theta)
    t.setpos(x,y)
    t.pendown()
    
hipocicloide(30,2)

