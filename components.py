from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QFrame, QToolBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtGui import QIcon, QPixmap


class LeftSideMenu(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedWidth(200)
        self.setStyleSheet(
            """
            QFrame {
                background: grey;
                border-radius: 20px;

                
            }
            QPushButton {
                color: black;
            }
            """
        )

        layout = QVBoxLayout(self)

        label = QLabel("ICA Options", self)
        label.setStyleSheet("font-size: 16px; padding: 10px; color: white")

        # Buttons for MNE filters and ICA analysis
        btn_bandpass_filter = QPushButton("Apply Bandpass Filter", self)
        btn_notch_filter = QPushButton("Apply Notch Filter", self)
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
        btn_notch_filter.clicked.connect(self.apply_notch_filter)
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
        layout.addWidget(label)
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
        layout.addStretch()

    # implements stuff
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

    def apply_notch_filter(self):
        pass

    def run_ica_analysis(self):
        pass


class MyToolbar(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)

        self.button_action = QAction("Btn1", self)
        self.button_action.setStatusTip("This is your button")
        self.button_action.triggered.connect(self.onMyToolBarButtonClick)
        self.button_action.setCheckable(True)
        self.addAction(self.button_action)
        # Create the actions
        upload_action = QAction("Btn2", self)

        icon1 = QIcon.fromTheme("SP_MediaPlay")
        upload_action.setIcon(icon1)
        read_time_data_action = QAction("Btn3", self)
        icon2 = QIcon.fromTheme("SP_ArrowUp")
        read_time_data_action.setIcon(icon2)

        # Add the actions to the toolbar
        self.addAction(upload_action)
        self.addAction(read_time_data_action)
        self.addSeparator()

        self.setStyleSheet("color: #7e5302;")
        self.setFloatable(False)
        self.setMovable(False)

    def onMyToolBarButtonClick(self):
        print("Button clicked")
