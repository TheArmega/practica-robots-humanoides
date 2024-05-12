#!/usr/bin/env python

"""\
lipm2d.py: A tiny 2d LIPM simulation with matplotlib animation.

- Partial inspiration (beware some bugs atow): <https://github.com/AtsushiSakai/PythonRobotics/blob/808e98133d57426b1e6fbbc2bdc897a196278d7d/Bipedal/bipedal_planner/bipedal_planner.py>
"""

__author__ = "Juan G Victores"
__copyright__ = "Copyright 2024, Planet Earth"

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from time import sleep

MAX_TIME = 60
HEIGHT = 0.2 * len("santillan")
G = 9.8
TIME_DELTA = 0.1  # s

fig, ax = plt.subplots()
(ln,) = ax.plot([], [], marker="o")


def init():
    # ax.set_xlim(0, 800)
    ax.set_xlim(0, 400)
    ax.set_ylim(-0.1, 2)
    return (ln,)


def animate(args):
    return (ln,)


class Simulator:
    def __init__(self):
        # self.zmp_y = [200, 600, 200, 600]
        # self.zmp_time_change = [26, 31, 35, 38]
        self.zmp_y = [100, 300, 100, 300, 100, 300, 100, 300, 100]
        k = 5
        self.zmp_time_change = [
            24,
            29,
            31 + k,
            31 + k * 2,
            31 + k * 3,
            31 + k * 4,
            31 + k * 5,
            31 + k * 6,
            31 + k * 7,
        ]
        self.zmp_idx = 0
        # self.c_y = 200.1
        self.c_y = self.zmp_y[0] + 0.75  # para que arranque
        self.c_y_dot = 0
        self.currentTimeStep = 0
        self.foot = "LF"  # left foot
        print("self.zmp_idx", self.zmp_idx, self.foot)

    def __call__(self):
        y_dot2 = G / HEIGHT * (self.c_y - self.zmp_y[self.zmp_idx])
        self.c_y += self.c_y_dot * TIME_DELTA
        self.c_y_dot += y_dot2 * TIME_DELTA

        ln.set_data([self.zmp_y[self.zmp_idx], self.c_y], [0, HEIGHT])
        # ln.set_data([180, self.currentTimeStep, 0, self.currentTimeStep], [0, HEIGHT, 0, HEIGHT])

        self.currentTimeStep += 1
        # sleep(0.1)

        if self.currentTimeStep > self.zmp_time_change[self.zmp_idx]:
            self.zmp_idx += 1
            if self.foot == "LF":
                self.foot = "RF"
            else:
                self.foot = "LF"
            print(
                "self.zmp_idx", self.zmp_idx, self.currentTimeStep, self.foot, self.c_y
            )

        if self.currentTimeStep > MAX_TIME:
            quit()

        return 1


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
    save_count=MAX_TIME,
)
plt.show()
