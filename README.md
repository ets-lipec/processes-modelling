# processes-modelling

This repository contains all the codes written to model processes developped at the LIPEC.

In the file requirements.txt, all the required python packages are listed.

## Rotary Jet-Spinning


### Concept of the process

The rotary jet-spinning, or centrifugal spinning, process is a fiber production technology where a polymer melt or solution is extruded through the orifices of a high speed rotating spinneret. The centrifugal force imparted by the spinneret provide the mechanical driving force for extrusion of the fibers. The fibers can then be collected to form a non-woven mat.

This code is designed to model this extrusion process and compute interesting parameters, such as the final fiber diameter and the critical jet ejection velocity, and the influence of processing variables.

It is based on the work of Mellado & al., 2011 [mellado_simple_2011].

**Predict the critical rotational velocity for jet ejection**

<img src="https://latex.codecogs.com/gif.latex?\Omega&space;_{th}=\sqrt{\frac{\sigma&space;}{a^{2}s_{0}\rho&space;}}" title="\Omega _{th}=\sqrt{\frac{\sigma }{a^{2}s_{0}\rho }}" />

&nbsp;

Spinneret parameters:

<img src="https://latex.codecogs.com/gif.latex?\Omega&space;_{th}" title="\Omega _{th}" /> : Critical rotational velocity for jet ejection (RPS)

<img src="https://latex.codecogs.com/gif.latex?s_{0}" title="s_{0}" /> : Radius of the reservoir (m)

Polymer properties:

<img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" /> : Surface tension (<img src="https://latex.codecogs.com/gif.latex?kg/s^{2}" title="kg/s^{2}" />)

a : Radius of the orifice (m)

<img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /> : Density (<img src="https://latex.codecogs.com/gif.latex?kg&space;/&space;m^{3}" title="kg / m^{3}" />)

[Details of the derivations here.](mellado_equations.md)

**Predict the final radius of the fiber**

<img src="https://latex.codecogs.com/gif.latex?r=\frac{a&space;U^{1/2}&space;\nu^{1/2}&space;}{R_{c}^{3/2}\Omega&space;}" title="r=\frac{a U^{1/2} \nu^{1/2} }{R_{c}^{3/2}\Omega }" />


&nbsp;


r : Final radius of the fiber (m)

a : Radius of the orifice (m)

U : Initial axial velocity (m/s)

<img src="https://latex.codecogs.com/gif.latex?\nu" title="\nu" /> : kinematic viscosity of the polymer (<img src="https://latex.codecogs.com/gif.latex?m^{2}&space;/&space;s" title="m^{2} / s" />)

Rc : Radius of the collector (m)

<img src="https://latex.codecogs.com/gif.latex?\Omega" title="\Omega" /> : Angular velocity (RPS)

[Details of the derivations here.](mellado_equations.md)


**Predict the radius of the jet in steady state as a function of the axial coordinate x**

<img src="https://latex.codecogs.com/gif.latex?r=r_{0}&space;\sqrt{\frac{\rho&space;U&space;x}{\mu&space;-\Sigma&space;&plus;\sqrt{(\mu&space;-\Sigma&space;)^{2}&plus;(\rho&space;\Omega&space;x^{2})^{2}}}}" title="r=r_{0} \sqrt{\frac{\rho U x}{\mu -\Sigma +\sqrt{(\mu -\Sigma )^{2}+(\rho \Omega x^{2})^{2}}}}" />

<img src="https://latex.codecogs.com/gif.latex?\Sigma&space;=\frac{\sigma&space;x}{r_{0}&space;U}" title="\Sigma =\frac{\sigma x}{r_{0} U}" />


&nbsp;


<img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" /> : Surface tension (<img src="https://latex.codecogs.com/gif.latex?kg/s^{2}" title="kg/s^{2}" />)

x : Axial coordinate (m)

<img src="https://latex.codecogs.com/gif.latex?r_{0}" title="r_{0}" /> : Initial radius of the jet = orifice radius a (m)

U : Initial axial velocity (m/s)

<img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /> : Density (<img src="https://latex.codecogs.com/gif.latex?kg&space;/&space;m^{3}" title="kg / m^{3}" />)

<img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" /> : Viscosity (Pa.s)

<img src="https://latex.codecogs.com/gif.latex?\Omega" title="\Omega" /> : Angular velocity (RPS)


### How this code works ?

**Classes**
- Deck : get the value in deck.yaml
- Polymer : stock the values of deck concerning the polymer in variables that will be reuse
- RJSMachine : stock the values of deck concerning the machine in variables that will be reuse
- RJSModel : contain all equations
- Data : compute the datas for which we want to draw graphics
- Organization : organize the previous data in order to draw graphics
- PointGraph : draw the graphic with the organized data and save it in the folder Graphics


## How to run this code ?

- Install all required python packages listed in requirements.txt :
```linux
pip install -r requirements.txt
```
- Run the code for the default example (Superfloss Max cotton candy machine) :
```linux
python main.py
```

- The only file which need to be run is the main.py. This script brings together all classes.
- The code outputs graphics of the fiber radius as a function of different parameters of interest. The effect of the following parameters is computed: angular velocity, collector distance, orifice radius, reservoir radius, density, surface tension, viscosity.

**How to adapt the computations ?**

The deck.yaml file contains all the necessary inputs for the code, you can modify them to adapt the computation to your own setup.
- The range of each input parameter is define by its Minimum and Maximum values.
- The *Discretisation number* will define the interval discretization and the number of points in the graphs.
- All values need to be set in SI units.

- Adapt the values directly in the file deck.yaml before running main.py:

```yaml
Polymers:
  Name: 'Polypropylene'
  Viscosity: 0.63
  Density: 900
  Surface Tension: 0.0436

Range Polymer Parameters:
  Minimum Viscosity: 0.1
  Maximum Viscosity: 1.0
  Minimum Density: 900
  Maximum Density: 1500
  Minimum Surface Tension: 0.02
  Maximum Surface Tension: 0.06

Machines:
  Name: 'Super Floss Maxx'
  Orifice Radius: 0.001512
  Collector Radius: 0.3302
  Reservoir Radius: 0.06985
  Angular Velocity : 57.5

Range Machine Parameters:
  Minimum Orifice Radius: 0.0001
  Maximum Orifice Radius: 0.001
  Minimum Collector Radius: 0.1
  Maximum Collector Radius: 0.5
  Minimum Reservoir Radius: 0.01
  Maximum Reservoir Radius: 0.1
  Minimum Angular Velocity: 30
  Maximum Angular Velocity: 600

Graphic features:
  Discretisation: 20
```
