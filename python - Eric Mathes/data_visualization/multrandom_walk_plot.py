import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program in active
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()

    ax.scatter(rw.x_values, rw.y_values, s = 15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break