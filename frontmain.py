import sys
import mne
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
import qdarktheme
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QSplitter,
    QScrollArea,
    QLabel,
    QSystemTrayIcon,
    QMenu,
)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import (
    Qt,
)
import qtawesome as qta
from components import MyToolbar, MyDockMenu, MyMenu
from globals import file_path

from back import EEG


class BrainNex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # init eeg class
        self.my_eeg = EEG()
        # self.left_eeg = EEG()
        # self.right_eeg = EEG()
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
        # initialize menu options class
        self.mymenu = MyMenu(self)
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea, self.mymenu)
        self.mymenu.hide()

        # init dock widget
        self.dock = MyDockMenu(self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
        self.dock.hide()

        # create first two btn layout
        button_layout = QHBoxLayout()
        # split btn
        split = qta.icon(
            "fa5s.columns",
            color="#ffffff",
        )
        self.split_button = QPushButton("Split screen")
        self.split_button.setIcon(split)
        self.split_button.clicked.connect(self.split_screen)
        # upload btn
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.clicked.connect(
            lambda: self.upload_data(self.inner_layout, hide_btns=True)
        )
        self.upload_button.setObjectName("upload_button")
        self.upload_button.setStyleSheet(
            """
        #upload_button {
            background: #1e2947;
            color: #ffffff;
        }
        #upload_button:hover {
            background-color:#868789;
        }
        """
        )
        button_layout.addWidget(self.upload_button)
        # read live data btn
        self.live_button = QPushButton("Read Time Data", self)
        self.live_button.clicked.connect(self.read_live_data)
        self.live_button.setObjectName("live_button")
        self.live_button.setStyleSheet(
            """
        #live_button {
            background: #575523;
            color: #ffffff;
        }
    
        #live_button:hover {
            background-color: #868789;
        }
        """
        )
        button_layout.addWidget(self.live_button)

        self.inner_layout.addLayout(button_layout)
        self.inner_layout.addWidget(self.split_button)

    # func to upload data from local env
    def upload_data(self, widget, hide_btns=True):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open EEG Data File", "", "EEG Files (*.edf *.fif);;"
        )
        if file_name:
            file_path = file_name

        self.raw = self.my_eeg.load_edf_data(file_path)

        if hide_btns:
            self.toolbar.show()
            self.upload_button.hide()
            self.live_button.hide()
            self.split_button.hide()
        # send uploaded data to be displayed on screen
        self.display_raw_eeg(self.raw, widget)

    def read_live_data(self):
        # read live data ; future development
        pass

    def show_all_channels(self, raw):
        self.raw_eeg_plot = mne.viz.plot_raw(raw, show=False)

        # Show the EEG plot in a separate window using mne
        self.raw_eeg_plot.canvas.manager.window.show()

    # func to display data after upload
    def display_raw_eeg(self, raw, layout):
        widget = QWidget()
        data_path_label = QLabel(f"Data: {self.my_eeg.file_path.split('/')[-1]}")
        # create sroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        v_layout = QVBoxLayout()
        widget.setLayout(v_layout)

        eeg_data = raw.get_data()
        time_axis = raw.times

        #  list to hold the PlotWidgets for each channel
        plot_widgets = []
        display_icon = qta.icon(
            "fa5s.arrow-right",
            color="#ffffff",
            color_active="#ffff00",
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

            plot_widget.setXRange(0.5, 15)

            v_layout.addWidget(plot_widget)
            # dispaly selected data chanell in separate window btn
            channel_button = QPushButton()
            channel_button.setFixedSize(20, 20)
            channel_button.setIcon(display_icon)
            channel_button.setObjectName("channel_button")
            channel_button.setStyleSheet(
                """
            #channel_button {
                background-color: #003366; border-radius:10px;
               
            }
            #channel_button:hover {
                background-color: #00416a;
                border-color:#EEEEEE;
            }
            """
            )
            channel_layout.addWidget(channel_button)
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
        self.popup_widget.showMaximized()
        popup_layout = QVBoxLayout()
        self.popup_widget.setLayout(popup_layout)

        channel_data = raw.get_data()[channel_index]

        time_axis = raw.times

        channel_plot_widget = pg.PlotWidget()

        channel_plot_widget.plot(
            time_axis, channel_data, pen=pg.mkPen(color=(255, 255, 255), width=1)
        )
        channel_plot_widget.setXRange(0.5, 10)
        channel_name = raw.info["ch_names"][channel_index]
        channel_plot_widget.setLabel("left", channel_name)
        channel_plot_widget.setLabel("bottom", "Time (s)")
        channel_plot_widget.setTitle(f"{channel_name} Data")
        popup_layout.addWidget(channel_plot_widget)
        self.popup_widget.setWindowTitle(f"Channel {channel_name} Data")
        self.popup_widget.show()

    def split_screen(self):
        # self.toolbar.close()

        splitter = QSplitter(Qt.Horizontal)
        left_widget = BrainNex()
        right_widget = BrainNex()

        # create the central widget for each split window
        left_central_widget = QWidget()
        right_central_widget = QWidget()
        left_widget.my_eeg = EEG()
        right_widget.my_eeg = EEG()
        left_widget.setCentralWidget(left_central_widget)
        right_widget.setCentralWidget(right_central_widget)

        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)

        self.setCentralWidget(splitter)
        # set left spliited window
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


def changeToLightTheme():
    qdarktheme.setup_theme("light")
    app.setPalette(qdarktheme.load_palette("light"))
    app.palette()


def changeToDarkTheme():
    qdarktheme.setup_theme("dark")
    app.setPalette(qdarktheme.load_palette("dark"))


def showMainWindow():
    window.showMaximized()
    window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    icon = QIcon("brain-icon.png")
    app.setWindowIcon(icon)
    app.setQuitOnLastWindowClosed(False)

    qdarktheme.setup_theme("auto")
    app.setPalette(qdarktheme.load_palette("auto"))
    # main application window entry
    window = BrainNex()
    # Create the tray for visibility in OS  toolbar
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # create the menu
    menu = QMenu()
    sun_icon = qta.icon(
        "fa5.sun",
        active="fa5.sun",
        color="#ffffff",
        color_active="#cbcbcb",
    )
    moon_icon = qta.icon(
        "fa5s.moon",
        active="fa5s.moon",
        color="#ffffff",
        color_active="#cbcbcb",
    )
    main_icon = qta.icon(
        "fa5s.tv",
        active="fa5s.tv",
        color="#ffffff",
        color_active="#cbcbcb",
    )
    actionLight = QAction(sun_icon, "Light Theme")
    actionLight.triggered.connect(changeToLightTheme)

    actionDark = QAction(moon_icon, "Dark Theme")
    actionDark.triggered.connect(changeToDarkTheme)
    show = QAction(main_icon, "Main Screen")
    show.triggered.connect(showMainWindow)
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(actionDark)
    menu.addAction(actionLight)
    menu.addAction(show)
    menu.addAction(quit)
    tray.setContextMenu(menu)

    window.showMaximized()
    window.show()
    sys.exit(app.exec())
