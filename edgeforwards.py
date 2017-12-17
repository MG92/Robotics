from ev3dev.ev3 import *
from time import sleep

class Motors():
	def __init__(self):
		self.left_motor = LargeMotor('outB')
		self.right_motor = LargeMotor('outC')
		self.tail = MediumMotor('outA')

	def drive_straight(self, run_time):
		self.left_motor.run_timed(time_sp=run_time, speed_sp=-750, stop_action='brake')
		self.right_motor.run_timed(time_sp=run_time, speed_sp=-750, stop_action='brake')
		#self.left_motor.wait_while('running')
		#self.left_motor.wait_while('running')
		return

class Sensors():
	def __init__(self):
		self.ir = InfraredSensor()
		assert self.ir.connected, "Connect an IR sensor"
		
	def measure_dist(self):
		self.ir.mode='IR-PROX'
		return self.ir.value()

ir_check = Sensors()
motors = Motors()
dist = ir_check.measure_dist()
while dist>10:
	motors.drive_straight(1000)
	dist=ir_check.measure_dist()
	print('Distance from obstacle', dist)

sleep(1)
motors.tail.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action='brake')	
