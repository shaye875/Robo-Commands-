from classes.guardRobot import *
from classes.deliveryRobot import *
dora = DeliveryRobot(3,4)
gedon = GuardRobot(4,5)
robots = [dora,gedon]
comands = [".SAY",".MOVE",".WHERE"]
while True:
  print("commands SAY")
  dora.SAY("im dora")
  gedon.SAY("im gedon")
  print("commands MOVE")
  dora.MOVE(8,9)
  gedon.MOVE(10, 11)
  print("commands WHERE")
  dora.WHERE()
  gedon.WHERE()
  exit = input("if you want to exit enter exit")
  if exit == "exit":
      break
