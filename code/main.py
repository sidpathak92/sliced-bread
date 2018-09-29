import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

from bokeh.io import curdoc, show
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import PreText, Select
from bokeh.plotting import figure

defaultDateRangeStart = dt.date(2014,1,1)
quandl.ApiConfig.api_key = "2xjA7xGppqWNJLZ2FsNx"

dollex30 = quandl.get("BSE/DOLL30")
realty = quandl.get("BSE/SIREAL")
bankex = quandl.get("BSE/SIBANK")

dollexPlot = figure(plot_width = 1000, plot_height = 300, x_axis_type = 'datetime')

dollexPlot.line(dollex30[defaultDateRangeStart:].index, 
                dollex30['Close'][defaultDateRangeStart:], 
                line_width = 1, line_color = 'green', legend = 'BSE Dollex 30')

dollexPlot.legend.location = "top_left"

realtyPlot = figure(plot_width = 1000, plot_height = 300, x_axis_type = 'datetime')

realtyPlot.line(realty[defaultDateRangeStart:].index, realty['Close'][defaultDateRangeStart:],
                line_width = 1, line_color = 'green', legend = 'BSE Realty')

realtyPlot.legend.location = "top_left"

bankexPlot = figure(plot_width = 1000, plot_height = 300, x_axis_type = 'datetime')

bankexPlot.line(bankex[defaultDateRangeStart:].index, bankex['Close'][defaultDateRangeStart:],
               line_width = 1, line_color = 'green', legend = 'BSE Bankex')

bankexPlot.legend.location = "top_left"

plots = column(dollexPlot, realtyPlot, bankexPlot)

curdoc().add_root(plots)