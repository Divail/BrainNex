from PyQt6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
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
)
from PyQt6.QtGui import QAction

from PyQt6.QtCore import Qt, QSize, QPoint
import qtawesome as qta
from globals import file_path


class LeftSideMenu(QMenu):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Options")

        self.setFixedWidth(300)

        self.setStyleSheet(
            """
            QPushButton {
               
                color: black;

            }
            """
        )

        layout = QVBoxLayout(self)

        # Buttons for MNE filters and ICA analysis
        btn_bandpass_filter = QPushButton("Apply Bandpass Filter", self)

        btn_notch_filter = QPushButton("Power Spectral Density", self)
        btn_ica_analysis = QPushButton("Run ICA Analysis", self)
        btn_fastica = QPushButton("FastICA", self)
        btn_infomax = QPushButton("Infomax", self)
        btn_extended_infomax = QPushButton("Extended Infomax", self)
        btn_amica = QPushButton("AMICA", self)
        btn_picard = QPushButton("Picard", self)
        btn_jade = QPushButton("JADE", self)
        btn_sobi = QPushButton("SOBI", self)
        btn_corrca = QPushButton("CorrCA", self)
        btn_combi = QPushButton("Combi", self)
        btn_tdsep = QPushButton("TDSEP", self)
        btn_afdica = QPushButton("AFDICA", self)
        btn_sobiwhiten = QPushButton("SOBIwhiten", self)
        btn_topomap_PSD = QPushButton("Topomap PSD", self)
        btn_plot_electrode = QPushButton("Plot Electrode", self)
        btn_preprocessing_ICA = QPushButton("Preprocessing ICA", self)
        btn_plot_ica_properties = QPushButton("Plot ICA Properties", self)
        btn_plot_ica_1D = QPushButton("Plot ICA 1D", self)
        btn_plot_ica_topomap = QPushButton("Plot ICA Topomap", self)
        btn_power_spectral_density = QPushButton("Power Spectral Density", self)
        btn_psd_channels = QPushButton("PSD Channels", self)
        btn_lowpass_filter = QPushButton("Lowpass Filter", self)
        btn_highpass_filter = QPushButton("Highpass Filter", self)
        btn_bandpass_filter = QPushButton("Bandpass Filter", self)
        btn_reset_raw = QPushButton("Reset Raw", self)
        # Add actions or connections to filter buttons if needed
        btn_bandpass_filter.clicked.connect(self.apply_bandpass_filter)
        btn_notch_filter.clicked.connect(self.power_spectr_analys)
        btn_ica_analysis.clicked.connect(self.run_ica_analysis)
        btn_fastica.clicked.connect(self.run_fastica)
        btn_infomax.clicked.connect(self.run_infomax)
        btn_extended_infomax.clicked.connect(self.run_extended_infomax)
        btn_amica.clicked.connect(self.run_amica)
        btn_picard.clicked.connect(self.run_picard)
        btn_jade.clicked.connect(self.run_jade)
        btn_sobi.clicked.connect(self.run_sobi)
        btn_corrca.clicked.connect(self.run_corrca)
        btn_combi.clicked.connect(self.run_combi)
        btn_tdsep.clicked.connect(self.run_tdsep)
        btn_afdica.clicked.connect(self.run_afdica)
        btn_sobiwhiten.clicked.connect(self.run_sobiwhiten)
        btn_topomap_PSD.clicked.connect(self.topomap_PSD)
        btn_plot_electrode.clicked.connect(self.plot_electrode)
        btn_preprocessing_ICA.clicked.connect(self.preprocessing_ICA)
        btn_plot_ica_properties.clicked.connect(
            lambda: self.plot_ica_components_properties([18, 11, 17])
        )
        btn_plot_ica_1D.clicked.connect(self.plot_ica_components_1D)
        btn_plot_ica_topomap.clicked.connect(
            lambda: self.plot_ica_components_topomap([0, 6, 7])
        )
        btn_power_spectral_density.clicked.connect(self.power_spectral_density)
        btn_psd_channels.clicked.connect(
            lambda: self.power_spectral_density_channels(["AFz", "CPz"])
        )
        btn_lowpass_filter.clicked.connect(self.lowpass_filtering)
        btn_highpass_filter.clicked.connect(self.highpass_filtering)
        btn_bandpass_filter.clicked.connect(self.bandpass_filtering)
        btn_reset_raw.clicked.connect(self.reset_raw)

        # layout.addWidget(label)
        layout.addWidget(btn_bandpass_filter)
        layout.addWidget(btn_notch_filter)
        layout.addWidget(btn_ica_analysis)
        layout.addWidget(btn_fastica)
        layout.addWidget(btn_infomax)
        layout.addWidget(btn_extended_infomax)
        layout.addWidget(btn_amica)
        layout.addWidget(btn_picard)
        layout.addWidget(btn_jade)
        layout.addWidget(btn_sobi)
        layout.addWidget(btn_corrca)
        layout.addWidget(btn_combi)
        layout.addWidget(btn_tdsep)
        layout.addWidget(btn_afdica)
        layout.addWidget(btn_sobiwhiten)
        layout.addWidget(btn_topomap_PSD)
        layout.addWidget(btn_plot_electrode)
        layout.addWidget(btn_preprocessing_ICA)
        layout.addWidget(btn_plot_ica_properties)
        layout.addWidget(btn_plot_ica_1D)
        layout.addWidget(btn_plot_ica_topomap)
        layout.addWidget(btn_power_spectral_density)
        layout.addWidget(btn_psd_channels)
        layout.addWidget(btn_lowpass_filter)
        layout.addWidget(btn_highpass_filter)
        layout.addWidget(btn_bandpass_filter)
        layout.addWidget(btn_reset_raw)
        layout.addStretch(20)

    # implements stuff
    def power_spectr_analys():
        # power_spectral_density_PSD()
        pass

    def run_fastica(self):
        pass

    def run_infomax(self):
        pass

    def run_extended_infomax(self):
        pass

    def run_amica(self):
        pass

    def run_picard(self):
        pass

    def run_jade(self):
        pass

    def run_sobi(self):
        pass

    def run_corrca(self):
        pass

    def run_combi(self):
        pass

    def run_tdsep(self):
        pass

    def run_afdica(self):
        pass

    def run_sobiwhiten(self):
        pass

    def apply_bandpass_filter(self):
        pass

    def run_ica_analysis(self):
        # preprocessing_ICA()
        pass

    def topomap_PSD(self):
        pass

    def plot_electrode(self):
        pass

    def preprocessing_ICA(self):
        pass

    def plot_ica_components_properties(self, components=[18, 11, 17]):
        pass

    def plot_ica_components_1D(self):
        pass

    def plot_ica_components_topomap(self, components=[0, 6, 7]):
        pass

    def power_spectral_density(self):
        pass

    def power_spectral_density_channels(self, picks=["AFz", "CPz"]):
        pass

    def lowpass_filtering(self):
        pass

    def highpass_filtering(self):
        pass

    def bandpass_filtering(self):
        pass

    def reset_raw(self):
        pass


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
            QToolBar { background-color:  #313131;
                                 }
            QToolBar:hover { background-color: #313131;
                             color:#bebb48 ; }
            QPushButton {
               
                color: black;
               
            }
            """
        )

        # layout = QVBoxLayout(self)

        layout = QVBoxLayout()
        # Buttons for MNE filters and ICA analysis

        # layout.addWidget(label)

        layout.addStretch(20)

        # implements stuff
        # Buttons for MNE filters and ICA analysis
        # btn_topomap_PSD = QPushButton("Topomap PSD", self)
        # btn_plot_electrode = QPushButton("Plot Electrode", self)
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
        btn_plot_ica_properties.triggered.connect(
            lambda: self.parent().my_eeg.plot_ica_components_properties(9)
        )
        btn_plot_ica_1D.triggered.connect(
            lambda: self.parent().my_eeg.plot_ica_components_1D()
        )
        btn_plot_ica_topomap.triggered.connect(
            lambda: self.parent().my_eeg.plot_ica_components_topomap([0, 6, 7])
        )
        btn_power_spectral_density.triggered.connect(self.power_spectral_density)
        btn_psd_channels.triggered.connect(
            lambda: self.parent().my_eeg.power_spectral_density_channels(["AFz", "CPz"])
        )
        btn_lowpass_filter.triggered.connect(self.lowpass_filtering)
        btn_highpass_filter.triggered.connect(self.highpass_filtering)
        btn_bandpass_filter.triggered.connect(self.bandpass_filtering)
        # btn_reset_raw.clicked.connect(self.reset_raw)

        # layout.addWidget(label)

        # layout.addWidget(btn_topomap_PSD)
        # layout.addWidget(btn_plot_electrode)
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
    def power_spectr_analys():
        # power_spectral_density_PSD()
        pass

    def apply_bandpass_filter(self):
        pass

    def run_ica_analysis(self):
        # preprocessing_ICA()
        pass

    def topomap_PSD(self):
        pass

    def plot_electrode(self):
        pass

    def preprocessing_ICA(self):
        self.parent().dock.show()

    # self.parent().my_raw.preprocessing_ICA()

    def plot_ica_components_1D(self):
        pass

    def power_spectral_density(self):
        pass

    def power_spectral_density_channels(self, picks=["AFz", "CPz"]):
        pass

    def lowpass_filtering(self):
        pass

    def highpass_filtering(self):
        pass

    def bandpass_filtering(self):
        pass

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
        self.n_components_spinbox = QSpinBox()
        self.n_components_spinbox.setValue(20)

        self.random_state_spinbox = QSpinBox()
        self.random_state_spinbox.setValue(97)

        self.max_iter_spinbox = QSpinBox()
        self.max_iter_spinbox.setValue(800)
        layout = QVBoxLayout()
        # layout.setContentsMargins(20, 10, 20, 10)
        central_widget.setLayout(layout)

        self.setStyleSheet(
            """
            QSpinBox {
    background-color:black;
    color:white;
    }"""
        )

        layout.addWidget(QLabel("n_components:"))
        layout.addWidget(self.n_components_spinbox)

        layout.addWidget(QLabel("random_state:"))
        layout.addWidget(self.random_state_spinbox)

        layout.addWidget(QLabel("max_iter:"))
        layout.addWidget(self.max_iter_spinbox)
        apply_button = QPushButton("Apply")
        apply_button.clicked.connect(self.ok_clicked)
        apply_button.setStyleSheet(
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
        layout.addWidget(apply_button)

        self.setLayout(layout)

    def ok_clicked(self):
        n_components = self.n_components_spinbox.value()
        random_state = self.random_state_spinbox.value()
        max_iter = self.max_iter_spinbox.value()
        self.parent().my_eeg.preprocessing_ICA(n_components, random_state, max_iter)

        self.hide()
