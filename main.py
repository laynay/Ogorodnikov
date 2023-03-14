from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Data base')
root.attributes('-fullscreen', True)


def query_database(table, table_tree):
    # Create a database or connect to one that exists
    conn = sqlite3.connect(table)

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM {}".format(table))
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            table_tree.insert(parent='', index='end', iid=count, text='',
                              values=(record),
                              tags=('evenrow'))
        else:
            table_tree.insert(parent='', index='end', iid=count, text='',
                              values=(record),
                              tags=('oddrow'))
        # increment counter
        count += 1

    # Close our connection
    conn.close()


def close_window():
    root.destroy()


def info():
    info = Toplevel(root)
    info.title('О программе')
    info.geometry('300x200')
    info.minsize(300, 70)
    info.maxsize(300, 70)
    x = root.winfo_x()
    y = root.winfo_y()
    info.geometry("+%d+%d" % (x + 600, y + 280))
    info.wm_transient(root)
    text_label = Label(info, text='Программа создана в рамках курсового проекта Автор: Огородников Сергей Павлович, '
                                  'Группа: 082 ', wraplength=300)
    text_label.pack(anchor=CENTER, pady=15)
    info.grab_set()

def inform():
    info = Toplevel(root)
    info.title('Сведения о помещениях')
    info.geometry('300x200')
    info.minsize(300, 170)
    info.maxsize(300, 170)
    x = root.winfo_x()
    y = root.winfo_y()
    info.geometry("+%d+%d" % (x + 600, y + 280))
    info.wm_transient(root)
    conn = sqlite3.connect('rooms')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM rooms")
    records = c.fetchall()
    c.execute("SELECT COUNT(*) FROM rooms WHERE vid = 'Служебное'")
    vid = c.fetchall()
    c.execute("SELECT COUNT(*) FROM rooms WHERE vid = 'Учебное'")
    vid2 = c.fetchall()
    c.execute("SELECT COUNT(*) FROM rooms WHERE vid = 'Подсобка'")
    vid3 = c.fetchall()
    c.execute("SELECT COUNT(*) FROM rooms WHERE podrazdelenie = 'ИСТ'")
    ist = c.fetchall()
    c.execute("SELECT COUNT(*) FROM rooms WHERE podrazdelenie = 'ВМиФ'")
    vmif = c.fetchall()
    c.execute("SELECT COUNT(*) FROM rooms WHERE podrazdelenie = 'ИТиМС'")
    itims = c.fetchall()
    c.execute("SELECT COUNT(*) FROM rooms WHERE podrazdelenie = 'ИТиМ'")
    itim = c.fetchall()
    print(records[0][0])
    text_label = Label(info, text='Количество комнат в институте: {} \n Количество служебных помещений: {} \n '
                                  'Количество учебных помещений: {} \n Количество подсобных помещений: {} '
                                  '\n Количество помещений на ИСТ: {} \n Количество помещений на ВМиФ: {}'
                                  '\n Количество помещений на ИТиМС: {} \n Количество помещений на ИТиМ: {}'
                                  ''.format(records[0][0], vid[0][0], vid2[0][0], vid3[0][0], ist[0][0], vmif[0][0], itims[0][0], itim[0][0]),
                       wraplength=300)
    text_label.pack(anchor=CENTER, pady=15)
    info.grab_set()

def instr():
    instr = Toplevel(root)
    instr.title('Инструкция')
    instr.geometry('300x200')
    instr.minsize(300, 310)
    instr.maxsize(300, 310)
    x = root.winfo_x()
    y = root.winfo_y()
    instr.geometry("+%d+%d" % (x + 600, y + 280))
    instr.wm_transient(root)
    text_label = Label(instr, text='Программа работает с базой данных sqlite и разработана для учёта аудиторного '
                                   'фонда института. Для того чтобы переключаться между таблицами в нижней части'
                                   ' программы есть кнопки с названиями таблиц. В верхней панели программы размещено '
                                   'поле поиска, чтобы осуществить поиск нужно выбрать интересующий столбец в таблице,'
                                   ' затем в пустое поле ввести запрос. Для осуществления поиска в диапазне каких-то'
                                   ' чисел также нужно выбрать столбец и вписать диапазон в пустые поля рядом с кнопкой'
                                   ' "Искать по диапазону". Для того чтобы изменить значения записи или удалить её'
                                   ' кликнуть левой кнопкой мыши по записи затем в полях ниже ввести нужные значения.'
                                   ' Для того чтобы отсортировать столбец по возрастанию или убываю нужно нажать один'
                                   ' раз для сортировки по возрастанию и затем ещё раз для сортировки по убыванию.', wraplength=300)
    text_label.pack(anchor=CENTER, pady=15)
    instr.grab_set()

buttons_frame = LabelFrame(root)
buttons_frame.pack(anchor=NE, padx=20, pady=12)
info_button = Button(buttons_frame, text='О программе', command=info)
info_button.grid(row=0, column=0)
instr_button = Button(buttons_frame, text='Инструкция', command=instr)
instr_button.grid(row=0, column=1, padx=2)
exit_button = Button(buttons_frame, text='Выход', command=close_window)
exit_button.grid(row=0, column=2)


