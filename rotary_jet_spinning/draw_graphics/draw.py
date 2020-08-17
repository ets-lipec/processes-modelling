#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


class PointGraph:

    def __init__(self, organized_data):
        self.organized_data = organized_data
        self.plot(organized_data)

    def plot(self, organized_data):

        for dataset in self.organized_data:
            fig = plt.figure()
            axes = fig.add_subplot(1, 1, 1)
            axes.plot(dataset["x"], dataset["y"], dataset["color"])
            axes.grid()
            axes.set_xlabel(dataset["x_legend"], fontsize=16)
            axes.set_ylabel(dataset["y_legend"], fontsize=16)
            axes.set_title(dataset["title"], fontsize=16, y=1.)
            plt.savefig(dataset["save_as"], format="pdf")
