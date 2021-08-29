---
layout: page
title: ARM LAB 
description: Advanced robotic and mechatronic reseach lab.
img: /assets/img/sos-logo.jpg
importance: 1
---

I was head of the Electronics team at SOS robotic group that was working in the mechanical department of the Isfahan University of Technology, and its primary focus was on rescue robots. Our team consists of 9 people, and we had two robots including one ground vehicle and one Quad-rotor. Our ground vehicle was designed based on a mechanism consists of five main parts that provide three different configurations. These five elements are four independent moving crawler arms and one body. Our goal is to develop a robot with a reliable and robust system with the hope of success in helping humans in real disaster sites. An operator controls the robot via a teleportation process, so the control operation is not entirely autonomous right now. We are developing the control method to make it fully independent.

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
    Several pictures of the robot and the lab.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/sos-e-2.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    The concept
</div>

There is a PC inside the robot that processes images, the output of sensors, controls the actuators and runs the SLAM algorithm. As shown in the diagram, the process outputs and control feedbacks are sent to the operator station via a wireless connection, and the operator observes them is a GUI and operates the robot using a joystick and keyboard. 


I designed and built a thermal camera for our robot using a TPA81 infrared thermal sensor. The TPA81 is an array of thermopiles that detects infrared in the 2um-22um range. The thermopiles are placed within rows so that they can measure the temperature of 8 adjacent points simultaneously. By attaching this sensor to the top of a servo motor, we can create a thermal image and create a simple thermal camera. 

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/c-thermal-2.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/c-thermal-1.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    In the above image, you can see a thermal image of my friend, opening his arms in front of the camera. 
</div>

<br>
The following diagrams illustrate the connection between the robot and operator station: 
<br>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/sos-d2.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    The architucture
</div>




<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/sos-6.jpg' | relative_url }}" alt="" title="Team members"/>
    </div>
</div>
<div class="caption">
    Team members. I am the left one! :D .
</div>
