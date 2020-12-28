import PySimpleGUI as sg
# from numpy.random import random
import matplotlib
import matplotlib.pyplot as plt
from draw_matrix import *
from nussinov import *

# matrix = [[sg.Frame('', [[sg.I(random.randint(1,9), justification='r', size=(3,1),enable_events=True, key=(fr*3+r,fc*3+c)) for c in range(3)] for r in range(3)]) for fc in range(3)] for fr in range(3)]

layout = [
    [
        sg.Text("RNA sequence"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-")
    ],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button("Left"), sg.Button("Play"), sg.Button("Right")]
]

matplotlib.use("TkAgg")


def validate_sequence(seq):
    pass

window = sg.Window(
    "Nussinov algorithm",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

n = 8
def gen_data(seq):
    if seq == '':
        data = [[0 for x in range(0, n)],  # row 1
                [0 for x in range(0, n)],  # row 2
                [0 for x in range(0, n)],  # row 3
                [0 for x in range(0, n)],  # row 4
                [0 for x in range(0, n)],  # row 5
                [0 for x in range(0, n)],  # row 6
                [0 for x in range(0, n)],  # row 7
                [0 for x in range(0, n)]]  # row 8
    else:
        data = nussinov(seq)
    return data


fig = matplotlib.figure.Figure(figsize=(5, 5), dpi=100)
im = fig.add_subplot(111).imshow(gen_data(''))
# fig_agg = draw(gen_data(''), im, window, fig)


while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == 'Right':
        if exists('fig_agg'):
            delete_fig_agg(fig_agg, plt)
        data = gen_data(values['-FOLDER-'])
        fig_agg = draw(data, im, window, fig)
    elif event == 'Play':
        data = gen_data(values[0])
        fig_agg = draw(data, im, window, fig)
window.close()
