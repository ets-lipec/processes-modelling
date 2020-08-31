#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandas import DataFrame


class Save:

    def __init__(self, organized_data):
        self.organized_data = organized_data
        self.save(organized_data)

    def save(self, organized_data):
        for dataset in self.organized_data:
            # Put data in a dictionary
            dictData = {dataset["x_legend"]: dataset["x"], dataset["y_legend"]: dataset["y"]}
            dataFrm = DataFrame(dictData, columns= [dataset["x_legend"], dataset["y_legend"]])
            # Store the data in a file .csv in the folder data_files
            export_csv = dataFrm .to_csv (dataset["panda_file_title"], index = None, header = True)