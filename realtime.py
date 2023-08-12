
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
    abs_mov = data["abs_mov"][points:]
    lip_sum = data["lip_sum"][points:]
    lip_ratio = data["lip_ratio"][points:]

    ax[0,0].clear()
    ax[0,0].plot(time, abs_mov, 'tab:orange')
    ax[0,0].set_title("Absolute Movement")

    ax[0,1].clear()
    ax[0,1].plot(time, lefteye, 'tab:red')
    ax[0,1].set_title("Left Eye")

    ax[1,0].clear()
    ax[1,0].plot(time, lip_sum, 'tab:green')
    ax[1,0].set_title("Lips Sum")

    ax[1,1].clear()
    ax[1,1].plot(time, lip_ratio)
    ax[1,1].set_title("Lips Ratio")

   # ax[0,0].plot(time, headslope)
 #   ax.plot(time, headh)
 #   ax.plot(time, headv)


 #   ax.scatter(time, headslope)
#    ax.legend(["horizontal", "vertical"])
    
   # ax.set_ylim([-5,20])
  #  ax.set_xlabel("Time")


#ax = fig.add_subplot(111)
fg, ax = plt.subplots(2,2)

ani = FuncAnimation(plt.gcf(), animate, interval=10)
plt.tight_layout()
plt.show()


#%%