search_frame = LabelFrame(root, text="Поиск")
search_frame.pack(side=TOP, fill="x", padx=20)

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight='auto',
                fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
          background=[('selected', "#347083")])

# Создание таблицы "Комнаты"

rooms_frame = Frame(root)
rooms_frame.pack(pady=20, padx=21, expand=TRUE, fill=BOTH)

# Create a Treeview Scrollbar
tree_scrolly = Scrollbar(rooms_frame)
tree_scrolly.pack(side=RIGHT, fill=Y)
tree_scrollx = Scrollbar(rooms_frame, orient="horizontal")
tree_scrollx.pack(side=BOTTOM, fill=X)
# Create The Treeview
rooms_tree = ttk.Treeview(rooms_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                          selectmode="extended")
rooms_tree.pack(expand=TRUE, fill=BOTH)

# Configure the Scrollbar
tree_scrolly.config(command=rooms_tree.yview)
tree_scrollx.config(command=rooms_tree.xview)
# Define Our Columns
rooms_tree['columns'] = ('Ключ',
    "Комната", "Ширина (м)", "Длина (м)", "Назначение", "Вид помещения", "Высота потолков (м)", "Подразделение", "Этаж", 'Корпус')


naznachenie_frame = Frame(root)

# Create a Treeview Scrollbar
tree_scrolly = Scrollbar(naznachenie_frame)
tree_scrolly.pack(side=RIGHT, fill=Y)
tree_scrollx = Scrollbar(naznachenie_frame, orient="horizontal")
tree_scrollx.pack(side=BOTTOM, fill=X)
# Create The Treeview
naznachenie_tree = ttk.Treeview(naznachenie_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                          selectmode="extended")
naznachenie_tree.pack(expand=TRUE, fill=BOTH)

# Configure the Scrollbar
tree_scrolly.config(command=naznachenie_tree.yview)
tree_scrollx.config(command=naznachenie_tree.xview)
# Define Our Columns
naznachenie_tree['columns'] = ('Ключ', 'Назначение')

naznachenie_tree.column("#0", width=0, stretch=NO)
naznachenie_tree.heading("#0", text="", anchor=W)
naznachenie_tree.column('Назначение', anchor=CENTER, width=210, stretch=1)
naznachenie_tree.heading('Назначение', text='Назначение', anchor=CENTER, command=lambda col=1, table_tree=naznachenie_tree: sort_num(col, 'naznachenie', table_tree))
naznachenie_tree.column('Ключ',anchor=CENTER, width=410, stretch=0)
naznachenie_tree.heading("Ключ", text="Ключ", anchor=CENTER, command=lambda col=0, table_tree=naznachenie_tree: sort_num(col, 'naznachenie', table_tree))
# Create Striped Row Tags
naznachenie_tree.tag_configure('oddrow', background="white")
naznachenie_tree.tag_configure('evenrow', background="lightblue")

vid_frame = Frame(root)

# Create a Treeview Scrollbar
tree_scrolly = Scrollbar(vid_frame)
tree_scrolly.pack(side=RIGHT, fill=Y)
tree_scrollx = Scrollbar(vid_frame, orient="horizontal")
tree_scrollx.pack(side=BOTTOM, fill=X)
# Create The Treeview
vid_tree = ttk.Treeview(vid_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set,
                          selectmode="extended")
vid_tree.pack(expand=TRUE, fill=BOTH)

# Configure the Scrollbar
tree_scrolly.config(command=vid_tree.yview)
tree_scrollx.config(command=vid_tree.xview)
# Define Our Columns
vid_tree['columns'] = ('Ключ', 'Вид помещения')

vid_tree.column("#0", width=0, stretch=NO)
vid_tree.heading("#0", text="", anchor=W)
vid_tree.column('Вид помещения', anchor=CENTER, width=210, stretch=1)
vid_tree.heading('Вид помещения', text='Вид помещения', anchor=CENTER, command=lambda col=1, table_tree=vid_tree: sort_num(col, 'vid', table_tree))
vid_tree.column('Ключ',anchor=CENTER, width=410, stretch=0)
vid_tree.heading("Ключ", text="Ключ", anchor=CENTER, command=lambda col=0, table_tree=vid_tree: sort_num(col, 'vid', table_tree))
# Create Striped Row Tags
vid_tree.tag_configure('oddrow', background="white")
vid_tree.tag_configure('evenrow', background="lightblue")

# Format Our Columns and create Func
clicks = 0


def sort_num(num_column, table, table_tree):
    global clicks
    conn = sqlite3.connect('{}'.format(table))
    # Create a cursor instance
    c = conn.cursor()
    clicks += 1
    c.execute("SELECT rowid, * FROM {}".format(table))
    records = c.fetchall()
    global count
    if clicks % 2 == 0:
        n = 1
        while n < len(records):
            for i in range(len(records) - n):
                if records[i][num_column] > records[i + 1][num_column]:
                    records[i], records[i + 1] = records[i + 1], records[i]
            n += 1
    else:
        n = 1
        while n < len(records):
            for i in range(len(records) - n):
                if records[i][num_column] < records[i + 1][num_column]:
                    records[i], records[i + 1] = records[i + 1], records[i]
            n += 1

    table_tree.delete(*table_tree.get_children())

    for record in records:
        if count % 2 == 0:
            table_tree.insert(parent='', index='end', iid=count, text='',
                              values=(
                                  record),
                              tags=('evenrow'))
        else:
            table_tree.insert(parent='', index='end', iid=count, text='',
                              values=(
                                  record),
                              tags=('oddrow'))
        # increment counter
        count += 1


