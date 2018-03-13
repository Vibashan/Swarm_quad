#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class move_turtle():
	"""docstring for move_turtle"""
	def __init__(self):
		
		#Initialize node
		rospy.init_node('move_turtle')

		#Declare subscriber funtion to collect data of turtle pose
		#Use rostopic list command to identify the topic name
		#TODO: Fill in the parameters of the Subscriber function
		rospy.Subscriber(,self.getTurtlePose)

		#Publisher object for moving the turtle
		#TODO: Fill in the parameters of the Publisher funtion
		self.turtle_move_pub = rospy.Publisher(,,)

		#
		self.msg = Twist()
		self.pose = Pose()

		self.msg.linear.x = 0.0  
		self.msg.linear.y = 0.0
		self.msg.linear.z = 0.0
		self.msg.angular.x = 0.0
		self.msg.angular.y = 0.0
		self.msg.angular.z = 0.0

		self.linear_x = 3

		self.angular_z = 1.6

	def draw_line(self):
		self.msg.linear.x = -self.linear_x #Setting linear veloctiy in x before publishing. Rest values remain zero by default
		self.turtle_move_pub.publish(self.msg) #Publishing data to tutlesim object under topic 'turtleX/cmd_vel'

	def draw_square(self):
		
		#TODO: Draw a sqare by moving the turtle
		#To move straight, apply value to linear x
		#To rotate the turtle, apply a calculated angular z value

	def draw_star(self):

		#TODO: Draw a star pattern by moving the turtle			

	def draw_circle(self):

		i = 0
		j = 0
		
		while i < 4:
			self.msg.angular.z = self.angular_z #Setting an angular value on z so that the turtle will turn at an angle
			self.msg.linear.x = self.linear_x #Setting a linear value on x so that the turtle will move in a linear direction
			self.turtle_move_pub.publish(self.msg) #Combination of both will create a arc movement of the turtle
			rospy.sleep(1.2)
			i = i + 1
			j = j + 1
			if i == 4:
				i = 0
				self.angular_z = -self.angular_z
			if j == 80:
				j = 0
				self.linear_x = -self.linear_x
				break
		self.draw_line()

	#Subscriber function
	def getTurtlePose(self, data):
		self.pose = data #Saving turtle data in variable pose
		print(self.pose) #Printing the pose


if __name__ == '__main__':

	#Create object of class 'move_turtle()'
	move = move_turtle()
	rospy.sleep(1)

	#Call funtion draw_line()
	move.draw_line()
	rospy.sleep(1)

	#Call funtion draw_circle()
	move.draw_circle()
	rospy.sleep(1)

	#TODO: Implement a sqaure and star pattern
	move.draw_square()
	rospy.sleep(1)

	move.draw_star()
	rospy.sleep(1)

	rospy.spin()	