import sys

from functools import partial
from PyQt6 import QtWidgets, QtGui
from .widgets import MainWindow, SearchItem, ActiveItem

from .. import recipes
from ..facility import facilities
from ..base import Materials


def start_gui():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    window.setWindowTitle("DSP recipe calculator")
    window.resize(1100, 640)
    ui = MainWindow(window)

    all_recipes = {
        k.replace("_", " ").capitalize(): v
        for k, v in recipes.__dict__.items()
        if isinstance(v, recipes.Recipe)
    }
    recipe_widgets = [SearchItem(recipe) for recipe in all_recipes]
    for widget in recipe_widgets:
        ui.search_items.addWidget(widget)
    ui.search_items.addStretch()

    def filter_recipes(text):
        for i in range(ui.search_items.count() - 1):
            widget = ui.search_items.itemAt(i).widget()
            widget.setVisible(text.lower() in widget.search_name)

    ui.search_edit.textChanged.connect(filter_recipes)

    active_widgets = [
        ActiveItem(name, [f.name for f in facilities[recipe.facility]])
        for name, recipe in all_recipes.items()
    ]

    mono_font = QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.SystemFont.FixedFont)

    def update_calcs(*args, **kwargs):
        in_ = Materials()
        out = Materials()
        for active in active_widgets:
            if not active.isVisible():
                continue

            recipe = all_recipes[active.recipe_name]
            count = active.multiplier_scroll.value()
            f_ix = active.select_facility.currentIndex()
            facility = facilities[recipe.facility][f_ix]
            multiplier = count * facility.efficiency / recipe.secs
            in_ += recipe.in_ * multiplier
            out += recipe.out * multiplier

        for _ in range(ui.needs_items.count()):
            item = ui.needs_items.itemAt(0)
            widget = item.widget()
            if widget is None:
                ui.needs_items.removeItem(item)
                continue
            widget.setVisible(False)
            ui.needs_items.removeWidget(widget)

        for _ in range(ui.produces_items.count()):
            item = ui.produces_items.itemAt(0)
            widget = item.widget()
            if widget is None:
                ui.produces_items.removeItem(item)
                continue
            widget.setVisible(False)
            ui.produces_items.removeWidget(widget)

        diff = out - in_
        for name, count in diff.items():
            if count > 0:
                label = QtWidgets.QLabel(f"{count:5.2f} {name.name} / sec")
                label.setFont(mono_font)
                ui.produces_items.addWidget(label)
            else:
                label = QtWidgets.QLabel(f"{-count:5.2f} {name.name} / sec")
                label.setFont(mono_font)
                ui.needs_items.addWidget(label)

        ui.needs_items.addStretch()
        ui.produces_items.addStretch()

    for widget in active_widgets:
        ui.active_items.addWidget(widget)
        widget.setVisible(False)
        widget.multiplier_scroll.valueChanged.connect(update_calcs)
        widget.select_facility.currentIndexChanged.connect(update_calcs)
    ui.active_items.addStretch()

    def deactivate_recipe(_, self: ActiveItem):
        self.setVisible(False)
        update_calcs()

    def activate_recipe(_, active: ActiveItem):
        active.setVisible(True)
        update_calcs()

    for search, active in zip(recipe_widgets, active_widgets):
        search.add_button.clicked.connect(partial(activate_recipe, active=active))
        active.remove_button.clicked.connect(partial(deactivate_recipe, self=active))

    def clear_recipes(_):
        for widget in active_widgets:
            widget.setVisible(False)
        update_calcs()

    ui.clear_active_button.clicked.connect(clear_recipes)

    window.show()
    return app.exec()
