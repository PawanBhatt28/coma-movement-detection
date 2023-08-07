
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []


def animate(i):
    points = -250
    
    data = pd.read_csv("data.csv")
    time = data["time"][points:]
    lefteye = data["left_eye"][points:]
  #  righteye = data["right_eye"][points:]
    lips = data["lips"][points:]
    headh = data["head_h"][points:]
    headv = data["head_v"][points:]
    headslope = data["head_slope"][points:]
    sin = data["planar_angle"][points:]

 #   ax.clear()
    ax[0,0].clear()
    ax[0,0].plot(time, headslope, 'tab:orange')
    ax[0,0].set_title("Vertical + Horizontal Head")

    ax[0,1].clear()
    ax[0,1].plot(time, sin, 'tab:red')
    ax[0,1].set_title("Angular Rotation")

    ax[1,0].clear()
    ax[1,0].plot(time, headh, 'tab:green')
    ax[1,0].set_title("Head Horizontal")

    ax[1,1].clear()
    ax[1,1].plot(time, headv)
    ax[1,1].set_title("Head Vertical")

   # ax[0,0].plot(time, headslope)
 #   ax.plot(time, headh)
 #   ax.plot(time, headv)


 #   ax.scatter(time, headslope)
#    ax.legend(["horizontal", "vertical"])
    
   # ax.set_ylim([-5,20])
  #  ax.set_xlabel("Time")

fig = plt.figure()
#ax = fig.add_subplot(111)
fg, ax = plt.subplots(2,2)


ani = FuncAnimation(plt.gcf(), animate, interval=100)
plt.tight_layout()
plt.show()


#%%
