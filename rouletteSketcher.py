class rouletteSketcher:
  def __init__(self):
    import turtle
    self.t = turtle.Turtle()

  def hypocycloid(self,r,k,color1='blue',color2='red'):
    #Big outer circle
    self.t.color(color1)
    self.t.penup()
    self.t.setpos(0,-r*k)
    self.t.pendown()
    self.t.circle(r*k)
    #Hypocycloid
    self.t.color(color2)
    self.t.penup()
    from fractions import Fraction
    factor = Fraction(k).limit_denominator().denominator
    from math import radians as radians, sin as sin, cos as cos, ceil as ceil
    for theta in range(0,360*factor+1):
      theta = radians(theta)
      x = r*(k-1)*cos(theta)+r*cos((k-1)*theta)
      y = r*(k-1)*sin(theta)-r*sin((k-1)*theta)
      self.t.setpos(x,y)
      self.t.pendown()
  
  def epicycloid(self,r,k,color1='blue',color2='red'):
    #Big inner circle
    self.t.color(color1)
    self.t.penup()
    self.t.setpos(0,-r*k)
    self.t.pendown()
    self.t.circle(r*k)
    #Epicycloid
    self.t.color(color2)
    self.t.penup()
    from fractions import Fraction
    factor = Fraction(k).limit_denominator().denominator
    from math import radians as radians, sin as sin, cos as cos
    for theta in range(0,360*factor+1):
      theta = radians(theta)
      x = r*(k+1)*cos(theta)-r*cos((k+1)*theta)
      y = r*(k+1)*sin(theta)-r*sin((k+1)*theta)
      self.t.setpos(x,y)
      self.t.pendown()
    
  def hypotrochoid(self,R,r,d,color1='blue',color2='red'):
    #Big outer circle
    self.t.color(color1)
    self.t.penup()
    self.t.setpos(0,-R)
    self.t.pendown()
    self.t.circle(R)
    #Hipotrochoid
    self.t.color(color2)
    self.t.penup()
    from fractions import Fraction
    factor = Fraction(R/r).limit_denominator().denominator
    from math import radians as radians, sin as sin, cos as cos
    for theta in range(0,360*factor+1):
      theta = radians(theta)
      x = (R-r)*cos(theta) + d*cos(((R-r)/r)*theta)
      y = (R-r)*sin(theta) - d*sin(((R-r)/r)*theta)
      self.t.setpos(x,y)
      self.t.pendown()

  def epitrochoid(self,R,r,d,color1='blue',color2='red'):
    #Big inner circle
    self.t.color(color1)
    self.t.penup()
    self.t.setpos(0,-R)
    self.t.pendown()
    self.t.circle(R)
    #Epitrochoid
    self.t.color(color2)
    self.t.penup()
    from fractions import Fraction
    factor = Fraction(R/r).limit_denominator().denominator
    from math import radians as radians, sin as sin, cos as cos
    for theta in range(0,360*factor+1):
      theta = radians(theta)
      x = (R+r)*cos(theta) - d*cos(((R+r)/r)*theta)
      y = (R+r)*sin(theta) - d*sin(((R+r)/r)*theta)
      self.t.setpos(x,y)
      self.t.pendown()
