#!/usr/bin/env python2

import math, wx

from wx import glcanvas
from OpenGL.GLU import *
from OpenGL.GL import *

from numpy import *
import matplotlib
matplotlib.use('WXAgg')
import matplotlib.pyplot as plt

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure


class CanvasFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Mandelbrot thingy', size=(550, 350))

        width = 400
        height = 400

        itermax = 50
        xmin = -1
        xmax = .5
        ymin = -1.25
        ymax = 1.25

        I = self.mandel(width, height, itermax, xmin, xmax, ymin, ymax)
        I[I==0] = 101

        # self.Bind(wx.EVT_PAINT, self.OnPaint)
        # plt.matshow(I.T, origin='lower left')

        self.figure = Figure()
        print(self.figure)
        self.axes = self.figure.add_subplot(111)
        print(self.axes)
        # t = arange(0.0, 3.0, 0.01)
        # s = sin(2 * pi * t)

        self.axes.imshow(I.T, origin='lower left')
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

    def OnPaint(self, event=None):
        pass

    def mandel(self, n, m, itermax, xmin, xmax, ymin, ymax):
        ix, iy = mgrid[0:n, 0:m]

        x = linspace(xmin, xmax, n)[ix]
        y = linspace(ymin, ymax, m)[iy]

        c = x+complex(0,1)*y
        del x, y

        img = zeros(c.shape, dtype=int)

        ix.shape = n*m
        iy.shape = n*m
        c.shape = n*m

        z = copy(c)
        for i in range(itermax):
            if not len(z): break

            multiply(z, z, z)
            add(z, c, z)

            rem = abs(z)>2.0

            img[ix[rem], iy[rem]] = i+1

            rem = -rem

            z = z[rem]
            ix, iy = ix[rem], iy[rem]
            c = c[rem]

        return img



class App(wx.App):
    def OnInit(self):
        frame = CanvasFrame()
        frame.Show(True)

        self.frame = frame

        return True

    def OnExitApp(self, evt):
        self.frame.Close(True)

    def OnCloseFrame(self, evt):
        if hasattr(self, "window") and hasattr(self.window, "ShutdownDemo"):
            self.window.ShutdownDemo()

        evt.Skip()

if __name__ == '__main__':
    app = App()
    app.MainLoop()
