import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program in active
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()

    point_numbers = range(rw.num_points)

    # Emphasize the first and last points
    ax.plot(rw.x_values, rw.y_values, linewidth=3)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break