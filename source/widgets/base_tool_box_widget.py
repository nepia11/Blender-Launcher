from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolBox

from widgets.base_list_widget import BaseListWidget


class BaseToolBoxWidget(QToolBox):
    def __init__(self, parent=None):
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.currentChanged.connect(self.current_changed)

    def add_list_widget(self, name):
        list_widget = BaseListWidget()
        self.addItem(list_widget, QIcon(
            ":resources/icons/page_closed.svg"), name)

        return list_widget

    def current_changed(self, index):
        icon_page_opened = QIcon(":resources/icons/page_opened.svg")
        icon_page_closed = QIcon(":resources/icons/page_closed.svg")

        for i in range(self.count()):
            if i != index:
                self.setItemIcon(i, icon_page_closed)

        self.setItemIcon(index, icon_page_opened)
