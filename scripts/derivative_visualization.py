import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim
from functools import partial

# Set up plot aesthetics
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 18,
    "axes.titlesize": 18,
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.fontsize": 12,
    "figure.figsize": (8, 6),
    "figure.dpi": 100,
    "savefig.dpi": 200,
    "savefig.transparent": True,
    "axes.grid": True,
    "grid.linewidth": 0.5,
    "grid.linestyle": "--",
    "grid.color": "0.8",
    "image.cmap": "Blues",
    "lines.linewidth": 1.5,
    "lines.markersize": 6,
    "text.usetex": True,
    "mathtext.fontset": "cm"
})

# Function definition


def f(x):
    return x ** 6


def df(x):
    return 6 * x ** 5


def derivative(f, x, h):
    return (f(x + h) - f(x)) / h


def update(i, ax, x, y, dy, x_loc, h):
    ax.clear()
    axins = ax.inset_axes([0.35, 0.6, 0.35, 0.35])

    dy_est = derivative(f, x_loc, h[i])
    dy_est_line = dy_est * (x - x_loc) + f(x_loc)
    ax.plot(x, y, label='$f(x) = x^6$', color='black')
    ax.plot(x, dy, label="$f'(x) = 6x^5$", color='blue', linestyle='--')
    ax.plot(x_loc, f(x_loc), 'ro')
    ax.plot(x, dy_est_line, label="Estimated derivative", color='red')
    ax.vlines(x_loc, 0, f(x_loc), color='green', linestyle='--')
    ax.vlines(x_loc+h[i], 0, f(x_loc +h[i]), color='green', linestyle='--')

    ax.set_title(f"Estimating the derivative at $x = {x_loc}$ with $h = {h[i]:.1e}$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(-0.5, 4)
    ax.set_ylim(-0.5, 1300)

    axins.plot(x, y, color='black')
    axins.plot(x, dy, color='blue')
    axins.plot(x_loc, f(x_loc), 'ro')
    axins.plot(x, dy_est_line, color='red')
    axins.set_xlim(x_loc - 0.1, x_loc + 0.1)
    axins.set_ylim(f(x_loc) - 20, f(x_loc) + 20)
    axins.set_xticks([])
    axins.set_yticks([])

    ax.indicate_inset_zoom(axins, edgecolor="black")
    ax.legend(loc='upper left')


def main():
    x = np.linspace(-0.1, 10, 400)
    x_loc = 2.4
    h = np.logspace(0, -4, 100)
    y = f(x)
    slope = df(x_loc)
    dy = slope * (x - x_loc) + f(x_loc)

    fig, ax = plt.subplots(figsize=(8, 6))

    update_filled = partial(update, ax=ax, x=x, y=y, dy=dy, x_loc=x_loc, h=h)

    ani = anim.FuncAnimation(fig, update_filled, frames=len(h), interval=100, repeat=False)
    ani.save("figures/derivative_animation.gif", writer='pillow', fps=10, dpi=100)
    plt.show()


if __name__ == "__main__":
    main()
