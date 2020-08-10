# processes-modelling

This repository contains all the codes written to model processes developped at the LIPEC.

In the file requirements.txt, all the required python packages are listed.

## Rotary Jet-Spinning


### Concept of the process

This process consists in extruding a melt polymer through the orifices of a rotating spinneret due to the centrifugal force.
The extruded polymer transforms into a fiber to be collected.



### Predict the critical rotational velocity for jet ejection


<img src="https://latex.codecogs.com/gif.latex?\Omega&space;_{th}=\sqrt{\frac{\sigma&space;}{a^{2}s_{0}\rho&space;}}" title="\Omega _{th}=\sqrt{\frac{\sigma }{a^{2}s_{0}\rho }}" />


&nbsp;


<img src="https://latex.codecogs.com/gif.latex?\Omega&space;_{th}" title="\Omega _{th}" /> : Critical rotational velocity for jet ejection (RPS)

<img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" /> : Surface tension (<img src="https://latex.codecogs.com/gif.latex?kg/s^{2}" title="kg/s^{2}" />)

a : Radius of the orifice (m)

<img src="https://latex.codecogs.com/gif.latex?s_{0}" title="s_{0}" /> : Radius of the reservoir (m)

<img src="https://latex.codecogs.com/gif.latex?\rho" title="\rho" /> : Density (<img src="https://latex.codecogs.com/gif.latex?kg&space;/&space;m^{3}" title="kg / m^{3}" />)

[Explanation of where this equation comes from](mellado_equations.md)

### Predict the final radius of the fiber

<img src="https://latex.codecogs.com/gif.latex?r=\frac{a&space;U^{1/2}&space;\nu^{1/2}&space;}{R_{c}^{3/2}\Omega&space;}" title="r=\frac{a U^{1/2} \nu^{1/2} }{R_{c}^{3/2}\Omega }" />


&nbsp;


r : Final radius of the fiber (m)

a : Radius of the orifice (m)

U : Initial axial velocity (m/s)

<img src="https://latex.codecogs.com/gif.latex?\nu" title="\nu" /> : kinematic viscosity (<img src="https://latex.codecogs.com/gif.latex?m^{2}&space;/&space;s" title="m^{2} / s" />)

Rc : Radius of the collector (m)

<img src="https://latex.codecogs.com/gif.latex?\Omega" title="\Omega" /> : Angular velocity (RPS)

[Explanation of where this equation comes from](mellado_equations.md)

Prediction of the effect of several parameters on the final radius.

The following parameters were studied : angular velocity, collector distance, orifice radius,
                                        reservoir radius, density, surface tension, viscosity.



### Predict the radius of the jet in steady state as a function of the axial coordinate x

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

**What the user have to do ?**
- Adapt the values of the polymer and machine in the file deck.yaml : 

```yaml
Polymers:
  Name: 'Polypropylene'
  Viscosity: 0.63
  Density: 900
  Surface Tension: 0.0436

Machines:
  Name: 'Super Floss Maxx'
  Orifice Radius: 0.001512
  Collector Radius: 0.3302
  Reservoir Radius: 0.06985
  Angular Velocity : 57.5

Discretisation: 20
```

The Discretisation number is the number of points on the graphics.

- Install all required python packages listed in requirements.txt: 

```linux
pip install -r requirements.txt
```

- The only file which need to be run is the main.py. This script brings together all classes.

```linux
python main.py
```


## Viscosity

### Compute the viscosity as a function of the temperature and the shear stress  

<img src="https://latex.codecogs.com/gif.latex?\eta&space;=&space;B&space;exp(\frac{E_{\tau&space;}}{RT}-b\tau&space;^{s})" title="\eta = B exp(\frac{E_{\tau }}{RT}-b\tau ^{s})" />


&nbsp;


<img src="https://latex.codecogs.com/gif.latex?\eta" title="\eta" /> : Melt viscosity (Pa.s)

<img src="https://latex.codecogs.com/gif.latex?\tau" title="\tau" /> : Shear stress

<img src="https://latex.codecogs.com/gif.latex?E_{\tau&space;}" title="E_{\tau }" /> : activation energy of viscous-elastic flow under condition of <img src="https://latex.codecogs.com/gif.latex?\tau" title="\tau" /> = constant

R : gas constant in J/(mol.K)

T : temperature of experiment in K

B, b, s : Constants of the material (in this case : s=1/2)



### How this code works ?

**Classes**
- Deck : get the value in viscosity.yaml
- Polymer : stock the values of deck concerning the polymer in variables that will be reuse
- Model : contain the equation to predict the viscosity
- Graph : calculate the data with the model, draw the graphic and save it in the folder Graphics


**What the user have to do ?**
- Adapt the values in the file viscosity.yaml :

```yaml
Polymers:
  Name: 'PP Shell'
  Constant B: 1.5
  Constant b: 0.0043
  Activation Energy: 45522

Constants:
  Gas Constant: 8.314

Discretisation: 20
```

The Discretisation number is the number of points on the graphics.

- Install all required python packages listed in requirements.txt: 

```linux
pip install -r requirements.txt
```

- The only file which need to be run is the main_viscosity.py. This script brings together all classes.

```linux
python main_viscosity.py
```
