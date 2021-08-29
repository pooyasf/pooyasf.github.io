---
layout: page
title: PDE solver
description: Master's Thesis
img: /assets/img/heat.png
importance: 5
---

My master's thesis was on "Deep learning of High-Dimensional PDEs". These kind of PDEs arise in many diciplines like finance, physics, and engineering. In addition to theoretic studies on the function approximation and optimization of neural networks, we have developed a library to facilitate experiments. We have also tested several examples (Advection, Heat, American Option, and KdV) and analyzed the effect of different settings like initialization in this context. We discovered a type of numerical instability while solving KdV equation in this context. We are preparing an in-depth report for this problem. 

You can check out the code and more description for this project on my github [here](https://github.com/pooyasf/DGM){:target="_self"} <br>
Also, you can see my dissertation abstract [here](/assets/pdf/abstract.pdf){:target="_self"}

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/advection_anim.gif' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    Neural Network finding solution of Advection Equation.
</div>


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid rounded z-depth-1" src="{{ '/assets/img/heat_anim.gif' | relative_url }}" alt="" title="example image"/>
    </div>
</div>
<div class="caption">
    Neural Network finding solution of Heat Equation.
</div>
