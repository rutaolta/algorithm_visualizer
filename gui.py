import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
import time
from draw_matrix import *
from nussinov import *
# from traceback import *

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
                    background_color="white"
                )
        self.fig = matplotlib.figure.Figure(figsize=(5, 5), dpi=100)
        self.data = None
        self.im = None
        self.fig_agg = None

    def _init_layout(self):
        return [
            [
                sg.Text("RNA sequence", background_color='white', text_color='black'),
                sg.In(size=(25, 1), enable_events=True, key="-SEQ-"),
                sg.Button("OK")
            ],
            [
                sg.Text(size=(25, 1), key="-TRACEBACK-"),
                sg.Button("Traceback")
            ],
            [
                sg.Canvas(key="-CANVAS-")
            ],
            [
                sg.Button("Left"),
                # sg.Button("Play"),
                sg.Button("Right")
            ]
        ]

    def validate_sequence(self, seq):
        if not seq.isalpha():
            return ''
        for char in seq.upper():
            if char not in 'ACGU':
                return ''
        return seq.upper()

    def clean_fig(self):
        if self.fig_agg:
            delete_fig_agg(self.fig_agg, plt)

    def draw_fig(self, data=None):

        if data:
            self.fig_agg = draw(data, self.im, self.window, self.fig)
        else:
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
            # elif event == 'Play':
            #     if not self.data: continue
            #     for m in self.data.history:
            #         self.clean_fig()
            #         self.draw_fig(m)
            #         time.sleep(1)
            elif event == 'OK':
                seq = self.validate_sequence(values['-SEQ-'])
                if not seq: continue
                self.clean_fig()
                self.data = Nussinov(seq)
                self.im = self.fig.add_subplot(111).imshow(self.data[-1], cmap='coolwarm')
                self.im.axes.set_xticklabels([''] + list(seq))
                self.im.axes.set_yticklabels([''] + list(seq))
                self.draw_fig()
            elif event == 'Traceback':
                pass
                # traceback = Traceback(self.data.sequence, self.data.get_last())
                # values["-TRACEBACK -"] = traceback.run()
                # s = traceback.run()
        self.window.close()


if __name__ == '__main__':
    app = Application()
    app.run_loop()
