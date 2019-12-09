import random
import matplotlib.pyplot as plt

def inOut(xC, yC):
    result = xC ** 2 + yC ** 2
    if result <= 1.0:
        inside = True
    else:
        inside = False
    return inside

def main():

    total_random = int(input("\nHow many random points?\n>"))

    numberIn = 0
    i = 0

    while i < total_random:

        i = i + 1
        x = random.random() # Random number between 0.0 and 1.0
        y = random.random()

        print('Calculating point: ' + str(i))

        if inOut(x,y):
            numberIn = numberIn +1
            random_points_plot = plt.scatter(x, y, color='red', s=.1)
        else:
            random_points_plot = plt.scatter(x, y, color='green', s=.1)

        # Draw points
        ax = plt.gca()
        ax.add_artist(random_points_plot)

    pi_approx = (numberIn / total_random) * 4.0

    print ("--------------")
    print ("Approximate value for pi: {0:.6f}".format(pi_approx))
    print ("--------------")

    # Draw circle
    circle_plot = plt.Circle( ( 0, 0 ), 1, color='red', linewidth=2, fill=False)
    ax.add_artist(circle_plot)

    # Show image
    plt.show()

main()
