#!/usr/bin/env python

"""\
lipm3d_diagonal_stairs.py: A tiny 3d LIPM simulation with matplotlib animation, moving diagonally with stairs-like motion.
"""

__author__ = "Juan G Victores"
__copyright__ = "Copyright 2024, Planet Earth"

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

MAX_X = 1200
HEIGHT = 0.2 * len("santillan")
G = 9.8
TIME_DELTA = 0.1  # s

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
(ln,) = ax.plot([], [], [], marker="o")


def init():
    ax.set_xlim(0, MAX_X)
    ax.set_ylim(0, MAX_X)  # Adjusted to match x range
    ax.set_zlim(0, HEIGHT)
    return (ln,)


def askGravity():
    print("###### Elije la gravedad que quieres experimentar ######\n")
    print(
        "Mercurio: 2.78 m/s2\nVenus: 8.87 m/s2\nTierra: 9.81 m/s2\nLuna: 1.62 m/s2\nMarte: 3.72 m/s2\nJupiter: 22.88 m/s2\nSaturno: 9.05 m/s2\nUrano: 7.77 m/s2\nNeptuno: 11 m/s2"
    )
    planeta = input("Indica el nombre del planeta: ")
    match planeta:
        case "Mercurio":
            return 2.78
        case "Venus":
            return 8.87
        case "Tierra":
            return 9.81
        case "Luna":
            return 1.62
        case "Marte":
            return 3.72
        case "Jupiter":
            return 22.88
        case "Saturno":
            return 9.05
        case "Urano":
            return 7.77
        case "Neptuno":
            return 11
        case _:
            print("Introduce un planeta valido...")


G = askGravity()


def animate(args):
    return (ln,)


class Simulator:
    def __init__(self):
        self.zmp_x = [0, 200, 400, 600, 800, 1000, 1200, 1400]
        self.zmp_y = [0, 200, 400, 600, 800, 1000, 1200, 1400]
        # Modifica las alturas de los puntos en el eje Z
        self.zmp_z = [1, 1.5, 1, 1.5, 1, 1.5, 1, 1.5]
        self.zmp_x_change = [100, 300, 500, 700, 900, 1100, 1300]
        self.zmp_y_change = [100, 300, 500, 700, 900, 1100, 1300]
        self.zmp_idx = 0
        self.c_x = self.zmp_x[0] + 0.1  # para que arranque
        self.c_y = self.zmp_y[0] + 0.1  # para que arranque
        self.c_z = self.zmp_z[0]  # para que arranque
        self.c_x_dot = 0
        self.c_y_dot = 0
        self.aux = 100

    def __call__(self):
        x_dot2 = G / HEIGHT * (self.c_x - self.zmp_x[self.zmp_idx])
        y_dot2 = G / HEIGHT * (self.c_y - self.zmp_y[self.zmp_idx])

        # Incrementa la coordenada Z solo cuando el eje X cambie
        if self.aux < self.zmp_x_change[self.zmp_idx]:
            self.c_z = self.zmp_z[self.zmp_idx]
            self.aux = self.zmp_x_change[self.zmp_idx]

        self.c_x += self.c_x_dot * TIME_DELTA
        self.c_y += self.c_y_dot * TIME_DELTA
        self.c_x_dot += x_dot2 * TIME_DELTA
        self.c_y_dot += y_dot2 * TIME_DELTA

        ln.set_data(
            [self.zmp_x[self.zmp_idx], self.c_x], [self.zmp_y[self.zmp_idx], self.c_y]
        )
        ln.set_3d_properties([0, self.c_z])

        if (
            self.c_x > self.zmp_x_change[self.zmp_idx]
            or self.c_y > self.zmp_y_change[self.zmp_idx]
        ):
            self.zmp_idx += 1

        if self.c_x > MAX_X or self.c_y > MAX_X:
            quit()

        return (ln,)


simulator = Simulator()


def frames():
    while True:
        yield simulator()


ani = FuncAnimation(
    fig,
    animate,
    frames=frames,
    interval=100,
    init_func=init,
    blit=True,
    save_count=MAX_X,
)
plt.show()
