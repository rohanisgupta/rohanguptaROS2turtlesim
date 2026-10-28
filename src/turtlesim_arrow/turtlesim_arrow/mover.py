import rclpy

from rclpy.Node import Node
from geometry.msgs.msg import Twist

from turtlesim.msg import Pose

import math



Mover(Node):

    def __inti__(self):
        super():__inti__('mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel')
        self.timer = self.create_timer(0.5, self.send_command)

        self.create_subscription(Pose, '/turtle1/pose', self.on_pose, 10)


    #simple function that when called will return arrow key if arrow key is pressed
    def check_for_key(self):
      ready, _, _ = select.select([self.fd], [], [], 0)   
        if ready:

            return ARROWS.get(os.read(self.fd, 3))           
        return None

    def send_command(self):
        key_pressed = self.check_for_key()
        twist = Twist()

        if key_pressed not None:

            if key_pressed == 'right':

                target = 0.0
            
            if key_pressed == 'up':

                target = Math.PI / 2
            
            if key_pressed == 'left':

                target = Math.PI
            
            if key_pressed == 'down'

                target == -Math.PI / 2
            
            else:
                return twist
    
        turn = target - self.pose.theta

        twist.angular.z = turn

        twist.linear.z = 1

        self.publisher_.publish(twist)

def main():
    rclpy.init()
    mover = Arrowmover()
    rclpy.spin(mover)




