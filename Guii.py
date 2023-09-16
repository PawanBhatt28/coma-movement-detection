from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np
import tkinter.messagebox


root = Tk()
root.wm_title("Embedding in TK")
'''
plt.rcParams["figure.figsize"] = [13, 11]
plt.rcParams["figure.autolayout"] = True
plt.axes()

fig = plt.Figure(dpi=100)
ax = fig.subplots(2,2)
'''
'''
fig2 = plt.Figure(dpi=100)
ax2 = fig2.add_subplot()

fig3 = plt.figure(dpi=100)
ax3 = fig3.add_subplot()

fig4 = plt.figure(dpi=100)
ax4 = fig4.add_subplot()
'''
#line, = ax.plot([], [], lw=2)
'''
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=BOTTOM, expand=1)


canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.draw()
canvas2.get_tk_widget().grid(row=0, column=1)

canvas3 = FigureCanvasTkAgg(fig3, master=root)
canvas3.draw()
canvas3.get_tk_widget().grid(row=1, column=0)

canvas4 = FigureCanvasTkAgg(fig4, master=root)
canvas4.draw()
canvas4.get_tk_widget().grid(row=1, column=1)
'''
#toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
#toolbar.update()

#canvas.mpl_connect("key_press_event", lambda event:print(f"you pressed {event.key}"))
#canvas.mpl_connect("key_press_event", key_press_handler)

#button = Button(master=root, text="Quit", command=root.quit)
#button.pack(side=tkinter.BOTTOM)

#toolbar.pack(side=BOTTOM, fill=tkinter.X)
def message():
    messagebox.showinfo("Hello Bithces")
B1 = Button(root,height=100,width=100,text="aaainnn", command=message)
B1.pack(side=TOP)

def init():
    line.set_data([],[])
    return line,

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
    ax[1,0].plot(time, headh, 'tab:green')
    ax[1,0].set_title("Head horizontal")

    ax[1,1].clear()
    ax[1,1].plot(time, headv)
    ax[1,1].set_title("Head Vertical")

    
   # line.set_data(time, headv)
  #  return line,

anim = FuncAnimation(fig, animate,   frames=200, interval=20)

tkinter.mainloop()







# def plot():
#
#     def func():
#         points = -250
#
#         data = pd.read_csv("data.csv")
#         time = data["time"][points:]
#         lefteye = data["left_eye"][points:]
#         #  righteye = data["right_eye"][points:]
#         lips = data["lips"][points:]
#         headh = data["head_h"][points:]
#         headv = data["head_v"][points:]
#         headslope = data["head_slope"][points:]
#         sin = data["planar_angle"][points:]
#         abs_mov = data["abs_mov"][points:]
#         lip_sum = data["lip_sum"][points:]
#         lip_ratio = data["lip_ratio"][points:]
#
#         plot1.plot(time, headv)
#         canvas.draw()
#
#     fig = Figure(figsize=(15, 45), dpi=100)
#     plot1 = fig.add_subplot(111)
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.get_tk_widget().pack()
#     toolbar = NavigationToolbar2Tk(canvas, root)
#     toolbar.update()
#     canvas.get_tk_widget().pack()
#
#     ani = FuncAnimation(fig, func, interval=10)
#
#
#
# root = Tk()
#
# root.title("Patient Charts")
# root.geometry("1900x1200")
#
# plot_button = Button(master=root, command=plot, height=2, width=10, text="PLOT", bg="black", fg="white")
# plot_button.pack()
#
# root.mainloop()
#
# #%%

#%%
