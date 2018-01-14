from ev3dev.ev3 import *
from time import sleep

class Motors():
	def __init__(self):
		self.left_motor = LargeMotor('outB')
		self.right_motor = LargeMotor('outC')
		self.neck = MediumMotor('outA')

	def drive_straight(self, run_time):
		#N.B 1000ms at 900deg/s -> 23cm
		self.left_motor.run_timed(time_sp=run_time, speed_sp=-900, stop_action='brake')
		self.right_motor.run_timed(time_sp=run_time, speed_sp=-900, stop_action='brake')
		return

	def turn_left(self, run_time):
		#1400ms at 900deg/s -> 90deg turn
		self.left_motor.run_timed(time_sp=run_time, speed_sp=-900, stop_action='brake')
		return

	def turn_right(self, run_time):
		self.right_motor.run_timed(time_sp=run_time, speed_sp=-900, stop_action='brake')
		return

class Sensors():
	def __init__(self):
		self.ir = InfraredSensor()
		self.cl = ColorSensor()
		self.ts = TouchSensor()
		assert self.ir.connected, "Connect an IR sensor"
		assert self.cl.connected, "Connect a colour sensor"
		assert self.ts.connected, "Connect a touch sensor"		

	def measure_dist(self):
		self.ir.mode='IR-PROX'
		return self.ir.value()

	def colour_test(self):
		self.cl.mode='RGB-RAW'
		red= self.cl.value(0)
		green = self.cl.value(1)
		blue=self.cl.value(2)
		return red, green, blue


#Initialise motors and sensors 
motors = Motors()
sensors = Sensors()

r,g,b = sensors.colour_test()
print("Red: %i, green: %i, blue: %i"%(r,g,b))
sleep(0.5)
while not sensors.ts.value():
	#dist = sensors.measure_dist()
	#print('Nearest obstacle is %i cm away'%dist)
	#if dist > 20:
	motors.drive_straight(430)
	sleep(0.5)
	motors.turn_right(700)
	sleep(0.5)
	motors.drive_straight(215)
	sleep(0.5)
	motors.turn_left(1400) #1000ms
	sleep(0.5)
	motors.drive_straight(430)
	sleep(0.5)
	motors.turn_left(1400)
	sleep(0.5)
	motors.drive_straight(1000)
	sleep(0.5)
	r,g,b = sensors.color_test()
	print("Red:%i, green:%i, blue:%i"%(r,g,b))
	break
