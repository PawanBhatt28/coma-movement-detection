
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
    ax[0,1].plot(time, lip_sum, 'tab:pink')
    ax[0,1].set_title("Lip sum")


    ax[1,0].clear()
    ax[1,0].plot(time, headv, 'tab:green')
    ax[1,0].set_title("head vertical")

    ax[1,1].clear()
    ax[1,1].plot(time, lefteye)
    ax[1,1].set_title("eye")
    
'''
    ax[0,1].clear()
    ax[0,1].plot(time, headh, 'tab:red')
    ax[0,1].set_title("Lhorizontal head")

    
    ax[1,0].clear()
    ax[1,0].plot(time, lip_ratio, 'tab:blue')
    ax[1,0].set_title("Lip ratio")
'''






   # ax[0,0].plot(time, headslope)
 #   ax.plot(time, headh)
 #   ax.plot(time, headv)


 #   ax.scatter(time, headslope)
#    ax.legend(["horizontal", "vertical"])
    
   # ax.set_ylim([-5,20])
  #  ax.set_xlabel("Time")


#ax = fig.add_subplot(111)
#fg, ax = plt.subplots(2,2)
fg, ax = plt.subplots(2,2)

ani = FuncAnimation(plt.gcf(), animate, interval=10)
plt.tight_layout()
plt.show()


#%%
