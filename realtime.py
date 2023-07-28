
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []


def animate(i, count):
    data = pd.read_csv("data.csv")
    time = data["time"][count:]
    lefteye = data["left_eye"][20:]
    righteye = data["right_eye"][20:]
    lips = data["lips"][20:]
    headh = data["head_h"][20:]
    headv = data["head_v"][20:]
    headslope = data["head_slope"][count:]
    plt.cla()

    
    #plt.plot(time, headh, color="green")
   # plt.plot(time, headv, color="red")
  #  plt.legend(["horizontal", "vertical"])

    plt.scatter(time, headslope, s=5)
    plt.xlabel("Time")
    count += 100
    print(count)
    

count = 20
ani = FuncAnimation(plt.gcf(), animate, interval=0, repeat=False, frames=500, fargs=(count,))
plt.tight_layout()
plt.show()


#%%
