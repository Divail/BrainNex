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
    QSplitter,
    QDockWidget,
    QFrame,
    QLayout,
    QSizePolicy,
    QScrollArea,
    QScrollBar,
    QLabel,
    QDialog,
)
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPalette, QAction
from PyQt6.QtCore import (
    Qt,
    QSize,
    QPropertyAnimation,
    QSequentialAnimationGroup,
    QPoint,
)
import qtawesome as qta
from darktheme.widget_template_pyqt6 import DarkApplication, DarkPalette
from components import MyToolbar, MyDockMenu, MyMenu
from globals import file_path
import qdarktheme
from back import EEG


class BrainNex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.my_eeg = EEG()
        self.left_eeg = EEG()
        self.right_eeg = EEG()
        self.setWindowTitle("BrainNex")
        # self.setGeometry(400, 400, 800, 600)
        #        # self.setStyleSheet(
        #             """
        # QMainWindow {
        # background-image:url(backgr);
        # background-repeat:repeat;
        # background-position: center;

        # }
        # """
        #         )

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
        self.mymenu = MyMenu(self)
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea, self.mymenu)
        self.mymenu.hide()

        # we Dont use LEFT menu rn
        # self.left_menu = LeftSideMenu()
        # self.left_menu.hide()

        # create dock widget
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

    def upload_data(self, widget, hide_btns=True):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open EEG Data File", "", "EEG Files (*.edf *.fif);;"
        )
        if file_name:
            file_path = file_name
            # raw = mne.io.read_raw_edf(file_name, preload=True)

        self.raw = self.my_eeg.load_edf_data(file_path)

        if hide_btns:
            self.toolbar.show()
            self.upload_button.hide()
            self.live_button.hide()

        self.display_raw_eeg(self.raw, widget)

    def read_live_data(self):
        # read real time or whatever
        pass

    def show_all_channels(self, raw):
        # Create the EEG plot
        self.raw_eeg_plot = mne.viz.plot_raw(raw, show=False)

        # Show the EEG plot in a separate window using mne
        self.raw_eeg_plot.canvas.manager.window.show()

    def add_channel_to_watchlist(self):
        pass

    def create_watchlist(self):
        pass

    def display_selected_channels(self):
        pass

    def display_raw_eeg(self, raw, layout):
        widget = QWidget()
        data_path_label = QLabel(f"Data: {self.my_eeg.file_path.split('/')[-1]}")
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        v_layout = QVBoxLayout()
        widget.setLayout(v_layout)

        eeg_data = raw.get_data()
        time_axis = raw.times

        #  list to hold the PlotWidgets for each channel
        plot_widgets = []
        display_icon = qta.icon(
            "fa5s.tv",
            color="#ffffff",
            color_active="grey",
        )
        for i in range(eeg_data.shape[0]):
            plot_widget = pg.PlotWidget()
            channel_layout = QHBoxLayout()
            plot_widgets.append(plot_widget)

            # graph the EEG data for the channel
            plot_widget.plot(
                time_axis, eeg_data[i], pen=pg.mkPen(color=(255, 255, 255), width=1)
            )
            channel_name = raw.info["ch_names"][i]
            plot_widget.setLabel("left", channel_name)
            plot_widget.setTitle(f"{i + 1}: {channel_name}")
            plot_widget.setLabel("bottom", "Time (s)")
            plot_widget.setMinimumHeight(180)

            x_min = time_axis.min()
            x_max = time_axis.max()
            plot_widget.setXRange(x_min, x_max)
            # plot_widget.setYRange(eeg_data.min(), eeg_data.max())
            # plot_widget.setXRange(time_axis.min(), time_axis.max())
            v_layout.addWidget(plot_widget)

            channel_button = QPushButton()
            channel_button.setFixedSize(20, 20)
            # channel_button.setStyleSheet("background-color: blue; border-radius: 5px;")
            channel_button.setIcon(display_icon)
            # channel_button.setStyleSheet(
            #     """
            # QPushButton {
            #     background-color: transparent;
            # }

            # """
            # )
            channel_button.setStyleSheet(
                """
            QPushButton {
                background-color: #003366; border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #00416a;
            }
            """
            )
            channel_layout.addWidget(channel_button)
            # v_layout.addWidget(channel_button)
            channel_layout.addWidget(plot_widget)
            v_layout.addLayout(channel_layout)
            # Connect a slot to the button click event to open a popup window
            channel_button.clicked.connect(
                lambda state, i=i: self.show_channel_popup(raw, i)
            )
        # add the widget containing all PlotWidgets to the layout

        scroll_area.setWidget(widget)
        layout.addWidget(data_path_label)
        layout.addWidget(scroll_area)

    # layout.addWidget(self.raw_eeg_plot.get_figure().canvas)
    def show_channel_popup(self, raw, channel_index):
        #  popup window to display the channel data separately

        self.popup_widget = QWidget()

        popup_layout = QVBoxLayout()
        self.popup_widget.setLayout(popup_layout)

        channel_data = raw.get_data()[channel_index]
        time_axis = raw.times

        channel_plot_widget = pg.PlotWidget()
        channel_plot_widget.plot(
            time_axis, channel_data, pen=pg.mkPen(color=(255, 255, 255), width=1)
        )
        channel_name = raw.info["ch_names"][channel_index]
        channel_plot_widget.setLabel("left", channel_name)
        channel_plot_widget.setLabel("bottom", "Time (s)")
        channel_plot_widget.setTitle(f"{channel_name} Data")
        popup_layout.addWidget(channel_plot_widget)

        self.popup_widget.setWindowTitle(f"Channel {channel_name} Data")
        self.popup_widget.show()

    def split_screen(self):
        splitter = QSplitter(Qt.Horizontal)

        left_widget = BrainNex()
        right_widget = BrainNex()

        # create the central widget for each split window
        left_central_widget = QWidget()
        right_central_widget = QWidget()
        left_widget.my_eeg = self.left_eeg
        right_widget.my_eeg = self.right_eeg
        left_widget.setCentralWidget(left_central_widget)
        right_widget.setCentralWidget(right_central_widget)

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
        left_widget.dock = MyDockMenu(left_widget)
        left_widget.addDockWidget(
            Qt.DockWidgetArea.LeftDockWidgetArea, left_widget.dock
        )
        left_widget.dock.hide()
        left_widget.mymenu = MyMenu(left_widget)
        left_widget.addToolBar(Qt.ToolBarArea.RightToolBarArea, left_widget.mymenu)
        left_widget.mymenu.hide()
        #

        left_widget.addToolBar(left_tool)

        # left_widget.setLayout(left_widget.inner_layout)
        # do right main window
        right_widget.inner_layout = QVBoxLayout()
        right_central_widget.setLayout(right_widget.inner_layout)

        right_tool = MyToolbar(right_widget)
        right_widget.dock = MyDockMenu(right_widget)
        right_widget.addDockWidget(
            Qt.DockWidgetArea.LeftDockWidgetArea, right_widget.dock
        )
        right_widget.dock.hide()
        right_widget.mymenu = MyMenu(right_widget)
        right_widget.addToolBar(Qt.ToolBarArea.RightToolBarArea, right_widget.mymenu)
        right_widget.mymenu.hide()

        right_widget.addToolBar(right_tool)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setPalette(DarkPalette())
    icon = QIcon("brain-icon.png")

    app.setWindowIcon(icon)
    qdarktheme.setup_theme(
        custom_colors={
            "[dark]": {
                "primary": "#ffffff",
            }
        }
    )
    app.setPalette(qdarktheme.load_palette("dark"))
    window = BrainNex()
    window.showMaximized()
    window.show()
    sys.exit(app.exec())
