import time
import matplotlib.pyplot as plt

p_red = lambda x, y: 0.5 * (x / (x + y) + (side_count - x) / (deck_size - x - y))

ds = []
deck_sizes = range(2, 1002, 10)
for deck_size in deck_sizes:
    side_count = deck_size // 2
    p_max = -1
    x0, y0 = 0, 0
    start_time = time.time()
    for x in range(side_count):
        for y in range(side_count):
            if x == y == 0 or x == y == side_count:
                continue
            p = p_red(x, y)
            if (p > p_max):
                p_max = p
                x0, y0 = x, y
    ds.append(time.time() - start_time)

print("red = %d\nblack = %d\np_max = %f" % (x0, y0, p_max))

plt.plot(deck_sizes, ds, 'b-')
plt.savefig("./time.png")

