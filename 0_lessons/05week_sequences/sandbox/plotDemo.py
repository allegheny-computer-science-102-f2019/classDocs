# Matplotlib plotting points demonstration
# code ref:
# 25 Sept 2019
# https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/marker_reference.html#sphx-glr-gallery-lines-bars-and-markers-marker-reference-py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D



# Notes on installing libraries
# matplotlib (for plotting)
# pip install --user matplotlib
# test in python3's interactive shell
# import matplotlib
# Python Crash Course: https://ehmatthes.github.io/pcc/




points = np.ones(3)  # Draw 3 points for each line
text_style = dict(horizontalalignment='right', verticalalignment='center',
                  fontsize=12, fontdict={'family': 'monospace'})
marker_style = dict(linestyle=':', color='0.8', markersize=10,
                    mfc="C0", mec="C0")


def format_axes(ax):
    ax.margins(0.2)
    ax.set_axis_off()
    ax.invert_yaxis()


def split_list(a_list):
    i_half = len(a_list) // 2
    return (a_list[:i_half], a_list[i_half:])

fig, axes = plt.subplots(ncols=2)
fig.suptitle('un-filled markers', fontsize=14)

# Filter out filled markers and marker settings that do nothing.
unfilled_markers = [m for m, func in Line2D.markers.items()
                    if func != 'nothing' and m not in Line2D.filled_markers]

for ax, markers in zip(axes, split_list(unfilled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot(y * points, marker=marker, **marker_style)
    format_axes(ax)

plt.show()

fig, axes = plt.subplots(ncols=2)
for ax, markers in zip(axes, split_list(Line2D.filled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot(y * points, marker=marker, **marker_style)
    format_axes(ax)
fig.suptitle('filled markers', fontsize=14)

plt.show()
