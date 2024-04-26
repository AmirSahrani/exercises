import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim

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
    "savefig.format": "png",
    "savefig.transparent": True,
    "axes.grid": True,
    "grid.linewidth": 0.5,
    "grid.linestyle": "--",
    "grid.color": "0.8",
    "image.cmap": "Blues",
    "lines.linewidth": 1.5,
    "lines.markersize": 6,
    "text.usetex": True,
    "mathtext.fontset": "cm",
    "pgf.preamble": r"\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{cmbright}"
})


def f(x):
    return x**2


def df(x):
    return 2 * x


def derivative(f, x, h):
    return (f(x + h) - f(x)) / h


x = np.linspace(-10, 10, 100)
x_loc = 3
h = [1, 0.1, 0.01, 0.001, 0.0001]
y = f(x)
dy = df(x_loc) * (x - x_loc) + f(x_loc)

fig, ax = plt.subplots(figsize=(8, 6))


def update(i):
    ax.clear()
    axins = ax.inset_axes([0.3, 0.6, 0.35, 0.35])
    # axins.clear()

    dy_est = derivative(f, x_loc, h[i])
    dy_est_line = dy_est * (x - x_loc) + f(x_loc)
    ax.plot(x, y, label='$f(x) = x^2$', color='black')
    ax.plot(x, dy, label="$f'(x) = 2x$", color='blue', linestyle='--')
    ax.plot(x_loc, f(x_loc), 'ro')
    ax.plot(x, dy_est_line, label="Estimated derivative", color='red')

    ax.set_title(f"Estimation of the derivative at h={h[i]}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 20)

    # Reconfigure axins after clearing it
    axins.plot(x, y, color='black')
    axins.plot(x, dy, color='blue')
    axins.plot(x_loc, f(x_loc), 'ro')
    axins.plot(x, dy_est_line, color='red')
    axins.set_xlim(2.95, 3.05)
    axins.set_ylim(8.55, 9.45)
    axins.set_xticks([])
    axins.set_yticks([])

    # Indicate the zoom again
    ax.indicate_inset_zoom(axins, edgecolor="black")

    ax.legend(loc='upper left')


ani = anim.FuncAnimation(fig, update, frames=len(h), interval=1000, repeat=False)
ani.save("derivative_animation.gif", writer='pillow', fps=1, dpi=100)
plt.show()