rooms_tree.column("#0", width=0, stretch=NO)
rooms_tree.heading("#0", text="", anchor=W)
for index, column in enumerate(rooms_tree['columns']):
    rooms_tree.column(column, anchor=CENTER, width=140)
    rooms_tree.heading(column, text=column, anchor=CENTER,
                       command=lambda col=index, table_tree=rooms_tree: sort_num(col, 'rooms', table_tree))
rooms_tree.column('Назначение', anchor=CENTER, width=210, stretch=0)
rooms_tree.heading('Назначение', text='Назначение', anchor=CENTER)
rooms_tree.column('Ключ',anchor=CENTER, width=0, stretch=0)
rooms_tree.heading("Ключ", text="Ключ", anchor=CENTER)
rooms_tree.column('Корпус', anchor=CENTER, width=100, stretch=0)
rooms_tree.heading('Корпус', text='Корпус', anchor=CENTER)

# Create Striped Row Tags
rooms_tree.tag_configure('oddrow', background="white")
rooms_tree.tag_configure('evenrow', background="lightblue")

# Создание таблицы "Кафедра"

tree_frame = Frame(root)

# Create a Treeview Scrollbar
tree_scrolly = Scrollbar(tree_frame)
tree_scrolly.pack(side=RIGHT, fill=Y)
tree_scrollx = Scrollbar(tree_frame, orient="horizontal")
tree_scrollx.pack(side=BOTTOM, fill=X)
# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scrolly.set, xscrollcommand=tree_scrollx.set)
my_tree.pack(expand=TRUE, fill=BOTH)

# Configure the Scrollbar
tree_scrolly.config(command=my_tree.yview)
tree_scrollx.config(command=my_tree.xview)
# Define Our Columns
my_tree['columns'] = ("Ключ", "Название", "Зав. Кафедрой", "Специализация")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.heading("#0", text="", anchor=W)
for index, column in enumerate(my_tree['columns']):
    my_tree.column(column, anchor=CENTER, width=400, stretch=1)
    my_tree.heading(column, text=column, anchor=CENTER,
                    command=lambda col=index, table_tree=my_tree: sort_num(col, 'kafedra', table_tree))
my_tree.column('Ключ',anchor=CENTER, width=0, stretch=0)
my_tree.heading("Ключ", text="Ключ", anchor=CENTER)
my_tree.column('Название',anchor=CENTER, width=130, stretch=0)
my_tree.heading("Название", text="Название", anchor=CENTER)
my_tree.column('Зав. Кафедрой',anchor=CENTER, width=400, stretch=0)
my_tree.heading("Зав. Кафедрой", text="Зав. Кафедрой", anchor=CENTER)


# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


# Create Rooms and Kaf Label Frame

rooms_add_frame = LabelFrame(root, text="Записи")
rooms_add_frame.pack(fill="x", padx=20)

kaf_add_frame = LabelFrame(root, text="Записи")

naznachenie_add_frame = LabelFrame(root, text="Записи")

vid_add_frame = LabelFrame(root, text="Записи")

# Create Entrys for Rooms and Kaf Label Frames

nazvan_kaf_label = Label(kaf_add_frame, text="Название")
nazvan_kaf_label.grid(row=0, column=0, padx=10, pady=10)
nazvan_kaf_entry = Entry(kaf_add_frame)
nazvan_kaf_entry.grid(row=0, column=1, pady=10, padx=10)

zavkaf_kaf_label = Label(kaf_add_frame, text="Зав. Кафедрой")
zavkaf_kaf_label.grid(row=0, column=2, padx=10, pady=10)
zavkaf_kaf_entry = Entry(kaf_add_frame, width=30)
zavkaf_kaf_entry.grid(row=0, column=3, pady=10, padx=10)

specializ_kaf_label = Label(kaf_add_frame, text="Специализация")
specializ_kaf_label.grid(row=0, column=4, padx=10, pady=10)
specializ_kaf_entry = Entry(kaf_add_frame, width=70)
specializ_kaf_entry.grid(row=0, column=5, pady=10, padx=10)


comnat_label = Label(rooms_add_frame, text="Комната")
comnat_label.grid(row=0, column=0, padx=10, pady=10)
comnat_entry = Entry(rooms_add_frame)
comnat_entry.grid(row=0, column=1, padx=10, pady=10)

shirina_label = Label(rooms_add_frame, text="Ширина (м)")
shirina_label.grid(row=0, column=2, padx=10, pady=10)
shirina_entry = Entry(rooms_add_frame)
shirina_entry.grid(row=0, column=3, padx=10, pady=10)

dlina_label = Label(rooms_add_frame, text="Длина (м)")
dlina_label.grid(row=0, column=4, padx=10, pady=10)
dlina_entry = Entry(rooms_add_frame)
dlina_entry.grid(row=0, column=5, padx=10, pady=10)

