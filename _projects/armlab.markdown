---
layout: page
title: ARM LAB 
description: Advanced robotic and mechatronic reseach lab.
img: /assets/img/sos-logo.jpg
importance: 1
---

I was head of EE team at SOS robotic group that is working in the mechanical department of the Isfahan University of Technology, and its primary focus is on rescue robots. Our team consists of 9 people, and we have two robots including one ground vehicle and one Quad-rotor. Our ground vehicle is designed based on a mechanism consists of five main parts that provide three different configurations. These five elements are four independent moving” crawler arms and one body. In software, we mostly focus on SLAM algorithms and robot AI engine. Our goal is to develop a robot with a reliable and robust system with hope to success in helping humans in real disaster sites.
An operator controls the robot via a teleportation process, so the control operation is not entirely autonomous right now. We are developing the control method to make it fully independent. 

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/sos-1.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/sos-5.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/sos-7.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/sos-e-2.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

There is a PC inside the robot that processes images, the output of sensors, controls the actuators and runs the SLAM algorithm. As shown in the diagram, the process outputs and control feedbacks are sent to the operator station via a wireless connection, and the operator observes them is a GUI and operates the robot using a joystick and keyboard. 


For our robot , i designed and constructed a simple thermal camera by TPA81 infra-red thermal sensor. TPA81 is a thermopile array detecting infra-red in the 2um-22um range. It has an array of eight thermopiles arranged in a row so that it can measure the temperature of 8 adjacent points simultaneously. Through attaching this sensor to the top of a servo motor, we can create a thermal image and have a simple thermal camera. 
Then, the output image, visualized by RVIZ with regards to ambient temperature: 


<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/c-thermal-2.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/c-thermal-1.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    In the above image, you can see a thermal image of my friend , opening his arms in front of the camera. 
</div>


Connection between the robot and operator station is based on the following diagrams: 

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/sos-d2.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    Architucture.
</div>




<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/sos-6.jpg' | relative_url }}" alt="" title="Team members"/>
    </div>
</div>
<div class="caption">
    Team members. I am the left one! :D .
</div>
