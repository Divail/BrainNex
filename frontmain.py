import sys
import mne
import numpy as np
import matplotlib.pyplot as plt

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QToolBar,
    QListWidget,
)
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize
from darktheme.widget_template_pyqt6 import DarkApplication, DarkPalette

from components import LeftSideMenu, MyToolbar

# from back import display_raw_eeg
from back import preprocessing_ICA
from back import power_spectral_density_PSD

# from back import *


class BrainNex(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("BrainNex")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # Create a toolbar and add it to the QMainWindow
        toolbar = MyToolbar(self)
        self.addToolBar(toolbar)  # Show the toolbar

        self.layout = QVBoxLayout(self.central_widget)

        # left_menu = LeftSideMenu()
        # self.layout.addWidget(left_menu)

        button_layout = QHBoxLayout()
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.clicked.connect(self.upload_data)
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

        self.layout.addLayout(button_layout)
        self.raw_eeg_plot = None

    def upload_data(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open EEG Data File", "", "EEG Files (*.edf *.fif);;All Files (*)"
        )

        if file_name:
            raw = mne.io.read_raw_edf(file_name, preload=True)
            # craee the new buttons
            button_layout = QHBoxLayout()

            self.show_all_channels_button = QPushButton("Show All Channels", self)
            self.show_all_channels_button.clicked.connect(self.show_all_channels)
            self.show_all_channels_button.setStyleSheet(
                """
    QPushButton {
        background: #236c2f;
        width: 100%;
        margin-top: 2px;
        border: 1px solid #074a04;
        padding: 2px;
        border-radius:75%;
    }
    
    QPushButton:hover {
        background-color: #868789;
    }
    """
            )  # create new button
            self.create_watchlist_button = QPushButton("Create Watchlist", self)
            self.create_watchlist_button.clicked.connect(self.create_watchlist)
            self.create_watchlist_button.setStyleSheet(
                """
    QPushButton {
        background: #8d7623;
        width: 100%;
        margin-top: 2px;
        border: 1px solid #7e5302;
        padding: 2px;
        border-radius:75%;
    }
    
    QPushButton:hover {
        background-color: #868789;
    }
    """
            )
            # Add the new buttons to the layout
            button_layout.addWidget(self.show_all_channels_button)
            button_layout.addWidget(self.create_watchlist_button)
            self.layout.addLayout(button_layout)
            # Create a QListWidget for channel selection
            self.channel_list_widget = QListWidget()
            self.layout.addWidget(self.channel_list_widget)  # Add it to the layout
            self.channel_list_widget.setVisible(False)  #
            self.display_raw_eeg(raw)

    def read_live_data(self):
        # read real time or whatever
        pass

    def show_all_channels(self):
        # Show the plot
        self.raw_eeg_plot.show()

    def add_channel_to_watchlist(self):
        pass

    def create_watchlist(self, raw):
        pass

    def display_selected_channels(self):
        pass

    def display_raw_eeg(self, raw):
        # Clear any previous raw_eeg_plot if it exists
        if self.raw_eeg_plot:
            self.layout.removeWidget(self.raw_eeg_plot)
            self.raw_eeg_plot.get_figure().clear()
            plt.close(self.raw_eeg_plot.get_figure())

        # Create a new plot widget
        with plt.style.context("dark_background"):
            self.raw_eeg_plot = raw.plot(show=False, color="white")

        raw_eeg_plot_widget = self.raw_eeg_plot.get_figure().canvas
        self.layout.addWidget(raw_eeg_plot_widget)

        # Get the selected channels
        selected_channels = self.channel_list_widget.selectedItems()
        # Set the color of the selected channels to green
        for channel in selected_channels:
            self.raw_eeg_plot.get_lines()[channel.row()].set_color("green")

        # Set the color of the unselected channels to black
        for channel in range(len(self.raw_eeg_plot.get_axes())):
            if channel not in [item.row() for item in selected_channels]:
                self.raw_eeg_plot.get_axes()[channel].set_facecolor("black")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setPalette(DarkPalette())
    icon = QIcon("brain-icon.png")
    app.setWindowIcon(icon)
    window = BrainNex()

    window.show()
    sys.exit(app.exec())