naznach_label = Label(rooms_add_frame, text="Назначение")
naznach_label.grid(row=0, column=6, padx=10, pady=10)
naznach_entry = ttk.Combobox(rooms_add_frame, width=30)
naznach_entry.grid(row=0, column=7, padx=10, pady=10)

vid_label = Label(rooms_add_frame, text="Вид помещения")
vid_label.grid(row=1, column=0, padx=10, pady=10)
vid_entry = ttk.Combobox(rooms_add_frame, width=18)
vid_entry.grid(row=1, column=1, padx=10, pady=10)


def get_vid():
    conn = sqlite3.connect('vid')
    c = conn.cursor()
    c.execute('SELECT vid FROM vid')
    vid_names = c.fetchall()
    list_vid_names = []
    for name in vid_names:
        list_vid_names += name

    vid_entry['values'] = list_vid_names

get_vid()


visota_label = Label(rooms_add_frame, text="Высота потолков (м)")
visota_label.grid(row=1, column=2, padx=10, pady=10)
visota_entry = Entry(rooms_add_frame)
visota_entry.grid(row=1, column=3, padx=10, pady=10)


podrazdel_label = Label(rooms_add_frame, text="Подразделение")
podrazdel_label.grid(row=1, column=4, padx=10, pady=10)
podrazdel_entry = ttk.Combobox(rooms_add_frame)
podrazdel_entry.grid(row=1, column=5, padx=10, pady=10)


def get_kafedra():
    conn = sqlite3.connect('kafedra')
    c = conn.cursor()
    c.execute('SELECT nazvanie FROM kafedra')
    kaf_names = c.fetchall()
    podrazdel_entry['values'] = kaf_names

get_kafedra()


etazh_label = Label(rooms_add_frame, text="Этаж")
etazh_label.grid(row=1, column=6, padx=10, pady=10)
etazh_entry = Entry(rooms_add_frame)
etazh_entry.grid(row=1, column=7, padx=10, pady=10)

korpus_label = Label(rooms_add_frame, text= "Корпус")
korpus_label.grid(row=0, column=8, padx=10, pady=10)
korpus_entry = ttk.Combobox(rooms_add_frame, values=['1', '2', '3', '4', '5'])
korpus_entry.grid(row=0, column=9, padx=10, pady=10)

naznachenie_label = Label(naznachenie_add_frame, text="Назначение")
naznachenie_label.grid(row=0, column=0, padx=10, pady=10)
naznachenie_entry = Entry(naznachenie_add_frame)
naznachenie_entry.grid(row=0, column=1, padx=10, pady=10)

vidi_label = Label(vid_add_frame, text="Вид помещения")
vidi_label.grid(row=0, column=0, padx=10, pady=10)
vidi_entry = Entry(vid_add_frame)
vidi_entry.grid(row=0, column=1, padx=10, pady=10)


def get_naznachenie():
    conn = sqlite3.connect('naznachenie')
    c = conn.cursor()
    c.execute('SELECT naznachenie FROM naznachenie')
    naznachenie_names = c.fetchall()
    list_naznach_names = []
    for name in naznachenie_names:
        list_naznach_names += name

    naznach_entry['values'] = list_naznach_names

get_naznachenie()


button_frame = LabelFrame(root, text="Таблицы")
button_frame.pack(side=BOTTOM, fill="x", padx=20, pady=10)

search_by_rooms = ttk.Combobox(search_frame, values=["Комната", "Ширина (м)", "Длина (м)", "Назначение", "Вид помещения", "Высота потолков (м)", "Подразделение",
            "Этаж", 'Корпус'], state='readonly')
search_by_rooms.grid(row=0, column=0, padx=10, pady=10)


