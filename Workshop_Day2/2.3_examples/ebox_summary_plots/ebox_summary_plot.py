import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import sys
import os

# get the folder from the command line
ebox_folder = sys.argv[1]
system = sys.argv[2]

try:
    os.listdir(ebox_folder)
except FileNotFoundError:
    top_folder = os.getcwd()



date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

emin, tmp, prs, dns = [None, None, None, None]
for file in filter(lambda file: file.endswith('.xvg'), os.listdir(ebox_folder)):
    if "-eng" in file:
       emin = np.loadtxt(os.path.join(ebox_folder,file))
    elif "-tmp" in file:
        tmp = np.loadtxt(os.path.join(ebox_folder,file))
    elif "-prs" in file:
        prs = np.loadtxt(os.path.join(ebox_folder,file))
    elif "-dns" in file:
        dns = np.loadtxt(os.path.join(ebox_folder,file))



fig, axs = plt.subplots(2,2, figsize=(10,5))

# Energy Minimization
try: 
    axs[0,0].plot(*emin.T)
except AttributeError:
    axs[0,0].text(0,0, "FAILED TO EXTRACT DATA")
axs[0,0].set_xlabel("time [ps]")
axs[0,0].set_ylabel("energy [kJ/mol]")

# NVT Relaxation : Temperature
try:
    axs[1,0].plot(*tmp.T, 'tab:orange')
    axlims = axs[1,0].get_xlim()
    axs[1,0].hlines(298.15, -50,np.max(tmp.T[0])  + 50, colors="k")
    axs[1,0].set_xlim(*axlims)
except AttributeError:
    axs[1,0].text(0,0, "FAILED TO EXTRACT DATA")
axs[1,0].set_xlabel("time [ps]")
axs[1,0].set_ylabel("temperature [k]")

# NPT Relaxation : Pressure
try:
    axs[0,1].plot(*prs.T, 'tab:green')
    axlims = axs[0,1].get_xlim()
    axs[0,1].hlines(1, -5,np.max(prs.T[0])  + 55, colors="k")
    axs[0,1].set_xlim(*axlims)
except AttributeError:
    axs[0,1].text(0,0, "FAILED TO EXTRACT DATA")
axs[0,1].set_xlabel("time [ps]")
axs[0,1].set_ylabel("pressure [bar]")

# NPT Relaxation: Density
try:
    axs[1,1].plot(*dns.T, 'tab:red')
except AttributeError:
    axs[1,1].text(0,0, "FAILED TO EXTRACT DATA")
axs[1,1].set_xlabel("time [ps]")
axs[1,1].set_ylabel("density [kg/m^3]")

# Subplot Titles
axs[0,0].set_title("[1] Energy Minimization: ENERGY")
axs[1,0].set_title("[2] NVT Relaxation: TEMPERATURE")
axs[0,1].set_title("[3] NPT Relaxation: PRESSURE")
axs[1,1].set_title("[3] NPT Relaxation: DENSITY")

fig.suptitle("GROMACS Box Equilibration: {}\n{}".format(system, date))
fig.tight_layout()
fig.savefig(os.path.join(ebox_folder, system + "_eq_summary_plots.png"))
