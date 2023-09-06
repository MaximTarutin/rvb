import sys
from PySide6.QtWidgets import (QApplication, QMessageBox, QTextBrowser, QWidget, QPushButton)
from PySide6.QtCore import (Qt, QSize)

class HelpWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowModality(Qt.ApplicationModal)
        self.textBrowser = QTextBrowser(self)
        self.button_ok = QPushButton(self)
        self.button_ok.clicked.connect(self.__close_help)

# ----------------------------------- Инициализация ------------------------------------------

    def __init(self,w,h):
        self.show()
        self.resize(w, h)
        self.setMaximumSize(QSize(w, h))
        self.setMinimumSize(QSize(w, h))
        self.textBrowser.resize(w, h-40)
        self.button_ok.resize(80, 30)
        self.button_ok.setText("ОК")
        x1 = w/2-40
        y1 = h-35
        self.button_ok.move(x1, y1)
        self.textBrowser.show()
        self.button_ok.show()
        self.textBrowser.clear()

# ----------------------------------- О программе --------------------------------------------

    def about(self):
        self.__init(600,600)
        self.setWindowTitle("О программе")
        self.textBrowser.append('''<center><b><font color="blue" size="7">Программа РВБ</font></b></center></div>
                                   <font color="green" size="5"><div><br>Версия программы: 1.2
                                   <br>Язык разработки: Python 3.11<br>Фреймворк: Qt 6.4.3<br>Библиотека: PySide6
                                   <br><br></font><font color="black" size="5">Программа представляет собой рабочее
                                   место старшего электромеханика Регионального центра связи РЖД. Состоит из трёх 
                                   модулей:<br>1) Учет рабочего времени<br>2) Устранение замечаний<br>3) Планирование 
                                   работ</font><br><br><font size="5" color="red">Программирование: старший 
                                   элетромеханик Сосногорского регионального центра связи Ярославской дирекции связи - 
                                   Тарутин Максим Александрович</font><br><br><br><font size="5" color="blue">
                                   <center><b>Воркута 2023 год</b></center></font>''')

# ------------------------------- справко о главном модуле ------------------------------------------

    def help_main_window(self):
        self.__init(600,400)
        self.setWindowTitle("Главный модуль")
        self.textBrowser.append('''<font color="black" size="4">1.   Для начала работы с 
        программой необходимо придумать пароль администратора, который необходимо запомнить. В случае утери пароля 
        восстановить можно только направив файл database.db на электронный адрес mtarut@mail.ru для разблокировки.
        Позднее изменить пароль возможно в меню "Редакторы -> Изменить пароль администратора".
        <br><br>2. При первом запуске необходимо заполнить базу данных сотрудниками бригады, а также заполнить станции и
        перегоны на которых будут планироваться и производится работы. Для этого необходимо войти в режим 
        администратора: "Сервис -> Режим администратора". Ввести пароль. Затем зайти в меню "Редакторы -> Сотрудники"
        или "Редакторы -> Станции и перегоны" соответственно, для заполнения данных
        <br><br>3. Программа состоит из трех модулей : "Учет рабочего времени", "Устранение замечаний" и "Планирование 
        работ" доступ к которым осуществляется нажатием соответствующей кнопки на главном экране, либо через меню 
        "Сервис" и выбора соответствующего подменю</font>''')

