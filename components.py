from PyQt6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QToolBar,
    QDockWidget,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QWidget,
    QLineEdit,
    QComboBox,
    QGridLayout,
    QSpinBox,
    QFormLayout,
    QCheckBox,
    QDoubleSpinBox,
)
from PyQt6.QtGui import QAction
import mne
from PyQt6.QtCore import Qt, QSize, QPoint
import qtawesome as qta
from globals import file_path


class MyMenu(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("Menu")
        self.setFloatable(True)
        self.setMovable(True)
        # self.setFixedWidth(300)
        # self.setMaximumSize(1000, 1000)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setStyleSheet(
            """ 
            QToolBar { 
                background-color:  #313131;
             }
            QToolBar:hover { 
                background-color: #313131;
                color:#bebb48;
             }
            QPushButton {  
                color: black;           
            }
         """
        )
        layout = QVBoxLayout()
        layout.addStretch(20)
        # implements stuff
        btn_preprocessing_ICA = QAction("Preprocessing ICA", self)
        btn_plot_ica_properties = QAction("Plot ICA Properties", self)
        btn_plot_ica_1D = QAction("Plot ICA 1D", self)
        btn_plot_ica_topomap = QAction("Plot ICA Topomap", self)
        btn_power_spectral_density = QAction("Power Spectral Density", self)
        btn_psd_channels = QAction("PSD Channels", self)
        btn_lowpass_filter = QAction("Lowpass Filter", self)
        btn_highpass_filter = QAction("Highpass Filter", self)
        btn_bandpass_filter = QAction("Bandpass Filter", self)
        # btn_reset_raw = QPushButton("Reset Raw", self)
        # Add actions or connections to filter buttons if needed
        # btn_topomap_PSD.clicked.connect(self.topomap_PSD)
        # btn_plot_electrode.clicked.connect(self.plot_electrode)
        btn_preprocessing_ICA.triggered.connect(self.preprocessing_ICA)
        btn_plot_ica_properties.triggered.connect(self.plot_ica_components_properties)
        btn_plot_ica_1D.triggered.connect(self.plot_ica_components_1D)
        btn_plot_ica_topomap.triggered.connect(self.plot_ica_components_topomap)
        btn_power_spectral_density.triggered.connect(
            lambda: self.parent().my_eeg.power_spectral_density()
        )
        btn_psd_channels.triggered.connect(self.power_spectral_density_channels)
        btn_lowpass_filter.triggered.connect(self.lowpass_filtering)
        btn_highpass_filter.triggered.connect(self.highpass_filtering)
        btn_bandpass_filter.triggered.connect(self.bandpass_filtering)
        # btn_reset_raw.clicked.connect(self.reset_raw)

        self.addAction(btn_preprocessing_ICA)
        self.addAction(btn_plot_ica_properties)
        self.addAction(btn_plot_ica_1D)
        self.addAction(btn_plot_ica_topomap)
        self.addAction(btn_power_spectral_density)
        self.addAction(btn_psd_channels)
        self.addAction(btn_lowpass_filter)
        self.addAction(btn_highpass_filter)
        self.addAction(btn_bandpass_filter)
        # layout.addWidget(btn_reset_raw)
        layout.addStretch(20)

    # implements stuff
    def preprocessing_ICA(self):
        self.parent().dock.apply_function_parameters(1)
        self.parent().dock.show()

    # self.parent().my_raw.preprocessing_ICA()
    def plot_ica_components_properties(self):
        self.parent().dock.apply_function_parameters(2)
        self.parent().dock.show()

    def plot_ica_components_1D(self):
        self.parent().dock.apply_function_parameters(3)
        self.parent().dock.show()

    def plot_ica_components_topomap(self):
        self.parent().dock.apply_function_parameters(4)
        self.parent().dock.show()

    def power_spectral_density_channels(self):
        self.parent().dock.apply_function_parameters(5)
        self.parent().dock.show()

    def lowpass_filtering(self):
        self.parent().dock.apply_function_parameters(6)
        self.parent().dock.show()

    def highpass_filtering(self):
        self.parent().dock.apply_function_parameters(7)
        self.parent().dock.show()

    def bandpass_filtering(self):
        self.parent().dock.apply_function_parameters(8)
        self.parent().dock.show()

    def reset_raw(self):
        pass


