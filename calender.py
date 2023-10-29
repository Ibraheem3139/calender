import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel, QPushButton


class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calendar App')
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.show_selected_date)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(
            'font-size: 20px; font-weight: bold; color: #333; background-color: #f0f0f0; border: 1px solid #ddd; padding: 10px; border-radius: 10px;')

        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.close)
        self.quit_button.setStyleSheet(
            'background-color: #f44336; color: #fff; font-size: 16px; padding: 5px 10px; border: none; border-radius: 5px;')

        layout.addWidget(self.calendar)
        layout.addWidget(self.label)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)

    def show_selected_date(self):
        date = self.calendar.selectedDate()
        self.label.setText(date.toString("dddd, MMMM d, yyyy"))


def main():
    app = QApplication(sys.argv)
    cal_app = CalendarApp()
    cal_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
