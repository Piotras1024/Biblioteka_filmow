class Car:

   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

       # Variables
       self.current_speed = 0

   def accelerate(self, step=10):
       self.current_speed += step

   def decelerate(self, step=10):
       self.current_speed -= step


a=Car(make="dasdsa",model_name="dassda",top_speed=200,color="dsa")

print(a.current_speed)
a.accelerate()
print(a.current_speed)