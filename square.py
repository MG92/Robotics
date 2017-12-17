from ev3dev.ev3 import *
from time import sleep

class Motors():
    def __init__(self):
        self.left_motor = LargeMotor('outB')
        self.right_motor = LargeMotor('outC')
        self.time_log = 0
        self.tail = MediumMotor('outA')

    def drive_straight(self, run_time):
        self.left_motor.run_timed(time_sp=run_time, speed_sp=-750)
        self.right_motor.run_timed(time_sp=run_time, speed_sp=-750)
        self.time_log +=run_time
        #sleep(1)
        #print('motor speed left: %d, right: %d'%(self.left_motor.speed,
        #                                        self.right_motor.speed))
        print('total time:',self.time_log)
        sleep(1)

    def left_turn(self, run_time):
        self.left_motor.run_to_rel_pos(position_sp=120, speed_sp=-900, stop_action="hold")
        #sleep(1)
        #print('motor speed left: %d: %d'%(self.left_motor.speed))
        self.time_log+=run_time
        print('total time:',self.time_log)
        sleep(1)

    def right_turn(self, run_time):
        self.right_motor.run_timed(time_sp=run_time, speed_sp=-750)
        #sleep(1)
        #print('motor speed right: %d: %d'%(self.right_motor.speed))
        self.time_log+=run_time
        print('total time:',self.time_log)
        sleep(1)

    def square(self):
        self.drive_straight(500)
        self.left_turn(1000)
        self.drive_straight(500)
        self.left_turn(1000)
        self.drive_straight(500)
        self.left_turn(1000)
        self.drive_straight(500)
        self.left_turn(1000)
	#celebrate once we arrive at our dest
        self.tail.run_timed(time_sp=1000, speed_sp=750, stop_action='brake')
        self.tail.wait_while('running')

motor = Motors()
motor.square()
