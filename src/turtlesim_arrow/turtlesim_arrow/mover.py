import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist

from turtlesim.msg import Pose

import math
import termios
import tty
import sys

import time


class Mover(Node):

    def __init__(self):
        super().__init__('mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.send_command)
        self.fd = sys.stdin.fileno()
        self.target = 0

        self.create_subscription(Pose, '/turtle1/pose', self.on_pose, 10)
        self.pose = None

        self.settings = termios.tcgetattr(sys.stdin)


    
    def getKey(self):

        tty.setcbreak(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key
    
    def on_pose(self, msg):
        self.pose = msg #so pose keps updating



    def send_command(self):
        key_pressed = self.getKey()
        twist = Twist()

        if key_pressed is not None:

            if key_pressed == 'd':

                target = 0.0
            
            elif key_pressed == 'w':

                target = math.pi / 2
            
            elif key_pressed == 'a':

                target = math.pi
            
            elif key_pressed == 's':

                target = -math.pi / 2
            
            else:
                return twist
        if self.pose is None:
            return #crashes first tick otherwise
    
        turn = target - self.pose.theta


        #make it so turtle turns then moves
        twist.angular.z = turn

        self.publisher_.publish(twist)

        time.sleep(1.0)

        twist.linear.x = 1.0
        twist.angular.z = 0.0

        self.publisher_.publish(twist)

def main():
    rclpy.init()
    mover = Mover()

    try:
        rclpy.spin(mover)
    except KeyboardInterrupt: #check for ctr + c pressed
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, mover.settings) #to revert to default settings since getKey() changes them, from github so dont understand fully tbh