# ---------------------------------- Справка модуля учет рабочего времени ---------------------------------

    def help_timetracking(self):
        self.__init(600,650)
        self.setWindowTitle("Модуль учета рабочего времени")
        self.textBrowser.append('''<font color="black" size="4">1. Список работников формируется из базы данных, 
        добавлять или удалять сотрудников можно через меню "Редакторы -> Сотрудники" в режиме администратора.
        <br><br>2. Данные вводятся в соответствующие ячейки в режиме администратора, количество отработанных часов 
        в месяц просчитываются автоматически и вносятся в графу "факт", чтобы получить количество отгулов, необходимо 
        внести норму часов в графе "норма" при этом количество часов отгулов просчитается автоматически.<br><br>
        3. Если необходимо произвести корректировку отработанного времени, необходимо открыть скрытый столбец "корр"
        для этого в режиме администратора необходимо установить галочку в чекбоксе "Корректировка времени" после этого
        внести нужные данные в столбец "корр", отгулы при этом просчитаются автоматически.<br><br>
        4. В ячейки можно вносить не только часы, но и причины отсутствия: "о" - отпуск, "п" - прогул, "в" - выходной,
        "к" - командировка, "у" - учеба, "н" - отгул, "б" - больничный. Можно использовать как заглавные, так и
        строчные буквы, при внесении причины отсутствия ячейка закрасится определенным цветом 
        (подсказка - под таблицей)<br><br>
        5. В режиме пользователя двойной клик по ячейке с отработанными часами вызовет окно в котором будет выведена
        информация о выполненных работах сотрудника на указанную дату, при уславии что данные введены в модуле 
        планирования работ.<br><br> 
        6. Для просмотра количества часов переработки или недоработки у сотрудников необходимо
        нажать кнопку "Отгулы", либо выбрать меню "Сервис -> Сводная таблица отгулов"</font>''')

# --------------------------- Справка редактор сотрудников и станций ------------------------------------------

    def help_worker(self):
        self.__init(600, 250)
        self.setWindowTitle("Редактор сотрудников и станций")
        self.textBrowser.append('''<font color="black" size="4">1. Для добавления нового сотрудника (модуль "Редактор 
        сотрудников") или станции (модуль "Редактор станций и перегонов") необходимо нажать соответствующую кнопку
         "Добавить ...". В редакторе появится пустая строка, которую можно заполнить необходимыми данными, в редакторе
         сотруднников необходимо заполнять все поля иначе данные не будут занесены в базу данных <br><br>
         2. Для удаления данных из базы, необходимо выделить нужные строки и нажать кнопку "Удалить..."</font>''')

# -------------------------------- Справка планировщика работ -----------------------------------------------
    def help_plan(self):
        self.__init(600, 400)
        self.setWindowTitle("Модуль планировщик работ")
        self.textBrowser.append('''<font color="black" size="4">1. Модуль планировщика имеет возможность просматривать
        выполненые работы сотрудниками бригады на указанную дату. Если необходимо просмотреть работы за определенный 
        период, то необходимо нажать чекбокс "Выбор по периоду" и обозначить период.<br><br>
        2. Имеется возможность выборки по фильтру, для этого необходимо выбрать дату (период), сотрудника, и/или станцию
        <br><br>3. Для внесения данных по работам необходимо нажать кнопку "Редактор" в режиме администратора<br><br>
        4. Для удаления не актуальных записей необходимо выбрать не нужные строки и удалить их с помощью кнопки 
        "Удалить" в режиме администратора <br><br>
        5. В редакторе заполняются все поля и нажимается кнопка "Добавить" для добавления данных в базу</font>''')

# -------------------------------- Справка форма ввода новых замечаний -----------------------------------------------
    def help_new_comments(self):
        self.__init(600, 340)
        self.setWindowTitle("Модуль ввода новых замечаний")
        self.textBrowser.append('''<font color="black" size="4">1. Форма служит для ввода в базу данных новых замечаний
        различных уровней проверок, в базу кроме замечаний можно вносить планируемые работы с указанием срока выполнения
        для последующего их контроля. <br><br>
        2. Форма состоит из нескольких полей, которые необходимо заполнить. <br><br>
        3. Все поля являются обязательными для заполнения, в противном случае данные в базу сохранены не будут, и 
        появится соответствующее сообщение об ошибке.<br><br>
        4. После заполнения всех полей, для созранения данных, необходимо нажать кнопку "Добавить замечание в базу"<br>
        <br> 5. Для возврата из формы служт кнопка "Вернуться назад"</font>''')

# --------------------------------- Закрыть модуль --------------------------------------------------------

    def __close_help(self):
        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    mywindow = HelpWindow()
    mywindow.show()
    sys.exit(app.exec()) 
