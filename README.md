How I am approaching/approached this project:

I started by downlaoding Ubuntu on my personal desktop as I recently wiped my machine to remove useless clutter. 

My next step was learning how to setup ROS2 and also learning what exactly TurtleSim is. Honestly, the sources provided weren't enough help so I employed the help of some good old fashioned youtube tutorials and many google searches. 

Once I got a rough idea of what TurtleSim is, I ran the built in turtle_telop_key node to get an idea of what type of movements I would want to recreate. I also tried to look inside the node to get an idea of how to recreate something similar, but realised that it had been downloaded in machine code. I guess the purpose is so the program downloads faster.

After I reviewed these basics, I made a simple turtlesim program in python that moves right when the program runs. The reason for this is because I wanted a solid understanding of basic essentials I needed if I wanted to make a running program. 

Takeaways from simple turtlesim program:
    My first thing I learned is when creating the package, I needed to specify the build type as ament-python. I needed to do this because I wanted 
    to write the program in python, and without specifying build type, it defaults to C++. 

    After i created the package, I learned I would need to import two packages into package.xml. I would need to import rclpy and geometry.msgs. 
    From my understanding, rclpy allows my python program to be converted into a node, and geometry_msgs will give me access to a type Twist which 
    I will be using to send messages down the line.

    Now I actually make the program. First, I made a file caled move.py in the folder with same name as package, and learned i would need to import 
    certain things. First thing would be rclpy. The reason I need to import this is so I can use rclpy.spin to keep node continuously running. I 
    also needed to import Node from rclpy so i could actually make a node. I needed to import Twist from geometry_msgs.msg as well so I could send 
    the messages in Twist. 

    Now, I made the class called Move(Node) and had it extend Node. I learned basic structure of constructor. That is, first a call to super to 
    intialize the node. Next, I had to instantiate a variable which would be responsible for publishing messages to topic. The variable published 
    messages in Twist to the topic '/turtle1/cmd_vel'. There is also a 3rd parameter, honestly I'm still a bit confused on the purpose, I think 
    it's supposed to be the maximum backlog of messages that can be posted to the topic, but I'm not sure. I just put 10 since I saw people put 
    that online.  After, i needed to instantiate another variable using create_timer (imported from Node i believe) to perform a function I will 
    later define every sepcified duration. 

    Next, I wrote a simple function (same function in create_timer) that moves the turtle right in a straight line. i learned i need to use .linear.
    x to make the turtle move left and right, and .linear.z to make the turtle turn. I also learned I needed to intalize a new variable and assign 
    to Twist(). So, all my function did was twist = Twist() -- twist.linear.x = 1 -- self.publisher_.publish(twist) with publisher_ simply being 
    the variable i assigned in the constructor. 

    Lastly, I made a main which initalized rclpy, made a new move object, and used .spin to run contiuouly.

    One oversight, I also needed to register the program in setup.py, and specify to run main.

    All of this brings me to the present, which is specifying the design plan.



Design Plan:

    So, my plan is to write this program in Python. The resaon is simply because I'm not as comfortable with C++ as I'm with Python. I also know how to read input from arrow keys in python (live problems below will explain change to WASD from arrow keys).

    I will make a simple program that takes inputs from arrow keys. Left arrow will move the turtle left, up arrow will move turtle up, right arrow will move turtle right, and down arrow will move turtle down.

    My plan on implementing this will be to check consistently if a key is being pressed, if it is then it will more up, down, left, or right, if it isn't then it will continue on path it is already following. I plan on making the turtle move in different directions by setting the z somehow than incrementing the x every lets say 0.5 seconds.


Live Problems:

    Ran into first problem. I've now realised that I will need to subsicribe to pose topic in order to get self.pose.theta which will give me direction turtle currently facing so I can turn accordingly when arrow key pressed. Bit annoying since I now need to learn more documentation at 4am, but whatever.

    I definetly do not know how to read input from arrow keys like I thought. Apparently there is a bunch of more stuff than I thought I need to import and a lot more documentation to review. So, I'm going to call it a night and resume tommorow.

    Ok, it was the 27th last I worked on this, now I'm going to finish it up. I was following implementation of arrow input from this random post on reddit, but it wasn't even complete. Also, can't find updated material on arrow input that's not Google AI, so I'm going to pivot and use WASD instead. I'm using tutorial below.

    https://www.youtube.com/watch?v=8Dksx6X_1f8


    Can't use import keyboard, so this doesn't work, instead I'm going to follow code for actual telop_twist_keyboard implementation in python using public repository below

    https://github.com/ros2/teleop_twist_keyboard

    






    