class MyToolbar(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)

        tool_icon = qta.icon(
            "fa5s.wrench",
            active="fa5s.tools",
            color="#bebb48",
            color_active="#cbcbcb",
        )
        upload_icon = qta.icon(
            "fa5s.arrow-up",
            active="fa5s.upload",
            color="#bebb48",
            color_active="#cbcbcb",
        )
        live_read_data_icon = qta.icon(
            "fa5s.brain",
            active="fa5s.satellite-dish",
            color="#bebb48",
            color_active="#cbcbcb",
        )
        split_screen_icon = qta.icon(
            "fa5s.columns",
            active="fa5s.columns",
            color="#bebb48",
            color_active="#cbcbcb",
        )
        toolbar_icon = qta.icon(
            "fa5s.toolbox",
            active="fa5s.toolbox",
            color="#bebb48",
            color_active="#cbcbcb",
        )
        # Create the actions
        self.tool_action = QAction(tool_icon, "Menu ", self)
        # self.tool_action.setStatusTip("This is your button")
        self.tool_action.triggered.connect(self.onMyToolBarButtonClick)
        self.tool_action.setCheckable(True)
        self.upload_action = QAction(upload_icon, "Upload", self)
        self.upload_action.triggered.connect(self.uploadMyData)
        self.read_time_data_action = QAction(live_read_data_icon, "Live Data", self)
        self.split_screen_action = QAction(split_screen_icon, "Split screen", self)
        self.split_screen_action.triggered.connect(self.onMySplitScreen)
        self.show_toolbar = QAction(toolbar_icon, "Toolbar", self)
        self.show_toolbar.triggered.connect(self.showMyToolbar)
        self.addAction(self.tool_action)
        self.addSeparator()
        self.addAction(self.upload_action)
        self.addSeparator()
        self.addAction(self.read_time_data_action)
        self.addSeparator()
        self.addAction(self.split_screen_action)
        self.addSeparator()
        self.addAction(self.show_toolbar)
        self.setFloatable(True)
        self.setMovable(True)
        self.setIconSize(QSize(50, 25))
        self.setStyleSheet("background-color: transparent")

    def onMyToolBarButtonClick(self):
        if self.tool_action.isChecked():
            self.parent().mymenu.show()
        else:
            self.parent().mymenu.hide()

    # def onMyToolBarButtonClick(self):
    #     if self.tool_action.isChecked():
    #         # Show
    #         self.parent().left_menu.show()
    #     else:
    #         # Hide
    #         self.parent().left_menu.hide()

    def uploadMyData(self):
        # self.inner_layout = self.parent().layout()
        self.parent().upload_data(self.parent().inner_layout, hide_btns=False)

    def onMySplitScreen(self):
        self.parent().split_screen()

    def showMyToolbar(self):
        if self.parent().dock.isVisible():
            self.parent().dock.hide()
        else:
            self.parent().dock.show()


