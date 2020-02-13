import radial_distribution 
import numpy as np 
import matplotlib.pyplot as plt 

#print(radial_distribution.__doc__)


avg,r = radial_distribution.radial_distribution_one_particle_species(1000,"dump.simulation",200,12.59921049894873)



# # LATEX:
plt.rc('text', usetex=True)

fig,ax = plt.subplots()

ax.plot(r,avg,ls="-",color="black")
ax.set_ylabel(r'$g(r)$',fontsize=28)
ax.set_xlabel(r'$r$',fontsize=28)
ax.set_xlim(0,3.5)
ax.set_ylim(0,4.0)
plt.yticks(np.arange(0.,4.1, step=0.5),fontsize=22)
plt.xticks(np.arange(0., 3.51, step=0.5),fontsize=22)
ax.grid()
plt.tight_layout()

plt.show()