from ev3dev.ev3 import *
from time import sleep

left = LargeMotor('outB')
right = LargeMotor('outC')
claw = MediumMotor('outA')
ir = InfraredSensor()
assert ir.connected, "Connect sensor"
ir.mode='IR-PROX'


def move_fwd(time):
  left.run_timed(time_sp=time, speed_sp=750)
  right.run_timed(time_sp=time, speed_sp=750)
  return

def turn_left(time):
  left.run_timed(time_sp=time, speed_sp=900)
  return

def turn_right(time):
  right.run_timed(time_sp=time, speed_sp=900)
  return

def grab(time):
  claw.run_timed(time_sp=time, speed_sp=900)
  sleep(2)
  claw.run_timed(time_sp=time, speed_sp=-900)
  return

def reverse(time):
   left.run_timed(time_sp=time, speed_sp=-750)
   right.run_timed(time_sp=time, speed_sp=-750)
   return

def grab_and_run():
   dist = ir.value()
   while dist>10:
       move_fwd(500)
       sleep(0.5)
       dist=ir.value()

   grab(900)
   sleep(1)
   reverse(3000)
   return
