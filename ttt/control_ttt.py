import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from generated_ttt import Ui_Dialog
from PyQt5 import QtCore
from PyQt5 import QtCore
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtWidgets import QAction


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


        self.reminder_dates = [QtCore.QDate.fromString(date_str, "yyyy-MM-dd") for date_str in ["2024-01-01",
                                                                                                "2024-01-05",
                                                                                                "2024-01-07",
                                                                                                "2024-01-29",
                                                                                                "2024-01-31",
                                                                                                "2024-02-27",
                                                                                                "2024-03-12",
                                                                                                "2024-04-12", 
                                                                                                "2024-04-13",
                                                                                                #Akhaand??
                                                                                                "2024-04-19",
                                                                                                "2024-04-23",
                                                                                                "2024-04-29",
                                                                                                "2024-05-03", 
                                                                                                "2024-05-13", 
                                                                                                #Topperr??
                                                                                                "2024-05-21",
                                                                                                "2024-06-25",
                                                                                                #Turkeyy??
                                                                                                "2024-08-15",
                                                                                                "2024-08-25",
                                                                                                #nagraj??
                                                                                                "2024-09-22",
                                                                                                "2024-10-18",                                                                                                
                                                                                                "2024-11-15",
                                                                                                "2024-11-27",
                                                                                                "2024-06-25",
                                                                                                                                                                                             
                                                                                                ]]

        # Connect QCalendarWidget's clicked signal to a custom slot
        self.ui.calendarWidget.clicked.connect(self.custom_slot)

        self.ui.tabWidget.setCurrentIndex(0)

        # Initialize calendar widget text formats
        self.init_calendar_formats()

        # self.setup_dark_mode()


    def init_calendar_formats(self):
        # Initialize text formats for all dates in the calendar
        default_format = self.get_default_format()
        highlight_format = self.get_highlight_format()
        
        for date in self.reminder_dates:
            self.ui.calendarWidget.setDateTextFormat(date, highlight_format)

    def custom_slot(self):
        # Get the selected date from the QCalendarWidget
        selected_date = self.ui.calendarWidget.selectedDate()

        birthday_info = {
            QtCore.QDate(2024, 1, 1): "Sharduul's Birthday",
            QtCore.QDate(2024, 1, 5): "Dikki's Birthday",
            QtCore.QDate(2024, 1, 7): "Scootyy's Birthday",
            QtCore.QDate(2024, 1, 29): "Nitishh's Birthday",
            QtCore.QDate(2024, 1, 31): "Reenii's Birthday",
            QtCore.QDate(2024, 2, 27): "Aashiii's Birthday",
            QtCore.QDate(2024, 3, 12): "Jyooooti's Birthday",
            QtCore.QDate(2024, 4, 12): "Papaa's Birthday",
            QtCore.QDate(2024, 4, 13): "Kauwaa's Birthday",
            QtCore.QDate(2024, 4, 19): "Meeeee's Birthday",
            QtCore.QDate(2024, 4, 23): "Anniversayy ",
            QtCore.QDate(2024, 4, 29): "Maaami Birthday",
            QtCore.QDate(2024, 5, 3): "Doreeemon's Birthday",
            QtCore.QDate(2024, 5, 13): "Mammmiii's Birthday",
            QtCore.QDate(2024, 5, 21): "Manaswitii's Birthday",
            QtCore.QDate(2024, 6, 25): "Diiiiiiii's Birthday",
            QtCore.QDate(2024, 8, 15): "Faainaa's Birthday",
            QtCore.QDate(2024, 8, 25): "Gauravvv's Birthday",
            QtCore.QDate(2024, 10, 18): "Sakeeeet's Birthday",
            QtCore.QDate(2024, 9, 22): "Princuuuu's Birthday",
            QtCore.QDate(2024, 11, 15): "Lulwaa's Birthday",
            QtCore.QDate(2024, 11, 27): "Sardarrrr's Birthday",

            # Add more birthdays as needed
        }
        if selected_date in birthday_info:
            tooltip_text = birthday_info[selected_date]
            
            # Calculate position for tooltip near the calendar widget
            tooltip_position = self.ui.calendarWidget.mapToGlobal(self.ui.calendarWidget.pos())
            tooltip_position.setX(tooltip_position.x() - 590 )  # Adjust X position
            tooltip_position.setY(tooltip_position.y()  + 20 )  # Keep Y position

            QToolTip.showText(tooltip_position, tooltip_text)

    def get_default_format(self):
        # Get the default text format for dates
        default_format = QTextCharFormat()
        return default_format

    def get_highlight_format(self):
        # Create a text format to highlight dates with green color
        highlight_format = QTextCharFormat()
        highlight_format.setBackground(QColor('green'))
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

    # def setup_dark_mode(self):
    #     self.dark_mode = False
    #     self.toggle_action = QAction("Dark Mode", self)
    #     self.toggle_action.setCheckable(True)
    #     self.toggle_action.triggered.connect(self.toggle_dark_mode)
    #     self.menuBar().addAction(self.toggle_action)

    # def toggle_dark_mode(self):
    #     self.dark_mode = not self.dark_mode
    #     if self.dark_mode:
    #         self.setStyleSheet("background-color: #333; color: white;")
    #     else:
    #         self.setStyleSheet("")  # Reset stylesheet to default


    def save_tasks(self):
        # Open the file in write mode and save tasks
        with open('tasks.txt', 'w') as f:
            for index in range(self.ui.listWidget.count()):
                task_text = self.ui.listWidget.item(index).text()
                f.write(task_text + '\n')

    def load_tasks(self):
        # Open the file in read mode and load tasks
        try:
            with open('tasks.txt', 'r') as f:
                tasks = f.readlines()
                for task in tasks:
                    self.ui.listWidget.addItem(task.strip())
                    self.total_tasks += 1
        except FileNotFoundError:
            pass
    

    def save_city(self):
        # Open the file in write mode and save tasks
        with open('city.txt', 'w') as f:
            for index in range(self.ui.listWidget_2.count()):
                task_text = self.ui.listWidget_2.item(index).text()
                f.write(task_text + '\n')

    def load_city(self):
        # Open the file in read mode and load tasks
        try:
            with open('city.txt', 'r') as f:
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

