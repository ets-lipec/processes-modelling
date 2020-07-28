"""
Reference : 
Mark G. Dodin Ph.D. (1986) 
Mathematical Models of Polymer Melt Viscosity in Shearing Flow.
Polystyrene and Polypropylene Melts—2
International Journal of Polymeric Materials and Polymeric Biomaterials
1:3, 185-203,
DOI: 10.1080/00914038608078660
"""

from math import *
import numpy
import matplotlib.pyplot as plt

def viscosity_PP_PS(A, E0, a, gamma_point_power, R, Tp, T):
    """ 
    valid for Polypropylene and Polystyrene

    :Input:  
    - *A, a* : constant of the material
    - *E0* : activation energy of viscous-elastic flow under condition of gamma point = constant
    - *gamma_point_power* : shear rate to the power of 1/m with m a constant of the material
    - *R* : gas constant in J/(mol.K)
    - *Tp* : temperature limit of applicability of the equation
    - *T* : temperature of experiment (K)

    :Returns:
    Melt viscosity in shearing flow

    """
    return A*exp(((E0-a*gamma_point_power)/(R*T))*(1-T/Tp))

# PP Shell
A = 278
E0 = 43263
a = 2.662
R = 8.314
Tp = 1309
B = 1.5
E = 45522
b = 0.0043

discretisation = 20
T = [463, 483, 503, 533, 553]
color = ['ro', 'bo', 'go', 'yo', 'ko']
legend = ['463K', '483K', '503K', '533K', '553K']
T = numpy.array(T)
gamma_point_power = numpy.linspace(1, 4, discretisation)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for k in range(len(T)):
    # melt_viscosity = []
    log_melt_viscosity = []
    for i in range(discretisation):
        melt_viscosity = viscosity_PP_PS(A, E0, a, gamma_point_power[i], R, Tp, T[k])
        log_melt_viscosity.append(log10(melt_viscosity))
    log_melt_viscosity = numpy.array(log_melt_viscosity)
    axes.plot(gamma_point_power, log_melt_viscosity, color[k], label = legend[k])
    
axes.grid()
axes.set_xlabel("Shear rate to the power of 1/6", fontsize=16)
axes.set_ylabel("log ( Melt viscosity )", fontsize=16)
axes.set_title("PP Shell, m=6", fontsize=16, y=1.)

axes.legend()
plt.show()

def viscosity_all(B, E, R, T, b, shear_stress_power):
    """ 
    valid for all polymers

    :Input:  
    - *B, b* : constant of the material
    - *E* : activation energy of viscous-elastic flow under condition of shear stress = constant
    - *shear_stress_power* : shear stresse to the power of 1/2
    - *R* : gas constant in J/(mol.K)
    - *T* : temperature of experiment (K)

    :Returns:
    Melt viscosity in shearing flow

    """
    return B*exp(E/(R*T)-b*shear_stress_power)

shear_stress_power = numpy.linspace(250, 1000, discretisation)

fig2 = plt.figure()
axes2 = fig2.add_subplot(1, 1, 1)

for k in range(len(T)):
    # melt_viscosity = []
    log_melt_viscosity = []
    for i in range(discretisation):
        melt_viscosity = viscosity_all(B, E, R, T[k], b, shear_stress_power[i])
        log_melt_viscosity.append(log10(melt_viscosity))
    log_melt_viscosity = numpy.array(log_melt_viscosity)
    axes2.plot(shear_stress_power, log_melt_viscosity, color[k], label = legend[k])
    
axes2.grid()
axes2.set_xlabel("Shear stress to the power of 1/2", fontsize=16)
axes2.set_ylabel("log ( Melt viscosity )", fontsize=16)
axes2.set_title("PP Shell ", fontsize=16, y=1.)

axes2.legend()
plt.show()
