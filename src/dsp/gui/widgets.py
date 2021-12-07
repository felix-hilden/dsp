from typing import Tuple
from PyQt6 import QtCore, QtGui, QtWidgets

title_font = QtGui.QFont()
title_font.setPointSize(14)
title_font.setBold(True)
title_font.setWeight(75)


def make_scroll_area(parent) -> Tuple[QtWidgets.QScrollArea, QtWidgets.QVBoxLayout]:
    area = QtWidgets.QScrollArea(parent)
    area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    area.setWidgetResizable(True)

    widget = QtWidgets.QWidget()
    vbox = QtWidgets.QVBoxLayout()
    vbox.setContentsMargins(3, 3, 3, 3)
    vbox.setSpacing(1)
    widget.setLayout(vbox)
    area.setWidget(widget)
    return area, vbox


def make_title(text, parent) -> QtWidgets.QLabel:
    label = QtWidgets.QLabel(text, parent)
    label.setFont(title_font)
    return label


class MainWindow:
    def __init__(self, window):
        super().__init__()

        centralwidget = QtWidgets.QWidget(window)
        top_grid = QtWidgets.QGridLayout(centralwidget)
        columns = QtWidgets.QHBoxLayout()

        left_vertical = QtWidgets.QVBoxLayout()
        needs_vertical = QtWidgets.QVBoxLayout()
        needs_label = make_title("Needs resources", centralwidget)
        needs_vertical.addWidget(needs_label)
        scroll, self.needs_items = make_scroll_area(centralwidget)
        needs_vertical.addWidget(scroll)

        left_vertical.addLayout(needs_vertical)
        produces_vertical = QtWidgets.QVBoxLayout()
        produces_label = make_title("Produces resources", centralwidget)
        produces_vertical.addWidget(produces_label)
        scroll, self.produces_items = make_scroll_area(centralwidget)
        produces_vertical.addWidget(scroll)
        left_vertical.addLayout(produces_vertical)
        columns.addLayout(left_vertical)

        center_vertical = QtWidgets.QVBoxLayout()
        center_title_horizontal = QtWidgets.QHBoxLayout()
        active_label = make_title("Active recipes", centralwidget)
        center_title_horizontal.addWidget(active_label)
        self.clear_active_button = QtWidgets.QToolButton(centralwidget)
        self.clear_active_button.setText("X")
        center_title_horizontal.addWidget(self.clear_active_button)
        center_vertical.addLayout(center_title_horizontal)
        scroll, self.active_items = make_scroll_area(centralwidget)
        center_vertical.addWidget(scroll)
        columns.addLayout(center_vertical)

        search_vertical = QtWidgets.QVBoxLayout()
        search_label = make_title("Search recipes", centralwidget)
        search_vertical.addWidget(search_label)
        self.search_edit = QtWidgets.QLineEdit(centralwidget)
        search_vertical.addWidget(self.search_edit)
        scroll, self.search_items = make_scroll_area(centralwidget)
        search_vertical.addWidget(scroll)
        columns.addLayout(search_vertical)

        columns.setStretch(0, 2)
        columns.setStretch(1, 3)
        columns.setStretch(2, 2)

        top_grid.addLayout(columns, 0, 0, 1, 1)
        window.setCentralWidget(centralwidget)


class ActiveItem(QtWidgets.QWidget):
    def __init__(self, name, facilities, parent=None):
        super().__init__(parent)
        self.recipe_name = name

        self.row = QtWidgets.QHBoxLayout()
        self.name_label = QtWidgets.QLabel(name)
        self.row.addWidget(self.name_label)
        self.multiplier_scroll = QtWidgets.QSpinBox()
        self.multiplier_scroll.setMinimum(1)
        self.multiplier_scroll.setProperty("value", 1)
        self.row.addWidget(self.multiplier_scroll)

        self.select_facility = QtWidgets.QComboBox()
        self.select_facility.addItems(facilities)
        self.select_facility.setMinimumSize(QtCore.QSize(170, 0))
        self.row.addWidget(self.select_facility)

        self.remove_button = QtWidgets.QToolButton()
        self.remove_button.setText("X")
        self.row.addWidget(self.remove_button)
        self.row.setStretch(0, 1)
        self.row.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.row)


class SearchItem(QtWidgets.QWidget):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.search_name = name.lower()

        self.row = QtWidgets.QHBoxLayout()
        self.add_button = QtWidgets.QToolButton()
        self.add_button.setText("+")
        self.row.addWidget(self.add_button)
        self.name_label = QtWidgets.QLabel(name)
        self.row.addWidget(self.name_label)

        self.row.setStretch(1, 1)
        self.row.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.row)
