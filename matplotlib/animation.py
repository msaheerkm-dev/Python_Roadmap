import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.animation as animation
fig, ax = plt.subplots()
x = np.arange(0,2*np.pi,0.1)
line, = ax.plot(x, np.sin(x))
def update(frame):
    line.set_ydata(np.sin(x + frame/10.0))
    return line,
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