def search(e, table, table_tree, srch_by, type):
    con = sqlite3.connect(table)
    c = con.cursor()
    global count
    stroka = srch_by.get()
    text = ["Ключ", "Комната", "Ширина (м)", "Длина (м)", "Назначение", "Вид помещения", "Высота потолков (м)", "Подразделение",
            "Этаж", "Корпус", "Название", "Зав. Кафедрой", "Специализация"]
    table_text = ['rowid', 'nomer', 'shirin', 'dlin', 'naznachenie', 'vid', 'visota', 'podrazdelenie', 'itage', 'korpus', 'nazvanie',
                  'zavkaf', 'special']
    slovar = {}
    for i in range(len(text)):
        slovar[text[i]] = table_text[i]

    operators = ('>', '<', '>=', '<=', '=')

    if type == 'search':
        if var_search.get().find('AND') == 3 or var_search.get().find('AND') == 2:
            c.execute("SELECT rowid, * FROM " + table + " WHERE " + slovar[stroka] + " BETWEEN " + var_search.get() + "")
            row = c.fetchall()
            if len(row) > 0:
                table_tree.delete(*table_tree.get_children())
                for i in row:
                    if count % 2 == 0:
                        table_tree.insert(parent='', index='end', iid=count,
                                          values=i,
                                          tags=('evenrow',))
                    else:
                        table_tree.insert(parent='', index='end', iid=count,
                                          values=i,
                                          tags=('oddrow',))
                    # increment counter
                    count += 1
            else:
                table_tree.delete(*table_tree.get_children())


        if var_search.get().find('AND') == -1:
            count = 0
            for operator in operators:
                if operator in var_search.get():
                    c.execute("SELECT rowid, * FROM " + table + " WHERE " + slovar[stroka] + " "+ var_search.get() +"")
                else:
                    count += 1
                    if count == 5:
                        c.execute(
                            "SELECT rowid, * FROM " + table + " WHERE " + slovar[
                                stroka] + " LIKE '" + var_search.get() + "%'")


            row = c.fetchall()
            if len(row) > 0:
                table_tree.delete(*table_tree.get_children())
                for i in row:
                    if count % 2 == 0:
                        table_tree.insert(parent='', index='end', iid=count,
                                          values=i,
                                          tags=('evenrow',))
                    else:
                        table_tree.insert(parent='', index='end', iid=count,
                                          values=i,
                                          tags=('oddrow',))
                    # increment counter
                    count += 1
            else:
                table_tree.delete(*table_tree.get_children())
        else:
            if var_search.get() == '':
                    table_tree.delete(*table_tree.get_children())
                    query_database(table, table_tree)
    try:
        if type == "diapaz":
            con = sqlite3.connect(table)
            c = con.cursor()
            stroka = srch_by.get()
            text = ["Ключ", "Комната", "Ширина (м)", "Длина (м)", "Назначение", "Вид помещения", "Высота потолков (м)",
                    "Подразделение",
                    "Этаж", "Корпус", "Название", "Зав. Кафедрой", "Специализация"]
            table_text = ['rowid', 'nomer', 'shirin', 'dlin', 'naznachenie', 'vid', 'visota', 'podrazdelenie', 'itage',
                          'korpus', 'nazvanie',
                          'zavkaf', 'special']
            slovar = {}
            for i in range(len(text)):
                slovar[text[i]] = table_text[i]
            value1 = spinbox_box1.get()
            value2 = spinbox_box2.get()
            c.execute("SELECT rowid, * FROM " + table + " WHERE " + slovar[stroka] + " BETWEEN " + value1 + " AND " + value2 + "")
            row = c.fetchall()
            if len(row) > 0:
                table_tree.delete(*table_tree.get_children())
                for i in row:
                    if count % 2 == 0:
                        table_tree.insert(parent='', index='end', iid=count,
                                          values=i,
                                          tags=('evenrow',))
                    else:
                        table_tree.insert(parent='', index='end', iid=count,
                                          values=i,
                                          tags=('oddrow',))
                    # increment counter
                    count += 1
            else:
                table_tree.delete(*table_tree.get_children())
    except:
        table_tree.delete(*table_tree.get_children())
        query_database(table, table_tree)


var_search = StringVar()
search_button = Entry(search_frame, textvariable=var_search)
search_button.grid(row=0, column=2, padx=10, pady=10)
spinbox_button = Button(search_frame, text="Искать по диапазону")
spinbox_button.grid(row=0, column=4)
spinbox_button.bind("<ButtonRelease-1>",
                   lambda event, table='rooms', table_tree=rooms_tree, srch_by=search_by_rooms, type='diapaz': search(event, table,
                                                                                                       table_tree,
                                                                                                       srch_by, type))
spinbox_frame = Frame(search_frame)
spinbox_label = Label(spinbox_frame, text='Выбрать диапазон')
spinbox_label.grid(row=1, column=0, pady=10)
spinbox_box1 = Spinbox(spinbox_frame,width=5)
spinbox_box1.grid(row=1, column=1, padx=10)
spinbox_box2 = Spinbox(spinbox_frame, width=5)
spinbox_box2.grid(row=1, column=2, pady=10, padx=0)
search_button.bind("<Return>",
                   lambda event, table='rooms', table_tree=rooms_tree, srch_by=search_by_rooms, type='search': search(event, table,
                                                                                                       table_tree,
                                                                                                       srch_by, type))


def clear_entries():
    comnat_entry.delete(0, END)
    shirina_entry.delete(0, END)
    dlina_entry.delete(0, END)
    naznach_entry.delete(0, END)
    vid_entry.delete(0, END)
    visota_entry.delete(0, END)
    podrazdel_entry.delete(0, END)
    etazh_entry.delete(0, END)
    nazvan_kaf_entry.delete(0, END)
    zavkaf_kaf_entry.delete(0, END)
    specializ_kaf_entry.delete(0, END)
    korpus_entry.delete(0, END)
    naznachenie_entry.delete(0, END)
    vidi_entry.delete(0, END)


def select_record_rooms(e):
    try:
        clear_entries()

        selected = rooms_tree.focus()
        values = rooms_tree.item(selected, 'values')

        comnat_entry.insert(0, values[1])
        shirina_entry.insert(0, values[2])
        dlina_entry.insert(0, values[3])
        naznach_entry.insert(0, values[4])
        vid_entry.insert(0, values[5])
        visota_entry.insert(0, values[6])
        podrazdel_entry.insert(0, values[7])
        etazh_entry.insert(0, values[8])
        korpus_entry.insert(0, values[9])
    except:
        None


def select_record_kaf(e):
    try:
        clear_entries()

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')

        nazvan_kaf_entry.insert(0, values[1])
        zavkaf_kaf_entry.insert(0, values[2])
        specializ_kaf_entry.insert(0, values[3])
    except:
        None


