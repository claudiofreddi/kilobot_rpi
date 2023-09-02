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
        self.subscription = self.create_subscription(Twist,'turtle1/cmd_vel',self.cmd_to_pwm_callback,10)
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

        seconds = 0 #time.time()

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

    def motorStop(self):#Motor stops
        self.motor_right(1, self.Dir_forward,0)
        self.motor_left(1, self.Dir_forward,0)
        GPIO.output(self.Motor_Left_Pin1, GPIO.LOW)
        GPIO.output(self.Motor_Left_Pin2, GPIO.LOW)
        GPIO.output(self.Motor_Right_Pin1, GPIO.LOW)
        GPIO.output(self.Motor_Right_Pin2, GPIO.LOW)
        GPIO.output(self.Motor_Left_EN, GPIO.LOW)
        GPIO.output(self.Motor_Right_EN, GPIO.LOW)

    def motor_right(self,status, direction, speed):#Motor 2 positive and negative rotation
        if status == 0: # stop
            self.motorStop()
        else:
            if direction == self.Dir_forward:
                GPIO.output(self.Motor_Right_Pin1, GPIO.HIGH)
                GPIO.output(self.Motor_Right_Pin2, GPIO.LOW)
                self.pwm_Right.start(100)
                self.pwm_Right.ChangeDutyCycle(speed)
            elif direction == self.Dir_backward:
                GPIO.output(self.Motor_Right_Pin1, GPIO.LOW)
                GPIO.output(self.Motor_Right_Pin2, GPIO.HIGH)
                self.pwm_Right.start(0)
                self.pwm_Right.ChangeDutyCycle(speed)

    def motor_left(self,status, direction, speed):
        
        if status == 0: # stop
            self.motorStop()
        else:
            if direction == self.Dir_forward:#
                GPIO.output(self.Motor_Left_Pin1, GPIO.HIGH)
                GPIO.output(self.Motor_Left_Pin2, GPIO.LOW)
                self.pwm_Left.start(100)
                self.pwm_Left.ChangeDutyCycle(speed)
            elif direction == self.Dir_backward:
                GPIO.output(self.Motor_Left_Pin1, GPIO.LOW)
                GPIO.output(self.Motor_Left_Pin2, GPIO.HIGH)
                self.pwm_Left.start(0)
                self.pwm_Left.ChangeDutyCycle(speed)
        return direction       

    def destroy(self):
        self.motorStop()
        GPIO.cleanup() 

    def cmd_to_pwm_callback(self, msg):

        right_wheel_vel = (msg.linear.x + msg.angular.z)/2
        left_wheel_vel = (msg.linear.x - msg.angular.z)/2
        print(right_wheel_vel, " / ",left_wheel_vel )
        
        if (right_wheel_vel==0):
            self.motor_right(1, self.Dir_forward,0)

        if (right_wheel_vel>0):
            self.motor_right(1, self.Dir_forward,50)
        if (right_wheel_vel<0):
            self.motor_right(1, self.Dir_backward,50)

        if (left_wheel_vel==0):
            self.motor_left(1, self.Dir_forward,0)

        if (left_wheel_vel>0):
            self.motor_left(1, self.Dir_forward,50)
        if (left_wheel_vel<0):
            self.motor_left(1, self.Dir_backward,50)
        
        time.sleep(0.1)
        self.motorStop()

def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    velocity_subscriber.destroy_node()
    rclpy.shutdown()
    velocity_subscriber.destroy()


if __name__ == '__main__':
    main()