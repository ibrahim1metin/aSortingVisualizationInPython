import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from sortAlgo import quickSort,bubble_sort,BogoSort
def update_plotQuickSort(data):
    for bar, val in zip(barsq, data):
        bar.set_height(val)
def update_plotBubbleSort(data):
    for bar, val in zip(barsb, data):
        bar.set_height(val)
def update_plotBogoSort(data):
    for bar, val in zip(barsbogo, data):
        bar.set_height(val)
data1 = np.random.permutation(np.arange(0,101))
data2=data1.copy()
data3=data2.copy()

fig, (ax1,ax2,ax3), = plt.subplots(3,1,figsize=(10,10))

ax1.set_title("Quicksort")
ax2.set_title("Bubblesort")
ax3.set_title("Bogosort")

ax1.set_axis_off()
ax2.set_axis_off()
ax3.set_axis_off()

barsq = ax1.bar(range(len(data1)), data1,1,color="red")
barsb=ax2.bar(range(len(data2)), data2,1)
barsbogo=ax3.bar(range(len(data3)), data3,1,color="green")

animq = FuncAnimation(fig, update_plotQuickSort, frames=quickSort(data1,0,len(data1)-1))
animb=FuncAnimation(fig, update_plotBubbleSort, frames=bubble_sort(data2))
animbogo=FuncAnimation(fig, update_plotBogoSort, frames=BogoSort(data3))

plt.show()