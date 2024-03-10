import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from generated_ttt import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui

class TaskApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('/home/csl-r/Pictures/test.png'))
        # Set window opacity
        self.setWindowOpacity(1)  # Set the opacity value as desired (0.5 for 50% transparency)

        # Initialize total tasks count
        self.total_tasks = 0

        # Load tasks from file
        self.load_tasks()

        self.load_city()
        
        # Connect returnPressed signal of the QLineEdit to add_place function
        self.ui.lineEdit_2.returnPressed.connect(self.add_place)

        # Connect button box accepted and rejected signals to appropriate slots
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        # Connect return pressed event of the QLineEdit to a function
        self.ui.lineEdit.returnPressed.connect(self.add_task)
        
        # Connect list item double click event to a function
        self.ui.listWidget.itemDoubleClicked.connect(self.delete_task)

        self.ui.listWidget_2.itemDoubleClicked.connect(self.delete_city)

        # Update LCD display
        self.update_lcd()

        # Connect textChanged signal of the QLineEdit to add_place function


        self.reminder_dates = [QtCore.QDate.fromString(date_str, "yyyy-MM-dd") for date_str in ["2024-03-15", "2024-03-23", "2024-03-21", "2024-03-18"]]

        # Connect QCalendarWidget's clicked signal to a custom slot
        self.ui.calendarWidget.clicked.connect(self.custom_slot)

        self.ui.tabWidget.setCurrentIndex(0)

        # Initialize calendar widget text formats
        self.init_calendar_formats()

    def init_calendar_formats(self):
        # Initialize text formats for all dates in the calendar
        default_format = self.get_default_format()
        highlight_format = self.get_highlight_format()
        
        for date in self.reminder_dates:
            self.ui.calendarWidget.setDateTextFormat(date, highlight_format)

    def custom_slot(self):
        # Get the selected date from the QCalendarWidget
        selected_date = self.ui.calendarWidget.selectedDate()
        
        # Check if the selected date is in the list of reminder dates
        if selected_date in self.reminder_dates:
            # Toggle highlighting for selected date
            if self.ui.calendarWidget.dateTextFormat(selected_date).background().color() == QtGui.QColor('green'):
                self.ui.calendarWidget.setDateTextFormat(selected_date, self.get_default_format())
            else:
                self.ui.calendarWidget.setDateTextFormat(selected_date, self.get_highlight_format())

    def get_default_format(self):
        # Get the default text format for dates
        default_format = QtGui.QTextCharFormat()
        return default_format

    def get_highlight_format(self):
        # Create a text format to highlight dates
        highlight_format = QtGui.QTextCharFormat()
        highlight_format.setBackground(QtGui.QColor('green'))
        return highlight_format

        

    def accept(self):
        # Save tasks to file before closing
        self.save_tasks()
        self.save_city()
        # Close the window when OK button is pressed
        self.close()

    def reject(self):
        # Handle rejected signal from button box
        pass

    def add_task(self):
        # Get the task text from the QLineEdit
        task_text = self.ui.lineEdit.text()

        if task_text:
            # Add the task to the QListWidget
            self.ui.listWidget.addItem(task_text)
            # Clear the QLineEdit
            self.ui.lineEdit.clear()
            # Increment total tasks count
            self.total_tasks += 1
            # Update LCD display
            self.update_lcd()

    def delete_task(self, item):
        # Remove the selected item from the QListWidget
        self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
        # Decrement total tasks count
        self.total_tasks -= 1
        # Update LCD display
        self.update_lcd()

    def delete_city(self, item):
        # Remove the selected item from the QListWidget
        self.ui.listWidget_2.takeItem(self.ui.listWidget_2.row(item))
        # Decrement total tasks count

    def update_lcd(self):
        # Display the total number of tasks in the LCD display
        self.ui.lcdNumber.display(self.total_tasks)

    def save_tasks(self):
        # Open the file in write mode and save tasks
        with open('/home/csl-r/Desktop/ttt/ttt/tasks.txt', 'w') as f:
            for index in range(self.ui.listWidget.count()):
                task_text = self.ui.listWidget.item(index).text()
                f.write(task_text + '\n')

    def load_tasks(self):
        # Open the file in read mode and load tasks
        try:
            with open('/home/csl-r/Desktop/ttt/ttt/tasks.txt', 'r') as f:
                tasks = f.readlines()
                for task in tasks:
                    self.ui.listWidget.addItem(task.strip())
                    self.total_tasks += 1
        except FileNotFoundError:
            pass



    def save_city(self):
        # Open the file in write mode and save tasks
        with open('/home/csl-r/Desktop/ttt/ttt/city.txt', 'w') as f:
            for index in range(self.ui.listWidget_2.count()):
                task_text = self.ui.listWidget_2.item(index).text()
                f.write(task_text + '\n')

    def load_city(self):
        # Open the file in read mode and load tasks
        try:
            with open('/home/csl-r/Desktop/ttt/ttt/city.txt', 'r') as f:
                tasks = f.readlines()
                for task in tasks:
                    self.ui.listWidget_2.addItem(task.strip())
        except FileNotFoundError:
            pass

    def add_place(self):
        # Add the entered place to the QListWidget_2
        task_text = self.ui.lineEdit_2.text()
        if task_text:
            # Add the task to the QListWidget
            self.ui.listWidget_2.addItem(task_text)
            # Clear the QLineEdit
            self.ui.lineEdit_2.clear()

            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskApp()
    window.show()
    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        app.exit()

