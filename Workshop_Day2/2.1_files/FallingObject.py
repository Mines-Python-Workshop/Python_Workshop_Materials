import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes

plt.ioff()

class FallingObject():
   
    def __init__(self, dataframe):

        self.dataframe = dataframe

        self.time = dataframe['time[s]']
        self.position = dataframe['position[m]']

        self.velocity = self.get_velocity(self.position)
        self.acceleration = self.get_acceleration(self.velocity)

    def get_velocity(self, position):
        return np.gradient(position, self.time)
    
    def get_acceleration(self, velocity):
        return np.gradient(velocity, self.time)

    def plot_position(self, show=False, save=False, filename="position_plot.png"):

        fig, ax = plt.subplots()
        ax.plot(self.time, self.position)
        ax.set_xlabel("time[s]"); ax.set_ylabel("position[m]")
        ax.set_title("Position v. Time")

        if show == True:
            fig.show(block=True)
        if save == True:
            fig.savefig(filename)
        
        return fig, ax

    def plot_position(self, show=False, save=False, filename="position_plot.png"):

        fig, ax = plt.subplots()
        ax.plot(self.time, self.position)
        ax.set_xlabel("time[s]"); ax.set_ylabel("position[m]")
        ax.set_title("Position v. Time")

        if show == True:
            fig.show()
        if save == True:
            fig.savefig(filename)
        
        return fig, ax

    def plot_velocity(self, show=False, save=False, filename="velocity_plot.png"):

        fig, ax = plt.subplots()
        ax.plot(self.time, self.velocity)
        ax.set_xlabel("time[s]"); ax.set_ylabel("velocity[m/s]")
        ax.set_title("Velocity v. Time")

        if show == True:
            fig.show()
        if save == True:
            fig.savefig(filename)
        
        return fig, ax

    def plot_acceleration(self, show=False, save=False, filename="acceleration_plot.png"):
        
        fig, ax = plt.subplots()
        ax.plot(self.time, self.acceleration)
        ax.set_xlabel("time[s]"); ax.set_ylabel("acceleration[m/s$^2$]")
        ax.set_title("Acceleration v. Time")

        if show == True:
            fig.show()
        if save == True:
            fig.savefig(filename)
        
        return fig, ax

    def plot_all(self):
        # adapted from this tutorial:
        # https://matplotlib.org/3.4.3/gallery/axisartist/demo_parasite_axes.html

        fig = plt.figure()

        host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
        par1 = ParasiteAxes(host, sharex=host)
        par2 = ParasiteAxes(host, sharex=host)
        host.parasites.append(par1)
        host.parasites.append(par2)

        host.axis["right"].set_visible(False)

        par1.axis["right"].set_visible(True)
        par1.axis["right"].major_ticklabels.set_visible(True)
        par1.axis["right"].label.set_visible(True)

        par2.axis["right2"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

        p1, = host.plot(self.time, self.position, label="Position")
        p2, = par1.plot(self.time, self.velocity, label="Velocity")
        p3, = par2.plot(self.time, self.acceleration, label="Acceleration")

        host.set_xlabel("time[s]")
        host.set_ylabel("position [m]")
        par1.set_ylabel("velocity [m/s]")
        par2.set_ylabel("acceleration [m/s$^2$]")

        host.legend()

        host.axis["left"].label.set_color(p1.get_color())
        par1.axis["right"].label.set_color(p2.get_color())
        par2.axis["right2"].label.set_color(p3.get_color())
    
        return None

if __name__ == "__main__":
    pass