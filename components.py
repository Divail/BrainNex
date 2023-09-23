from PyQt6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLabel,
    QFrame,
    QToolBar,
    QDockWidget,
    QMenuBar,
)
from PyQt6.QtGui import QAction

from PyQt6.QtCore import Qt, QSize
import qtawesome as qta


class LeftSideMenu(QMenuBar):
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
            # Show
            self.parent().left_menu.show()
        else:
            # Hide
            self.parent().left_menu.hide()

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