def select_record_naznachenie(e):
    try:
        clear_entries()

        selected = naznachenie_tree.focus()
        values = naznachenie_tree.item(selected, 'values')

        naznachenie_entry.insert(0, values[1])
    except:
        None


def select_record_vid(e):
    try:
        clear_entries()

        selected = vid_tree.focus()
        values = vid_tree.item(selected, 'values')

        vidi_entry.insert(0, values[1])
    except:
        None


rooms_tree.bind("<ButtonRelease-1>", select_record_rooms)
my_tree.bind("<ButtonRelease-1>", select_record_kaf)
naznachenie_tree.bind("<ButtonRelease-1>", select_record_naznachenie)
vid_tree.bind("<ButtonRelease-1>", select_record_vid)


def update_record_rooms():
    # Grab the record number
    selected = rooms_tree.focus()
    values = rooms_tree.item(selected, 'values')
    # Update record
    rooms_tree.item(selected, text="", values=(values[0],
        comnat_entry.get(), shirina_entry.get(), dlina_entry.get(), naznach_entry.get(), vid_entry.get(),
        visota_entry.get(),
        podrazdel_entry.get(), etazh_entry.get(), korpus_entry.get()))

    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect('rooms')

    # Create a cursor instance
    c = conn.cursor()

    cursor = c.execute('select * from rooms')
    names = [description[0] for description in cursor.description]


    c.execute("""UPDATE rooms SET nomer = :nomer, shirin = :shirin, dlin=:dlin, naznachenie=:naznachenie, vid=:vid, 
    visota=:visota, podrazdelenie=:podrazdelenie, itage=:itage, korpus=:korpus WHERE rowid = :rowid""",
              {
                  'rowid': values[0],
                  'nomer': comnat_entry.get(),
                  'shirin': shirina_entry.get(),
                  'dlin': dlina_entry.get(),
                  'naznachenie': naznach_entry.get(),
                  'vid': vid_entry.get(),
                  'visota': visota_entry.get(),
                  'podrazdelenie': podrazdel_entry.get(),
                  'itage': etazh_entry.get(),
                  'korpus': korpus_entry.get()
              })


    conn.commit()

    conn.close()


def update_record_kaf():
    # Grab the record number
    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')
    # Update record
    my_tree.item(selected, text="", values=(values[0], nazvan_kaf_entry.get(), zavkaf_kaf_entry.get(), specializ_kaf_entry.get()))

    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect('kafedra')

    # Create a cursor instance
    c = conn.cursor()

    cursor = c.execute('select * from kafedra')
    names = [description[0] for description in cursor.description]

    c.execute("""UPDATE kafedra SET nazvanie=:nazvanie, zavkaf=:zavkaf, special=:special  WHERE rowid = :rowid""",
              {
                  'rowid': values[0],
                  'nazvanie': nazvan_kaf_entry.get(),
                  'zavkaf': zavkaf_kaf_entry.get(),
                  'special': specializ_kaf_entry.get(),
              })


    conn.commit()

    conn.close()

    get_kafedra()


def update_record_naznachenie():
    # Grab the record number
    selected = naznachenie_tree.focus()
    values = naznachenie_tree.item(selected, 'values')
    # Update record
    naznachenie_tree.item(selected, text="", values=(values[0], naznachenie_entry.get()))

    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect('naznachenie')

    # Create a cursor instance
    c = conn.cursor()

    cursor = c.execute('select rowid, * from naznachenie')
    names = [description[0] for description in cursor.description]

    c.execute("""UPDATE naznachenie SET naznachenie=:naznachenie  WHERE rowid = :rowid""",
              {
                  'rowid': values[0],
                  'naznachenie': naznachenie_entry.get()
              })


    conn.commit()

    conn.close()

    get_naznachenie()


def update_record_vid():
    # Grab the record number
    selected = vid_tree.focus()
    values = vid_tree.item(selected, 'values')
    # Update record
    vid_tree.item(selected, text="", values=(values[0], vidi_entry.get()))

    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect('vid')

    # Create a cursor instance
    c = conn.cursor()

    cursor = c.execute('select rowid, * from vid')
    names = [description[0] for description in cursor.description]

    c.execute("""UPDATE vid SET vid=:vid  WHERE rowid = :rowid""",
              {
                  'rowid': values[0],
                  'vid': vidi_entry.get()
              })


    conn.commit()

    conn.close()

    get_vid()


def show_kaf():
    search_by_kaf = ttk.Combobox(search_frame, values=['Название', 'Зав. Кафедрой', 'Специализация'], state='readonly')
    search_by_kaf.grid(row=0, column=0, padx=10, pady=10)
    tree_frame.pack(pady=20, padx=21, expand=TRUE, fill=BOTH)
    search_button.bind("<Return>",
                       lambda event, table='kafedra', table_tree=my_tree, srch_by=search_by_kaf, type='search': search(event, table,
                                                                                                        table_tree,
                                                                                                        srch_by, type))
    rooms_frame.forget()
    naznachenie_frame.forget()
    vid_frame.forget()
    vid_add_frame.forget()
    rooms_add_frame.forget()
    naznachenie_add_frame.forget()
    kaf_add_frame.pack(fill='x', padx=20)
    clear_entries()


