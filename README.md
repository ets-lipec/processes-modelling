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

Formule

r : Final radius of the fiber (m)
a : Radius of the orifice (m)
U : Initial axial velocity (m/s)
\nu : kinematic viscosity (m^2/s)
Rc : Radius of the collector (m)
\Omega : Angular velocity (RPS)

   a. Effect of the angular velocity on the final radius

final_radius_omega.py

   b. Effect of the collector distance on the final radius

final_radius_Rc.py

   c. Effect of the orifice radius on the final radius

final_radius_a.py

   d. Effect of the reservoir radius on the final radius

final_radius(s0).py


  4. Predict the radius of the jet in steady state as a function of the axial coordinate x

Formule

\sigma : Surface tension (g/s^2)
x : Axial coordinate (m)
r_{0} : Initial radius of the jet = orifice radius a (m)
U : Initial axial velocity (m/s)
\rho : Density (kg/m^3)
\mu : Viscosity (Pa.s)
\Omega : Angular velocity (RPS)


Radius_x.py



