import sys
import mne
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QSplitter,
    QDockWidget,
    QFrame,
    QLayout,
)
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPalette
from PyQt6.QtCore import (
    Qt,
    QSize,
    QPropertyAnimation,
    QSequentialAnimationGroup,
    QPoint,
)
from darktheme.widget_template_pyqt6 import DarkApplication, DarkPalette
from components import LeftSideMenu, MyToolbar, MyDockMenu


# from back import display_raw_eeg
from back import preprocessing_ICA
from back import power_spectral_density_PSD

# from back import *

global raw_data


class BrainNex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("BrainNex")
        # self.setGeometry(400, 400, 800, 600)
        self.setStyleSheet(
            """
QMainWindow {
background-image:url(backgr);
background-repeat:repeat;
background-position: center;

}
"""
        )
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # Create a toolbar and add it to the QMainWindow
        self.toolbar = MyToolbar(self)
        self.addToolBar(self.toolbar)  # Show the toolbar
        self.toolbar.hide()  # hide toolbar for start
        self.main_layout = QHBoxLayout(self.central_widget)
        self.inner_widget = QWidget()
        self.inner_layout = QVBoxLayout()
        self.inner_widget.setLayout(self.inner_layout)
        self.main_layout.addWidget(self.inner_widget)
        # initialize LeftMenu class

        self.left_menu = LeftSideMenu()
        self.left_menu.hide()
        # create dick widget
        self.dock = MyDockMenu(self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
        self.dock.hide()

        # create first two btn
        button_layout = QHBoxLayout()
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.clicked.connect(
            lambda: self.upload_data(self.inner_layout, hide_btns=True)
        )
        # self.upload_button.clicked.connect(self.upload_button.deleteLater)
        self.upload_button.setStyleSheet(
            """
    QPushButton {
        background: #1e2947;
        width: 100%;
        margin-top: 2px;
        border: 1px solid #3d4f7c;
        padding: 2px;
        border-radius:75%;
    }
    
    QPushButton:hover {
        background-color:#868789;
    }
    """
        )
        button_layout.addWidget(self.upload_button)
        self.live_button = QPushButton("Read Time Data", self)
        self.live_button.clicked.connect(self.read_live_data)
        self.live_button.setStyleSheet(
            """
    QPushButton {
        background: #575523;
        width: 100%;
        margin-top: 2px;
        border: 1px solid #897e03;
        padding: 2px;
        border-radius:75%;
    }
    
    QPushButton:hover {
        background-color: #868789;
    }
    """
        )
        button_layout.addWidget(self.live_button)

        self.inner_layout.addLayout(button_layout)

        self.raw_eeg_plot = None

    def upload_data(self, widget, hide_btns=True):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open EEG Data File", "", "EEG Files (*.edf *.fif);;"
        )
        if file_name:
            raw = mne.io.read_raw_edf(file_name, preload=True)
            global raw_data
            raw_data = raw
            # remove prev btns but show toolbar
            # if hasattr(self, "toolbar"):

        if hide_btns:
            self.toolbar.show()
            self.upload_button.hide()
            self.live_button.hide()

        self.display_raw_eeg(raw, widget)

    def read_live_data(self):
        # read real time or whatever
        pass

    def show_all_channels(self):
        # Create the EEG plot
        self.raw_eeg_plot = mne.viz.plot_raw(raw_data, show=False)

        # Show the EEG plot in a separate window using mne
        self.raw_eeg_plot.canvas.manager.window.show()

    def add_channel_to_watchlist(self):
        pass

    def create_watchlist(self):
        pass

    def display_selected_channels(self):
        pass

    def get_raw_data():
        return raw_data

    # this bs display func needd to be rewritten
    def display_raw_eeg(self, raw, layout):
        plot_widget = pg.PlotWidget()

        # Set the plot's background color to white
        plot_widget.setBackground("default")

        pens = []
        for i in range(raw.info["nchan"]):
            pens.append(pg.mkPen(color=(255, 255, 255), width=1))

        # Plot the EEG data for each channel
        for i in range(raw.info["nchan"]):
            plot_widget.plot(raw.get_data()[i], pen=pens[i])

        # Add the plot widget to the given widget
        layout.addWidget(plot_widget)

    # widget.addWidget(self.raw_eeg_plot.get_figure().canvas)

    def split_screen(self):
        splitter = QSplitter(Qt.Horizontal)

        left_widget = QMainWindow()
        right_widget = QMainWindow()
        # left_layout = QVBoxLayout()
        # right_layout = QVBoxLayout()
        # Create the central widget for each split window
        left_central_widget = QWidget()
        right_central_widget = QWidget()

        left_widget.setCentralWidget(left_central_widget)
        right_widget.setCentralWidget(right_central_widget)
        # left_widget.setLayout(left_layout)
        # right_widget.setLayout(right_layout)
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        self.toolbar.close()
        # self.main_layout.addWidget(splitter)
        self.setCentralWidget(splitter)
        # left main window
        # left_widget.inner_layout = left_widget.layout()
        left_widget.inner_layout = QVBoxLayout()
        left_central_widget.setLayout(left_widget.inner_layout)

        left_tool = MyToolbar(left_widget)
        left_widget.upload_data = self.upload_data
        left_widget.addToolBar(left_tool)
        left_widget.left_menu = LeftSideMenu()

        # left_widget.setLayout(left_widget.inner_layout)
        # do right main window
        right_widget.inner_layout = QVBoxLayout()
        right_central_widget.setLayout(right_widget.inner_layout)

        right_tool = MyToolbar(left_widget)
        right_widget.upload_data = self.upload_data
        right_widget.addToolBar(right_tool)
        right_widget.left_menu = LeftSideMenu()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setPalette(DarkPalette())
    icon = QIcon("brain-icon.png")
    app.setWindowIcon(icon)
    window = BrainNex()
    window.showMaximized()
    window.show()
    sys.exit(app.exec())