def show_rooms():
    search_by_rooms = ttk.Combobox(search_frame, values=["Комната", "Ширина (м)", "Длина (м)", "Назначение", "Вид помещения", "Высота потолков (м)", "Подразделение",
            "Этаж"], state='readonly')
    search_by_rooms.grid(row=0, column=0, padx=10, pady=10)
    rooms_frame.pack(pady=20, padx=21, expand=TRUE, fill=BOTH)
    search_button.bind("<Return>",
                       lambda event, table='rooms', table_tree=rooms_tree, srch_by=search_by_rooms, type='search': search(event, table,
                                                                                                           table_tree,
                                                                                                           srch_by, type))
    tree_frame.forget()
    naznachenie_frame.forget()
    vid_frame.forget()
    vid_add_frame.forget()
    naznachenie_add_frame.forget()
    kaf_add_frame.forget()
    rooms_add_frame.pack(fill="x", padx=20)
    spinbox_frame = Frame(search_frame)
    spinbox_frame.grid(row=0, column=3)
    spinbox_button.grid(row=0, column=4)
    clear_entries()


def show_naznachenie():
    search_by_naznachenie = ttk.Combobox(search_frame,
                                   values=["Ключ", "Назначение"], state='readonly')
    search_by_naznachenie.grid(row=0, column=0, padx=10, pady=10)
    search_button.bind("<Return>",
                       lambda event, table='naznachenie', table_tree=naznachenie_tree, srch_by=search_by_naznachenie, type='search': search(event, table,
                                                                                                        table_tree,
                                                                                                        srch_by, type))

    tree_frame.forget()
    rooms_frame.forget()
    vid_frame.forget()
    vid_add_frame.forget()
    rooms_add_frame.forget()
    kaf_add_frame.forget()
    naznachenie_frame.pack(pady=20, padx=21, expand=TRUE, fill=BOTH)
    naznachenie_add_frame.pack(fill="x", padx=20)
    clear_entries()


def show_vid():
    search_by_vid = ttk.Combobox(search_frame,
                                   values=["Ключ", "Вид помещения"], state='readonly')
    search_by_vid.grid(row=0, column=0, padx=10, pady=10)
    search_button.bind("<Return>",
                       lambda event, table='vid', table_tree=vid_tree, srch_by=search_by_vid, type='search': search(event, table,
                                                                                                        table_tree,
                                                                                                        srch_by, type))

    tree_frame.forget()
    rooms_frame.forget()
    naznachenie_frame.forget()
    rooms_add_frame.forget()
    kaf_add_frame.forget()
    naznachenie_add_frame.forget()
    vid_frame.pack(pady=20, padx=21, expand=TRUE, fill=BOTH)
    vid_add_frame.pack(fill="x", padx=20)
    clear_entries()

spinbox_frame.grid(row=0, column=3, padx=50)


def remove_one_rooms(tree, table):
    x = tree.selection()
    for record in x:
        value = tree.item(record, 'values')

        conn = sqlite3.connect(table)
        c = conn.cursor()

        c.execute("DELETE FROM "+table+" WHERE rowid = "+value[0]+"")

        rooms_tree.delete(record)

        conn.commit()
        conn.close()

    clear_entries()


def remove_one_kaf(tree, table):
    x = tree.selection()
    for record in x:
        value = tree.item(record, 'values')

        conn = sqlite3.connect(table)
        c = conn.cursor()

        c.execute("DELETE FROM "+table+" WHERE rowid = "+value[0]+"")

        tree.delete(record)

        conn.commit()
        conn.close()

    clear_entries()

    get_kafedra()


def remove_one_naznachenie(tree, table):
    x = tree.selection()
    for record in x:
        value = tree.item(record, 'values')

        conn = sqlite3.connect(table)
        c = conn.cursor()

        c.execute("DELETE FROM "+table+" WHERE rowid = "+value[0]+"")

        tree.delete(record)

        conn.commit()
        conn.close()

    clear_entries()

    get_naznachenie()


def remove_one_vid(tree, table):
    x = tree.selection()
    for record in x:
        value = tree.item(record, 'values')

        conn = sqlite3.connect(table)
        c = conn.cursor()

        c.execute("DELETE FROM "+table+" WHERE rowid = "+value[0]+"")

        tree.delete(record)

        conn.commit()
        conn.close()

    clear_entries()

    get_vid()


def add_record_rooms(tree, table):
    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect(table)

    # Create a cursor instance
    c = conn.cursor()

    # Add New Record
    c.execute("INSERT INTO "+table+" VALUES (:nomer, :shirin, :dlin, :naznachenie, :vid, :visota, :podrazdelenie, "
                                   ":itage, :korpus)",
              {
                  'nomer': comnat_entry.get(),
                  'shirin': shirina_entry.get(),
                  'dlin': dlina_entry.get(),
                  'naznachenie': naznach_entry.get(),
                  'vid': vid_entry.get(),
                  'visota': visota_entry.get(),
                  'podrazdelenie': podrazdel_entry.get(),
                  'itage': etazh_entry.get(),
                  'korpus': korpus_entry.get()
              })

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear entry boxes
    clear_entries()

    # Clear The Treeview Table
    tree.delete(*tree.get_children())

    # Run to pull data from database on start
    query_database('rooms', tree)


