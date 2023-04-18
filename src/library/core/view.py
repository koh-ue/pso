#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: FIXME: XXX: HACK: NOTE: INTENT: USAGE:

import os
import numpy as np
import plotly.graph_objects as go

def drawGriewank(prob, surface_object = go.Surface, target='../../../figures/griewank.html', vis = True):
    x1 = np.arange(-prob.max_range_value, prob.max_range_value)
    x2 = np.arange(-prob.max_range_value, prob.max_range_value)
    x1, x2 = np.meshgrid(x1, x2)
    x_mesh = np.stack([x1, x2], 2)
    y = prob.eval(x_mesh)
    fig = go.Figure(data=[surface_object(x=x1, y=x2, z=y)])
    if vis:
        fig.show()
    fig.write_html(target)

def drawGriewank_withPlot(prob, x1, x2, y, surface_object = go.Mesh3d, target='../../../figures/griewank.html', vis = True):
    x1_mesh, x2_mesh = np.arange(-prob.max_range_value, prob.max_range_value), np.arange(-prob.max_range_value, prob.max_range_value)
    x1_mesh, x2_mesh = np.meshgrid(x1_mesh, x2_mesh)
    x_mesh = np.stack([x1_mesh, x2_mesh], 2)
    y_mesh = prob.eval(x_mesh)

    fig = go.Figure(data=[surface_object(x=x1_mesh, y=x2_mesh, z=y_mesh), go.Scatter3d(x=x1, y=x2, z=y, mode='markers')])
    if vis:
        fig.show()
    
    #--- ext
    if os.path.splitext(target)[-1] == '.html':
        fig.write_html(target)
    else:
        fig.write_image(target)

def drawGriewank_withWire(prob, x1, x2, y, title, target='../../../figures/griewank.html', vis = True):
    x1_mesh, x2_mesh = np.linspace(-prob.max_range_value, prob.max_range_value, 50), np.linspace(-prob.max_range_value, prob.max_range_value, 50)
    x1_mesh, x2_mesh = np.meshgrid(x1_mesh, x2_mesh)
    x_mesh = np.stack([x1_mesh, x2_mesh], 2)
    y_mesh = prob.eval(x_mesh)

    data_list = [go.Scatter3d(x=x1, y=x2, z=y, mode='markers', marker=dict(size=12, color=y, colorscale='Viridis'))]
    line_marker = dict(color='#0066FF', width=2)
    for i,j,k in zip(x1_mesh, x2_mesh, y_mesh):
        data_list.append(go.Scatter3d(x=i, y=j, z=k, mode='lines', line=line_marker))

    layout = go.Layout(showlegend=False, width=1500, height=1500, title=title)
    fig = go.Figure(data=data_list, layout=layout)
    if vis:
        fig.show()
    
    #--- ext
    if os.path.splitext(target)[-1] == ".html":
        fig.write_html(target)
    else:
        fig.write_image(target)