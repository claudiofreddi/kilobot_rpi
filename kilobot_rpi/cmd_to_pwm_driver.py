# ROS
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 

#RPI
import RPi.GPIO as GPIO
import time

class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(Twist,'cmd_vel',self.cmd_to_pwm_callback,10)
        self.subscription  # prevent unused variable warning

        self.Motor_Left_EN    = 25
        self.Motor_Right_EN    = 4 
        self.Motor_Left_Pin1  = 23 
        self.Motor_Left_Pin2  = 24 
        self.Motor_Right_Pin1  = 14 
        self.Motor_Right_Pin2  = 15 

        self.Dir_forward   = 0
        self.Dir_backward  = 1

        self.pwm_Left = 0
        self.pwm_Right = 0

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Motor_Left_EN, GPIO.OUT)
        GPIO.setup(self.Motor_Right_EN, GPIO.OUT)
        GPIO.setup(self.Motor_Left_Pin1, GPIO.OUT)
        GPIO.setup(self.Motor_Left_Pin2, GPIO.OUT)
        GPIO.setup(self.Motor_Right_Pin1, GPIO.OUT)
        GPIO.setup(self.Motor_Right_Pin2, GPIO.OUT)
        try:
            self.pwm_Left = GPIO.PWM(self.Motor_Left_EN, 1000)
            self.pwm_Right = GPIO.PWM(self.Motor_Right_EN, 1000)
        except:
            pass

    
    def cmd_to_pwm_callback(self, msg):
        right_wheel_vel = (msg.linear.x + msg.angular.z)/2
        left_wheel_vel = (msg.linear.x - msg.angular.z)/2
        print(right_wheel_vel, " / ",left_wheel_vel )

def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()