import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
from draw_matrix import *
from nussinov import *
matplotlib.use("TkAgg")


class Application:

    def __init__(self):
        self.layout = self._init_layout()
        self.window = sg.Window(
                    "Nussinov algorithm",
                    self.layout,
                    location=(0, 0),
                    finalize=True,
                    element_justification="center",
                    font="Helvetica 18",
                )
        self.fig = matplotlib.figure.Figure(figsize=(5, 5), dpi=100)
        self.data = None
        self.im = None
        self.fig_agg = None

    def _init_layout(self):
        return [
            [
                sg.Text("RNA sequence"),
                sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
                sg.Button("OK")
            ],
            [sg.Canvas(key="-CANVAS-")],
            [sg.Button("Left"), sg.Button("Play"), sg.Button("Right")]
        ]

    def validate_sequence(seq):
        pass

    def clean_fig(self):
        if self.fig_agg:
            delete_fig_agg(self.fig_agg, plt)

    def draw_fig(self):
        self.fig_agg = draw(self.data[self.data.frame], self.im, self.window, self.fig)

    def go_right(self):
        if self.data.frame == len(self.data.history) - 1:
            self.data.frame = 0
        else:
            self.data.frame += 1

    def go_left(self):
        if self.data.frame == 0:
            self.data.frame = len(self.data.history) - 1
        else:
            self.data.frame -= 1

    def run_loop(self):
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            elif event == 'Left':
                if not self.data: continue
                self.clean_fig()
                self.go_left()
                self.draw_fig()
            elif event == 'Right':
                if not self.data: continue
                self.clean_fig()
                self.go_right()
                self.draw_fig()
            elif event == 'Play':
                if not self.data: continue
                self.draw_fig()
            elif event == 'OK':
                seq = values['-FOLDER-']
                if not seq: continue
                self.clean_fig()
                self.data = Nussinov(seq)
                self.im = self.fig.add_subplot(111).imshow(self.data[self.data.frame])
                self.draw_fig()
        self.window.close()


if __name__ == '__main__':
    app = Application()
    app.run_loop()
