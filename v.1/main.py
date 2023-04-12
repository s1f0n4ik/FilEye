#!/urs/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget
from PyQt5 import uic, QtWidgets
import sys
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sqlite3


class MainFuncWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.start()
        self.set()
        self.count = 0

    def start(self):
        self.ui = uic.loadUi("Main_window.ui")
        self.ui.show()
        self.serial = QSerialPort()
        self.serial.setBaudRate(19200)  # Задаём скорость (Как на Arduino)

    def on_open(self):
        self.serial.setPortName("COM3")
        self.serial.open(QIODevice.ReadWrite)

    def on_close(self):
        self.serial.close()

    def write_serial(self, data: list):
        txs = ""
        for value in data:
            txs += str(value)
            txs += ","
        txs = txs[:-1]
        txs += ";\n"
        self.serial.write(txs.encode())

    def click_off(self):
        self.write_serial([2, 0, 0, 0])

    def click_on(self):
        self.write_serial([2, 1, 0, 0])

    def frequency_control_slider(self):
        self.write_serial([1, self.ui.freq_dial.value(), 0, 0])
        self.ui.spinBox.setValue(self.ui.freq_dial.value())

    def frequency_control_spinbox(self):
        self.write_serial([1, self.ui.spinBox.value(), 0, 0])
        self.ui.freq_dial.setValue(self.ui.spinBox.value())

    def rgb_control(self):
        self.write_serial([0, self.ui.red_slider.value(), self.ui.green_slider.value(), self.ui.blue_slider.value()])
        self.ui.spinBox_red.setValue(self.ui.red_slider.value())
        self.ui.spinBox_green.setValue(self.ui.green_slider.value())
        self.ui.spinBox_blue.setValue(self.ui.blue_slider.value())

    def rgb_control_spinbox_red(self):
        self.write_serial([0, self.ui.spinBox_red.value(), self.ui.spinBox_green.value(), self.ui.spinBox_blue.value()])
        self.ui.red_slider.setValue(self.ui.spinBox_red.value())

    def rgb_control_spinbox_green(self):
        self.write_serial([0, self.ui.spinBox_red.value(), self.ui.spinBox_green.value(), self.ui.spinBox_blue.value()])
        self.ui.green_slider.setValue(self.ui.spinBox_green.value())

    def rgb_control_spinbox_blue(self):
        self.write_serial([0, self.ui.spinBox_red.value(), self.ui.spinBox_green.value(), self.ui.spinBox_blue.value()])
        self.ui.blue_slider.setValue(self.ui.spinBox_blue.value())

    def back_start_win(self):
        start_w = StartWindow()
        widget.addWidget(start_w)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        self.ui.close()

    def set_count(self):
        self.count += 1
        self.making_points()
        if 7 - self.count == 0:
            self.ui.point_label.setText("Всё!")
        elif 7 - self.count < 0:
            self.ui.point_label.setText("Хватит! Тормози!")
        elif 7 - self.count == 1:
            self.ui.point_label.setText("Последняя точка!")
        else:
            self.ui.point_label.setText("Осталось точек:" + str(7 - self.count))

    def making_points(self):
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()

            if self.count <= 7:
                values = f"{self.ui.spinBox_red.value()} {self.ui.spinBox_green.value()}" \
                         f" {self.ui.spinBox_blue.value()} {self.ui.spinBox.value()}"

                if self.count == 1:
                    cursor.execute("UPDATE users SET color_and_freq1 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 2:
                    cursor.execute("UPDATE users SET color_and_freq2 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 3:
                    cursor.execute("UPDATE users SET color_and_freq3 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 4:
                    cursor.execute("UPDATE users SET color_and_freq4 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 5:
                    cursor.execute("UPDATE users SET color_and_freq5 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 6:
                    cursor.execute("UPDATE users SET color_and_freq6 = ? WHERE flag = ?", [values, 1])
                    db.commit()
                elif self.count == 7:
                    cursor.execute("UPDATE users SET color_and_freq7 = ? WHERE flag = ?", [values, 1])
                    db.commit()

        except sqlite3.Error as err:
            print("Error: ", err)
        finally:
            cursor.close()
            db.close()

    def making_graph(self):
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()
            x1 = cursor.execute("SELECT color_and_freq1 FROM users WHERE flag = ?", [1]).fetchone()
            x2 = cursor.execute("SELECT color_and_freq2 FROM users WHERE flag = ?", [1]).fetchone()
            x3 = cursor.execute("SELECT color_and_freq3 FROM users WHERE flag = ?", [1]).fetchone()
            x4 = cursor.execute("SELECT color_and_freq4 FROM users WHERE flag = ?", [1]).fetchone()
            x5 = cursor.execute("SELECT color_and_freq5 FROM users WHERE flag = ?", [1]).fetchone()
            x6 = cursor.execute("SELECT color_and_freq6 FROM users WHERE flag = ?", [1]).fetchone()
            x7 = cursor.execute("SELECT color_and_freq7 FROM users WHERE flag = ?", [1]).fetchone()
            data_values = [int(x1[0].split()[3]), int(x2[0].split()[3]), int(x3[0].split()[3]), int(x4[0].split()[3]),
                           int(x5[0].split()[3]), int(x6[0].split()[3]), int(x7[0].split()[3])]
            xs = range(len(data_values))

            y1 = cursor.execute("SELECT color_and_freq1 FROM users WHERE flag = ?", [1]).fetchone()
            y2 = cursor.execute("SELECT color_and_freq2 FROM users WHERE flag = ?", [1]).fetchone()
            y3 = cursor.execute("SELECT color_and_freq3 FROM users WHERE flag = ?", [1]).fetchone()
            y4 = cursor.execute("SELECT color_and_freq4 FROM users WHERE flag = ?", [1]).fetchone()
            y5 = cursor.execute("SELECT color_and_freq5 FROM users WHERE flag = ?", [1]).fetchone()
            y6 = cursor.execute("SELECT color_and_freq6 FROM users WHERE flag = ?", [1]).fetchone()
            y7 = cursor.execute("SELECT color_and_freq7 FROM users WHERE flag = ?", [1]).fetchone()
            data_names = [y1[0].split()[:3], y2[0].split()[:3], y3[0].split()[:3], y4[0].split()[:3], y5[0].split()[:3],
                          y6[0].split()[:3], y7[0].split()[:3]]
            fig = plt.figure()
            ax = plt.axes()
            ax.yaxis.grid(True, zorder=1)
            plt.bar([x + 0.05 for x in xs], data_values)
            plt.xticks(xs, data_names)
            canvas = FigureCanvas(fig)
            canvas.draw()
            self.ui.horizontalLayout_6.addWidget(canvas)
        except sqlite3.Error as err:
            print("Error: ", err)
        finally:
            cursor.close()
            db.close()

    def set(self):
        self.ui.open_port_but.clicked.connect(self.on_open)
        self.ui.close_port_but.clicked.connect(self.on_close)
        self.ui.freq_dial.valueChanged.connect(self.frequency_control_slider)
        self.ui.spinBox.valueChanged.connect(self.frequency_control_spinbox)
        self.ui.red_slider.valueChanged.connect(self.rgb_control)
        self.ui.green_slider.valueChanged.connect(self.rgb_control)
        self.ui.blue_slider.valueChanged.connect(self.rgb_control)
        self.ui.spinBox_red.valueChanged.connect(self.rgb_control_spinbox_red)
        self.ui.spinBox_green.valueChanged.connect(self.rgb_control_spinbox_green)
        self.ui.spinBox_blue.valueChanged.connect(self.rgb_control_spinbox_blue)
        self.ui.on_b.clicked.connect(self.click_on)
        self.ui.off_b.clicked.connect(self.click_off)
        self.ui.fix_point_button.clicked.connect(self.set_count)
        self.ui.save_button.clicked.connect(self.making_graph)
        self.ui.escape_but.clicked.connect(self.back_start_win)


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start_sw()
        self.set_sw()

    def start_sw(self):
        self.ui_sw = uic.loadUi("Start_window.ui")
        self.ui_sw.show()

    def open_main_func_win(self):
        main_func_win = MainFuncWindow()
        # noinspection PyTypeChecker
        widget.addWidget(main_func_win)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.ui_sw.close()

    def open_file_cabinet(self):
        file_cab = FileCabinetWindow()
        widget.addWidget(file_cab)
        widget.setCurrentIndex(widget.currentIndex() + 2)
        self.ui_sw.close()

    def set_sw(self):
        self.ui_sw.start_but.clicked.connect(self.open_main_func_win)
        self.ui_sw.Cabin_but.clicked.connect(self.open_file_cabinet)


class FileCabinetWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start_fc()
        self.set_fc()
        self.table_set()
        self.db_show()

    def start_fc(self):
        self.ui_fc = uic.loadUi("File_cabinet_window.ui")
        self.ui_fc.show()
        self.create_db()

    def table_set(self):
        self.ui_fc.tableWidget.setHorizontalHeaderLabels(["Фамилия", "Имя", "Отчество", "Группа", "Пол"])

    def create_db(self):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS users(
                surname VARCHAR(30),
                first_name VARCHAR(30),
                patronymic VARCHAR(30),
                platoon VARCHAR(4),
                gender VARCHAR(7),
                id INTEGER PRIMARY KEY,
                color_and_freq1 VARCHAR(20),
                color_and_freq2 VARCHAR(20),
                color_and_freq3 VARCHAR(20),
                color_and_freq4 VARCHAR(20),
                color_and_freq5 VARCHAR(20),
                color_and_freq6 VARCHAR(20),
                color_and_freq7 VARCHAR(20),
                flag INTEGER,
                count INTEGER   
            )  
            """
            cursor.executescript(query)

    def db_show(self):
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        query = "SELECT * FROM users"
        cur.execute("""SELECT COUNT(*) FROM users""")
        res = cur.fetchone()[0]
        self.ui_fc.tableWidget.setRowCount(res)
        tablerow = 0
        for row in cur.execute(query):
            self.ui_fc.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui_fc.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui_fc.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui_fc.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui_fc.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui_fc.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1

    def choose_user(self):
        cur_row = self.ui_fc.tableWidget.currentRow()
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()
            cursor.execute("SELECT flag FROM users WHERE flag = ?", [1])
            if cursor.fetchall() is None:
                cursor.execute("UPDATE users SET flag = ? WHERE id = ?", [1, cur_row + 1])
                db.commit()
                self.ui_fc.ch_label.setText("Пользователь выбран")
            else:
                cursor.execute("UPDATE users SET flag = ? WHERE flag = ?", [0, 1])
                cursor.execute("UPDATE users SET flag = ? WHERE id = ?", [1, cur_row + 1])
                db.commit()
                self.ui_fc.ch_label.setText("Пользователь выбран")

        except sqlite3.Error as err:
            print("Error: ", err)
        finally:
            cursor.close()
            db.close()

    def open_reg(self):
        reg_w = RegistrationWindow()
        widget.addWidget(reg_w)
        widget.setCurrentIndex(widget.currentIndex() + 3)
        self.ui_fc.close()

    def back_start_win(self):
        start_w = StartWindow()
        widget.addWidget(start_w)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        self.ui_fc.close()

    def set_fc(self):
        self.ui_fc.reg_but.clicked.connect(self.open_reg)
        self.ui_fc.main_but.clicked.connect(self.back_start_win)
        self.ui_fc.choose_but.clicked.connect(self.choose_user)


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start_reg()
        self.set_reg()

    def start_reg(self):
        self.ui_reg = uic.loadUi("Registration_window.ui")
        self.ui_reg.show()

    def set_reg(self):
        self.ui_reg.registration_but.clicked.connect(self.registration)
        self.ui_reg.cancel_but.clicked.connect(self.return_to_file_cab)

    def return_to_file_cab(self):
        file_cab = FileCabinetWindow()
        widget.addWidget(file_cab)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        self.ui_reg.close()

    def err_win(self):
        err_window = ErrorWindow()
        widget.addWidget(err_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def registration(self):
        user_surname = self.ui_reg.surname_edit.text()
        user_name = self.ui_reg.name_edit.text()
        user_patronymic = self.ui_reg.patronymic_edit.text()
        user_group = self.ui_reg.group_edit.text()
        user_gender = self.ui_reg.gender_edit.currentText()
        if user_surname == "" or user_name == "" or user_group == "" or user_gender == "Выбрать...":
            self.ui_reg.surname_edit.clear()
            self.ui_reg.name_edit.clear()
            self.ui_reg.patronymic_edit.clear()
            self.ui_reg.group_edit.clear()
        else:
            try:
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                cursor.execute("SELECT surname FROM users WHERE surname = ?", [user_surname])
                # (surname,)
                if cursor.fetchone() is None:
                    cursor.execute("SELECT first_name FROM users WHERE first_name = ?", [user_name])
                    if cursor.fetchone() is None:
                        cursor.execute("INSERT INTO users(surname, first_name, patronymic, platoon, gender, count) "
                                       "VALUES(?, ?, ?, ?, ?, ?)",
                                       [user_surname, user_name, user_patronymic, user_group, user_gender, 0])

                        db.commit()
                        self.return_to_file_cab()
                    else:
                        self.err_win()
                else:
                    self.err_win()
            except sqlite3.Error as err:
                print("Error: ", err)
            finally:
                cursor.close()
                db.close()


class ErrorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start_err()
        self.set_err()

    def start_err(self):
        self.ui_err = uic.loadUi("Error_window.ui")
        self.ui_err.show()

    def ok(self):
        self.ui_err.close()

    def set_err(self):
        self.ui_err.ok_but.clicked.connect(self.ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = StartWindow()
    widget = QStackedWidget()
    widget.addWidget(ex)
    widget.setFixedWidth(400)
    widget.setFixedHeight(300)
    app.exec()