def add_record_naznachenie(tree, table):
    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect(table)

    # Create a cursor instance
    c = conn.cursor()

    # Add New Record
    c.execute("INSERT INTO "+table+" VALUES (:naznachenie)",
              {
                  'naznachenie': naznachenie_entry.get(),

              })

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear entry boxes
    clear_entries()

    # Clear The Treeview Table
    tree.delete(*tree.get_children())

    # Run to pull data from database on start
    query_database('naznachenie', tree)

    get_naznachenie()


def add_record_vid(tree, table):
    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect(table)

    # Create a cursor instance
    c = conn.cursor()

    # Add New Record
    c.execute("INSERT INTO "+table+" VALUES (:vid)",
              {
                  'vid': vidi_entry.get(),

              })

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear entry boxes
    clear_entries()

    # Clear The Treeview Table
    tree.delete(*tree.get_children())

    # Run to pull data from database on start
    query_database('vid', tree)

    get_vid()


def add_record_kaf(tree, table):
    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect(table)

    # Create a cursor instance
    c = conn.cursor()

    # Add New Record
    c.execute("INSERT INTO "+table+" VALUES (:nazvanie, :zavkaf, :special)",
              {
                  'nazvanie': nazvan_kaf_entry.get(),
                  'zavkaf': zavkaf_kaf_entry.get(),
                  'special': specializ_kaf_entry.get(),
              })

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    get_kafedra()

    # Clear entry boxes
    clear_entries()

    # Clear The Treeview Table
    tree.delete(*tree.get_children())

    # Run to pull data from database on start
    query_database(table, tree)




rooms_button = Button(button_frame, text="Комнаты", command=show_rooms)
rooms_button.grid(row=0, column=0, padx=10, pady=10)

kaf_button = Button(button_frame, text="Кафедра", command=show_kaf)
kaf_button.grid(row=0, column=1, padx=10, pady=10)

naznachenie_button = Button(button_frame, text="Назначения", command=show_naznachenie)
naznachenie_button.grid(row=0, column=2, padx=10, pady=10)

inform_button = Button(button_frame, text="Сведения о помещениях", command=inform)
inform_button.grid(row=0, column=7, padx=950, pady=10)

vid_button = Button(button_frame, text="Вид помещений", command=show_vid)
vid_button.grid(row=0, column=3, padx=10, pady=10)

update_button_rooms = Button(rooms_add_frame, text="Обновить запись", command=update_record_rooms)
update_button_rooms.grid(row=1, column=9, pady=10, padx=10)

delete_button_rooms = Button(rooms_add_frame, text="Удалить запись", command=lambda tree=rooms_tree, table='rooms': remove_one_rooms(tree,table))
delete_button_rooms.grid(row=1, column=10, pady=10, padx=10)

add_record_button_rooms = Button(rooms_add_frame, text="Добавить запись", command=lambda tree=rooms_tree, table='rooms': add_record_rooms(tree, table))
add_record_button_rooms.grid(row=0, column=10, pady=10, padx=10)


update_button_kaf = Button(kaf_add_frame, text="Обновить запись", command=update_record_kaf)
update_button_kaf.grid(row=0, column=8, pady=10, padx=10)

delete_button_kaf = Button(kaf_add_frame, text="Удалить запись", command=lambda tree=my_tree, table='kafedra': remove_one_kaf(tree,table))
delete_button_kaf.grid(row=0, column=10, pady=10, padx=10)

add_record_button_kaf = Button(kaf_add_frame, text="Добавить запись", command=lambda tree=my_tree, table='kafedra': add_record_kaf(tree, table))
add_record_button_kaf.grid(row=0, column=9, pady=10, padx=10)

update_button_naznachenie = Button(naznachenie_add_frame, text="Обновить запись", command=update_record_naznachenie)
update_button_naznachenie.grid(row=0, column=2, pady=10, padx=10)

delete_button_naznachenie = Button(naznachenie_add_frame, text="Удалить запись", command=lambda tree=naznachenie_tree, table='naznachenie': remove_one_naznachenie(tree, table))
delete_button_naznachenie.grid(row=0, column=3, pady=10, padx=10)

add_record_button_naznachenie = Button(naznachenie_add_frame, text="Добавить запись", command=lambda tree=naznachenie_tree, table='naznachenie': add_record_naznachenie(tree, table))
add_record_button_naznachenie.grid(row=0, column=4, pady=10, padx=10)

update_button_vid = Button(vid_add_frame, text="Обновить запись", command=update_record_vid)
update_button_vid.grid(row=0, column=2, pady=10, padx=10)

delete_button_vid = Button(vid_add_frame, text="Удалить запись", command=lambda tree=vid_tree, table='vid': remove_one_vid(tree, table))
delete_button_vid.grid(row=0, column=3, pady=10, padx=10)

add_record_button_vid = Button(vid_add_frame, text="Добавить запись", command=lambda tree=vid_tree, table='vid': add_record_vid(tree, table))
add_record_button_vid.grid(row=0, column=4, pady=10, padx=10)


query_database('rooms', rooms_tree)
query_database('kafedra', my_tree)
query_database('naznachenie', naznachenie_tree)
query_database('vid', vid_tree)

root.mainloop()
