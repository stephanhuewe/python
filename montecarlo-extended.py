import numpy as np
import matplotlib.pyplot as plt
import time as time

total_random = int(input("\nNumber of random points for Monte Carlo estimate of Pi?\n>"))
start_time = time.time()

x_array = np.random.rand(1,total_random)
y_array = np.random.rand(1,total_random)

radius_array = np.sqrt(x_array**2 + y_array**2)

inside_circle = np.sum(radius_array < 1.0)

pi_approx = (inside_circle / total_random) * 4.0

print ("--------------")
print ("Approximate value for pi: {0:.6f}".format(pi_approx))
print ("Difference from numpy pi: {0:.6f}".format(pi_approx-np.pi))
print ("Percent Error: (approx-numpy)/numpy*100: {0:.6f}%".format((pi_approx-np.pi)/np.pi*100))
print ("Execution Time: {0:.6f} seconds".format(time.time() - start_time))
print ("--------------")

random_points_plot = plt.scatter(x_array, y_array, color='blue', s=.1)
circle_plot = plt.Circle( ( 0, 0 ), 1, color='red', linewidth=2, fill=False)

ax = plt.gca()
ax.cla()

ax.add_artist(random_points_plot)
ax.add_artist(circle_plot)

plt.show()
