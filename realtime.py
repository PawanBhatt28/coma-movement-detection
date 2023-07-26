
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []


def animate(i):
    data = pd.read_csv("data.csv")
    x = data["time"][20:]
    y1 = data["left_eye"][20:]
    y2 = data["right_eye"][20:]
    y3 = data["lips"][20:]
    y4 = data["head_h"][20:]
    y5 = data["head_v"][20:]
    y6 = data["head_slope"][20:]
    plt.cla()

#plt.subplot()
  #  plt.plot(x, y4)
 #   plt.plot(x, y5)

#    plt.subplot()
#    plt.scatter(x, y6, s=10)

    plt.plot(x, y1)
    plt.legend(["eye ratio"])
  #  plt.legend(["head total", "head slope"])
    plt.xlabel("Time")
    
    

ani = FuncAnimation(plt.gcf(), animate, interval=0.01)
plt.show()


#%%
