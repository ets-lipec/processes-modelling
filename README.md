# processes-modelling

This repository contains all the codes written to model processes developped at the LIPEC.

## Rotary Jet-Spinning



  1. Concept of the process

This process consists in extruding a melt polymer through the orifices of a rotating spinneret due to the centrifugal force.
The extruded polymer transforms into a fiber to be collected.



  2. Predict the critical rotational velocity for jet ejection


<img src="https://latex.codecogs.com/gif.latex?\Omega&space;_{th}=\sqrt{\frac{\sigma&space;}{a^{2}s_{0}\rho&space;}}" title="\Omega _{th}=\sqrt{\frac{\sigma }{a^{2}s_{0}\rho }}" />


<img src="https://latex.codecogs.com/gif.latex?\Omega&space;_{th}" title="\Omega _{th}" /> : Critical rotational velocity for jet ejection (RPS)

<img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" /> : Surface tension (kg/s^2)

a : Radius of the orifice (m)

<img src="https://latex.codecogs.com/gif.latex?s_{0}" title="s_{0}" /> : Radius of the reservoir (m)

<img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /> : Density (kg/m^3)



  3. Predict the final radius of the fiber

<img src="https://latex.codecogs.com/gif.latex?r=\frac{a&space;U^{1/2}&space;\nu^{1/2}&space;}{R_{c}^{3/2}\Omega&space;}" title="r=\frac{a U^{1/2} \nu^{1/2} }{R_{c}^{3/2}\Omega }" />


r : Final radius of the fiber (m)

a : Radius of the orifice (m)

U : Initial axial velocity (m/s)

<img src="https://latex.codecogs.com/gif.latex?\nu" title="\nu" /> : kinematic viscosity (m^2/s)

Rc : Radius of the collector (m)

<img src="https://latex.codecogs.com/gif.latex?\Omega" title="\Omega" /> : Angular velocity (RPS)


   a. Effect of the angular velocity on the final radius

final_radius_omega.py

   b. Effect of the collector distance on the final radius

final_radius_Rc.py

   c. Effect of the orifice radius on the final radius

final_radius_a.py

   d. Effect of the reservoir radius on the final radius

final_radius(s0).py



  4. Predict the radius of the jet in steady state as a function of the axial coordinate x

<img src="https://latex.codecogs.com/gif.latex?r=r_{0}&space;\sqrt{\frac{\rho&space;U&space;x}{\mu&space;-\Sigma&space;&plus;\sqrt{(\mu&space;-\Sigma&space;)^{2}&plus;(\rho&space;\Omega&space;x^{2})^{2}}}}" title="r=r_{0} \sqrt{\frac{\rho U x}{\mu -\Sigma +\sqrt{(\mu -\Sigma )^{2}+(\rho \Omega x^{2})^{2}}}}" />

<img src="https://latex.codecogs.com/gif.latex?\Sigma&space;=&space;\frac{\sigma&space;x}{r_{0}U}" title="\Sigma = \frac{\sigma x}{r_{0}U}" />

<img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" /> : Surface tension (g/s^2)

x : Axial coordinate (m)

<img src="https://latex.codecogs.com/gif.latex?r_{0}" title="r_{0}" /> : Initial radius of the jet = orifice radius a (m)

U : Initial axial velocity (m/s)

<img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /> : Density (kg/m^3)

<img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" /> : Viscosity (Pa.s)

<img src="https://latex.codecogs.com/gif.latex?\Omega" title="\Omega" /> : Angular velocity (RPS)


Radius_x.py