class MyDockMenu(QDockWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Options")
        # Create the dock
        self.setFixedWidth(350)

        central_widget = QWidget()
        self.setWidget(central_widget)
        self.form_layout = QFormLayout()
        self.form_layout.setVerticalSpacing(40)
        central_widget.setLayout(self.form_layout)
        central_widget.setStyleSheet(
            """
    QPushButton {
        background: #125904;
        width: 100%;
    }   
    QPushButton:hover {
        background-color: #1c8906;
    }   
    """
        )

    def apply_function_parameters(self, x):
        for i in reversed(range(self.form_layout.count())):
            widget = self.form_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        if x == 1:
            data_label = QLabel("Preprocessing ICA:")
            self.form_layout.addRow(data_label)
            self.n_components_spinbox = QSpinBox()
            self.n_components_spinbox.setValue(20)
            self.form_layout.addRow("n_components:", self.n_components_spinbox)

            self.random_state_spinbox = QSpinBox()
            self.random_state_spinbox.setValue(97)
            self.form_layout.addRow("random_state:", self.random_state_spinbox)

            self.max_iter_spinbox = QSpinBox()
            self.max_iter_spinbox.setValue(800)
            self.form_layout.addRow("max_iter:", self.max_iter_spinbox)

            apply_button = QPushButton("Apply")
            apply_button.clicked.connect(self.ok_clicked)

            self.setStyleSheet(
                """
            QSpinBox {
                 background-color:black;
                 color:white;
             }"""
            )

            self.form_layout.addWidget(apply_button)
        elif x == 2:
            data_label = QLabel("Plot ICA Properties: ")
            self.form_layout.addRow(data_label)
            self.picks_line_edit = QLineEdit()
            self.picks_line_edit.setPlaceholderText("Enter picks (comma-separated)")

            self.form_layout.addWidget(QLabel("Picks:"))
            self.form_layout.addRow(self.picks_line_edit)

            plot_button = QPushButton("Plot Properties")
            plot_button.clicked.connect(self.plot_ica_properties_cklicked)
            self.form_layout.addWidget(plot_button)
        elif x == 3:
            data_label = QLabel("Plot ICA 1D: ")
            self.form_layout.addRow(data_label)
            self.picks_input = QLineEdit(self)
            self.picks_input.setPlaceholderText("Specify picks (comma-separated)")
            self.form_layout.addWidget(self.picks_input)

            apply_button = QPushButton("Apply", self)
            apply_button.clicked.connect(self.plot_ica_1d)
            self.form_layout.addWidget(apply_button)
        elif x == 4:
            data_label = QLabel("Plot ICA Topomap: ")
            self.form_layout.addRow(data_label)
            self.picks_line_edit = QLineEdit()
            self.picks_line_edit.setPlaceholderText("Enter picks (comma-separated)")

            self.form_layout.addWidget(QLabel("Picks:"))
            self.form_layout.addRow(self.picks_line_edit)

            plot_button = QPushButton("Plot Topomap")
            plot_button.clicked.connect(self.plot_ica_topomap_cklicked)
            self.form_layout.addWidget(plot_button)
        elif x == 5:
            self.channels = []
            data_label = QLabel("PSD - Channel(s): ")
            self.form_layout.addRow(data_label)
            add_icon = qta.icon(
                "fa5s.plus",
                color="#DAA520",
            )
            self.add_button = QPushButton("", self)
            self.add_button.setIcon(add_icon)
            self.add_button.clicked.connect(self.add_channel)
            self.add_button.setStyleSheet(
                """QPushButton {
                    background-color: transparent;}
                QPushButton:hover {
                    background-color: #669ff51c;
                }
              """
            )
            remove_icon = qta.icon(
                "fa5s.minus",
                color="#DC143C",
            )
            self.remove_button = QPushButton("", self)
            self.remove_button.setIcon(remove_icon)
            self.remove_button.clicked.connect(self.remove_channel)
            self.remove_button.setStyleSheet(
                """
                QPushButton {
                    background-color: transparent;}
                QPushButton:hover {
                    background-color:#5796f43a;
                }
                   """
            )
            self.channel_combobox = QComboBox(self)
            self.form_layout.addRow(self.add_button)
            available_channels = self.parent().my_eeg.raw.info["ch_names"]
            self.channel_combobox.addItems(available_channels)
            self.form_layout.addRow(self.channel_combobox)
            self.form_layout.addRow(self.remove_button)
            self.selected_channels_label = QLabel(self)
            self.form_layout.addRow(self.selected_channels_label)

            # execute function psd channels
            self.calculate_button = QPushButton("Calculate channel PSD", self)
            self.calculate_button.clicked.connect(self.calculate_psd_channels)
            self.form_layout.addRow(self.calculate_button)
        elif x == 6:
            data_label = QLabel("Lowpass Filter: ")
            self.form_layout.addRow(data_label)
            self.high_frq_spinbox = QDoubleSpinBox()
            self.high_frq_spinbox.setRange(0.0, 100.0)
            self.high_frq_spinbox.setSingleStep(0.1)
            self.fir_design_combobox = QComboBox()
            self.fir_design_combobox.addItems(["firwin", "other_designs"])
            self.apply_button = QPushButton("Apply Lowpass")
            self.apply_button.clicked.connect(self.apply_lowpass)
            self.form_layout.addRow("High Frequency (Hz):", self.high_frq_spinbox)
            self.form_layout.addRow("Filter Design:", self.fir_design_combobox)
            self.form_layout.addRow("", self.apply_button)
        elif x == 7:
            data_label = QLabel("Highpass Filter: ")
            self.form_layout.addRow(data_label)
            self.low_frq_spinbox = QDoubleSpinBox()
            self.low_frq_spinbox.setRange(0.0, 100.0)
            self.low_frq_spinbox.setSingleStep(0.1)
            self.fir_design_combobox = QComboBox()
            self.fir_design_combobox.addItems(["firwin", "other_designs"])
            self.apply_button = QPushButton("Apply Highpass")
            self.apply_button.clicked.connect(self.apply_highpass)
            self.form_layout.addRow("Low Frequency (Hz):", self.low_frq_spinbox)
            self.form_layout.addRow("Filter Design:", self.fir_design_combobox)
            self.form_layout.addRow("", self.apply_button)
        elif x == 8:
            data_label = QLabel("Bandpass Filter: ")
            self.form_layout.addRow(data_label)
            self.low_frq_spinbox = QDoubleSpinBox()
            self.low_frq_spinbox.setRange(0.0, 100.0)
            self.low_frq_spinbox.setSingleStep(0.1)

            self.high_frq_spinbox = QDoubleSpinBox()
            self.high_frq_spinbox.setRange(0.0, 100.0)
            self.high_frq_spinbox.setSingleStep(0.1)
            self.fir_design_combobox = QComboBox()
            self.fir_design_combobox.addItems(["firwin", "other_designs"])

            self.skip_by_annotation_combobox = QComboBox()
            self.skip_by_annotation_combobox.addItems(["edge", "other_options"])

            self.apply_button = QPushButton("Apply bandpass")
            self.apply_button.clicked.connect(self.apply_bandpass)
            self.form_layout.addRow("Low Frequency (Hz):", self.low_frq_spinbox)
            self.form_layout.addRow("High Frequency (Hz):", self.high_frq_spinbox)
            self.form_layout.addRow("Filter Design:", self.fir_design_combobox)
            self.form_layout.addRow(
                "Skip by Annotation:", self.skip_by_annotation_combobox
            )
            self.form_layout.addRow("", self.apply_button)

    def add_channel(self):
        # Add the selected channel to the list
        selected_channel = self.channel_combobox.currentText()
        if selected_channel and selected_channel not in self.channels:
            self.channels.append(selected_channel)
        self.update_selected_channels_label()

    def remove_channel(self):
        # Remove the selected channel from the list

        if self.channels:
            self.channels.pop()
        self.update_selected_channels_label()

    def update_selected_channels_label(self):
        # Update the label
        self.selected_channels_label.setText(
            "Selected Channels: " + ", ".join(self.channels)
        )

    def ok_clicked(self):
        n_components = self.n_components_spinbox.value()
        random_state = self.random_state_spinbox.value()
        max_iter = self.max_iter_spinbox.value()
        self.parent().my_eeg.preprocessing_ICA(n_components, random_state, max_iter)
        self.hide()

    def plot_ica_properties_cklicked(self):
        picks_text = self.picks_line_edit.text()
        if picks_text == '':
            picks = None
        else:
            picks = [int(pick.strip()) for pick in picks_text.split(",")]
        self.parent().my_eeg.plot_ica_components_properties(picks=picks)
        self.hide()

    def plot_ica_1d(self):
        picks_text = self.picks_input.text()
        if picks_text == '':
            picks = None
        else:
            picks = [int(pick.strip()) for pick in picks_text.split(",")]
        self.parent().my_eeg.plot_ica_components_1D(picks)
        self.hide()

    def plot_ica_topomap_cklicked(self):
        picks_text = self.picks_line_edit.text()
        if picks_text == '':
            picks = None
        else:
            picks = [int(pick.strip()) for pick in picks_text.split(",")]
        self.parent().my_eeg.plot_ica_components_topomap(picks=picks)
        self.hide()

    def calculate_psd_channels(self):
        # selected_channel = self.channel_combobox.currentText()
        self.parent().my_eeg.power_spectral_density_channels(self.channels)
        self.channels.clear()

        self.hide()

    def apply_lowpass(self):
        high_frq = self.high_frq_spinbox.value()
        fir_design = self.fir_design_combobox.currentText()
        self.parent().my_eeg.lowpass_filtering(high_frq, fir_design)
        self.hide()

    def apply_highpass(self):
        low_frq = self.low_frq_spinbox.value()
        fir_design = self.fir_design_combobox.currentText()
        self.parent().my_eeg.highpass_filtering(low_frq, fir_design)
        self.hide()

    def apply_bandpass(self):
        low_frq = self.low_frq_spinbox.value()
        high_frq = self.high_frq_spinbox.value()
        fir_design = self.fir_design_combobox.currentText()
        skip_by_annotation = self.skip_by_annotation_combobox.currentText()
        self.parent().my_eeg.bandpass_filtering(
            low_frq, high_frq, fir_design, skip_by_annotation
        )
        self.hide()
