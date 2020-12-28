import sys
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def print_matrix(data, im):
    im.set_data(data)
    im.axes.texts = []
    for (i, j), z in np.ndenumerate(data):
        im.axes.text(j, i, '{:0.1f}'.format(z), ha='center', va='center')


def draw(data, im, window, fig):
    print_matrix(data, im)
    return draw_figure(window["-CANVAS-"].TKCanvas, fig)


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg


def delete_fig_agg(fig_agg, plt):
    fig_agg.get_tk_widget().forget()
    plt.close('all')


def exists(name):
    return (name in sys._getframe(1).f_locals  # caller's locals
         or name in sys._getframe(1).f_globals # caller's globals
    )
