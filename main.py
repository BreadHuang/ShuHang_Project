import tkinter as tk
import tkinter.ttk as tt
import mysql.connector
import textwrap
from mysql.connector import Error
from tkinter import messagebox

is_first_check = 0
try:
    # 連接 MySQL 資料庫
    connection = mysql.connector.connect(
        host='127.0.0.1',          # 主機名稱
        database='pokemondb', # 資料庫名稱
        user='root',        # 帳號
        password='Henry19955112',  # 密碼
        auth_plugin='mysql_native_password')


    if connection.is_connected():
        print("資料庫連接成功")
        cursor = connection.cursor()

        # 查詢資料庫
        # cursor.execute("SELECT name, description FROM location;")

        #顯示table屬性
        # attributes = [des[0] for des in cursor.description]
        # for attribute in attributes:
        #     print(attribute)

        # 列出查詢的資料
        # for (name, description) in cursor:
        #     print("地區名稱: %s, 地區描述: %s" % (name, description))

    # 建立主視窗和 Frame（把元件變成群組的容器）
    window = tk.Tk()
    window.title('Pokemon')
    window.geometry('1000x1000')
    window.configure(background='white')

    result_list = []

    header_Label = tk.Label(window, text='寶可夢圖鑑', font=('Arial', 30))
    header_Label.pack()

    #查詢工具列
    select_tool_frame = tk.Frame(window, width=800, relief="solid")
    select_tool_frame.pack(side=tk.TOP)
    select_tool = tk.Label(select_tool_frame, text='查詢工具', width=20, font=('Arial', 16), relief="groove")
    select_tool.configure(background='#00A600')
    select_tool.pack(side=tk.LEFT)
    tool_bar = ['Use MySQL comment', 'Use UI buttons']
    select_tool_combobox = tt.Combobox(select_tool_frame, width=250, value=tool_bar)
    select_tool_combobox.current(0)
    select_tool_combobox.pack(side=tk.RIGHT)

    #Query輸入
    input_query_frame = tk.Frame(window, width=800, relief="solid")
    input_query_frame.pack(side=tk.TOP)
    input_label = tk.Label(input_query_frame, text='查詢關鍵字', width=20, height=10, font=('Arial', 16), relief="groove")
    input_label.configure(background='#00A600')
    input_label.pack(side=tk.LEFT)
    input_entry = tk.Text(input_query_frame, width=250, height=10, bg='#ADADAD', font=('Arial', 16), relief="solid")
    input_entry.pack(side=tk.RIGHT)

    #快捷條件輸入
    query_frame = tk.Frame(window, width=800, relief="solid")
    query_frame.pack(side=tk.TOP)
    table_Label = tk.Label(query_frame, text='要查詢的資料表', width=20, font=('Arial', 16), relief="groove")
    table_Label.configure(background='#E0E0E0')
    table_Label.grid(row=0,column=0)
    table_entry = tk.Text(query_frame, width=250, height=1, bg='#ADADAD', font=('Arial', 16), relief="solid")
    table_entry.grid(row=0, column=1)
    select_attr_Label = tk.Label(query_frame, text='欄位', width=20, font=('Arial', 16), relief="groove")
    select_attr_Label.configure(background='#E0E0E0')
    select_attr_Label.grid(row=1, column=0)
    attr_entry = tk.Text(query_frame, width=250, height=1, bg='#ADADAD', font=('Arial', 16), relief="solid")
    attr_entry.grid(row=1, column=1)
    condition_Label = tk.Label(query_frame, text='輸入條件', width=20, font=('Arial', 16), relief="groove")
    condition_Label.configure(background='#E0E0E0')
    condition_Label.grid(row=2, column=0)
    condition_entry = tk.Text(query_frame, width=250, height=1, bg='#ADADAD', font=('Arial', 16), relief="solid")
    condition_entry.grid(row=2, column=1)

    #快捷查詢按鈕
    query_btn_frame = tk.Frame(window, width=800, relief="solid")
    query_btn_frame.pack(side=tk.TOP)
    select_btn = tk.Button(query_btn_frame,  text='Select', bg='#E0E0E0', font=('Arial', 20),  relief='raised')
    select_btn.pack(side=tk.LEFT)
    insert_btn = tk.Button(query_btn_frame, text='Insert',  bg='#E0E0E0', font=('Arial', 20),  relief='raised')
    insert_btn.pack(side=tk.LEFT)
    delete_btn = tk.Button(query_btn_frame,  text='Delete',  bg='#E0E0E0', font=('Arial', 20), relief='raised')
    delete_btn.pack(side=tk.LEFT)
    update_btn = tk.Button(query_btn_frame,  text='Update',  bg='#E0E0E0', font=('Arial', 20), relief='raised')
    update_btn.pack(side=tk.LEFT)


    show_frame = tk.Frame(window, width=800, relief="solid")
    show_frame.pack(side=tk.TOP)
    # 查詢按鈕
    search_btn = tk.Button(show_frame, text='查詢', width=400, bg='#E0E0E0', font=('Arial', 20), relief='raised')
    search_btn.pack(side=tk.TOP, anchor='center')

    result_title = tk.Label(show_frame, text='查詢結果', width=800, font=('Roman', 30))
    result_title.configure(background='white')
    result_title.pack(side=tk.TOP, anchor='center')

    result_frame = tk.Frame(window, width=800, relief="solid")
    result_frame.pack(side=tk.TOP, fill='x')

    #清除文字
    def clearTxt():
        table_entry.delete("1.0","end")
        attr_entry.delete("1.0","end")
        condition_entry.delete("1.0","end")
        input_entry.delete("1.0","end")

    #清除顯示表格
    def clearTable():
        global is_first_check
        # print(is_first_check)
        if is_first_check > 0:
            for i in result_frame.winfo_children():
                i.destroy()
        is_first_check = is_first_check + 1

    def wrap(string, lenght = 15):

        return '\n'.join(textwrap.wrap(string, lenght))
        # print(string, len(string[0]))
        # len_str = len(string[0])
        # if len_str > lenght:
        #     return '\n'.join(textwrap.wrap(string, lenght))
        # else:
        #     return

    def showTree(field_names):
        col_count = len(field_names)
        if col_count == 1:
            style = tt.Style(result_frame)
            style.configure('Treeview', rowheight=70)
            tree = tt.Treeview(result_frame, show='headings')  # 表格

            tree["columns"] = (field_names[0])
            tree.column(field_names[0], width=300)

            tree.heading(field_names[0], text=field_names[0])

            for i in range(len(result_list)):
                tree.insert('', 'end', values=(result_list[i]))
            tree.pack(side= tk.TOP, fill='x')
            result_list.clear()
        elif col_count == 2:
            style = tt.Style(result_frame)
            style.configure('Treeview', rowheight=70)
            tree = tt.Treeview(result_frame, show='headings')  # 表格

            tree["columns"] = (field_names[0], field_names[1])
            tree.column(field_names[0], width=300)
            tree.column(field_names[1], width=300)

            tree.heading(field_names[0], text=field_names[0])
            tree.heading(field_names[1], text=field_names[1])

            for i in range(0, len(result_list), 2):
                tree.insert('', 'end',
                            values=(result_list[i], result_list[i + 1]))
            tree.pack(side= tk.TOP, fill='x')
            result_list.clear()
        elif col_count == 3:
            style = tt.Style(result_frame)
            style.configure('Treeview', rowheight=70)
            tree = tt.Treeview(result_frame, show='headings')  # 表格

            tree["columns"] = (field_names[0], field_names[1], field_names[2])
            tree.column(field_names[0], width=50)
            tree.column(field_names[1], width=200)
            tree.column(field_names[2], width=200)

            tree.heading(field_names[0], text=field_names[0])
            tree.heading(field_names[1], text=field_names[1])
            tree.heading(field_names[2], text=field_names[2])

            for i in range(0, len(result_list), 3):
                tree.insert('', 'end',
                            values=(result_list[i], result_list[i + 1], result_list[i + 2]))
            tree.pack(side= tk.TOP, fill='x')
            result_list.clear()
        elif col_count == 4:
            style = tt.Style(result_frame)
            style.configure('Treeview', rowheight=70)
            tree = tt.Treeview(result_frame, show='headings')  # 表格

            tree["columns"] = (field_names[0], field_names[1], field_names[2], field_names[3])
            tree.column(field_names[0], width=50)
            tree.column(field_names[1], width=200)
            tree.column(field_names[2], width=200)
            tree.column(field_names[3], width=200)

            tree.heading(field_names[0], text=field_names[0])
            tree.heading(field_names[1], text=field_names[1])
            tree.heading(field_names[2], text=field_names[2])
            tree.heading(field_names[3], text=field_names[3])

            for i in range(0, len(result_list), 4):
                tree.insert('', 'end',
                            values=(result_list[i], result_list[i + 1], result_list[i + 2], result_list[i + 3]))
            tree.pack(side= tk.TOP, fill='x')
            result_list.clear()
        elif col_count == 5:
            style = tt.Style(result_frame)
            style.configure('Treeview', rowheight=70)
            tree = tt.Treeview(result_frame, show='headings')  # 表格

            tree["columns"] = (field_names[0], field_names[1], field_names[2], field_names[3], field_names[4])
            tree.column(field_names[0], width=50)
            tree.column(field_names[1], width=200)
            tree.column(field_names[2], width=200)
            tree.column(field_names[3], width=200)
            tree.column(field_names[4], width=200)

            tree.heading(field_names[0], text=field_names[0])
            tree.heading(field_names[1], text=field_names[1])
            tree.heading(field_names[2], text=field_names[2])
            tree.heading(field_names[3], text=field_names[3])
            tree.heading(field_names[4], text=field_names[4])

            for i in range(0, len(result_list), 5):
                tree.insert('', 'end',
                            values=(result_list[i], result_list[i + 1], result_list[i + 2], result_list[i + 3], result_list[i + 4]))
            tree.pack(side= tk.TOP, fill='x')
            result_list.clear()
        elif col_count == 6:
            style = tt.Style(result_frame)
            style.configure('Treeview', rowheight=70)
            tree = tt.Treeview(result_frame, show='headings')  # 表格

            tree["columns"] = (field_names[0], field_names[1], field_names[2], field_names[3], field_names[4], field_names[5])
            tree.column(field_names[0], width=50)
            tree.column(field_names[1], width=200)
            tree.column(field_names[2], width=200)
            tree.column(field_names[3], width=200)
            tree.column(field_names[4], width=200)
            tree.column(field_names[5], width=200)

            tree.heading(field_names[0], text=field_names[0])
            tree.heading(field_names[1], text=field_names[1])
            tree.heading(field_names[2], text=field_names[2])
            tree.heading(field_names[3], text=field_names[3])
            tree.heading(field_names[4], text=field_names[4])
            tree.heading(field_names[5], text=field_names[5])

            for i in range(0, len(result_list), 6):
                tree.insert('', 'end',
                            values=(result_list[i], result_list[i + 1], result_list[i + 2], result_list[i + 3],
                                    result_list[i + 4], result_list[i + 5]))
            tree.pack(side= tk.TOP, fill='x')
            result_list.clear()
        elif col_count == 7:
            style = tt.Style(result_frame)
            style.configure('Treeview', rowheight=70)
            tree = tt.Treeview(result_frame, show='headings')  # 表格

            tree["columns"] = (
            field_names[0], field_names[1], field_names[2], field_names[3], field_names[4], field_names[5], field_names[6])
            tree.column(field_names[0], width=50)
            tree.column(field_names[1], width=200)
            tree.column(field_names[2], width=200)
            tree.column(field_names[3], width=200)
            tree.column(field_names[4], width=200)
            tree.column(field_names[5], width=200)
            tree.column(field_names[6], width=200)

            tree.heading(field_names[0], text=field_names[0])
            tree.heading(field_names[1], text=field_names[1])
            tree.heading(field_names[2], text=field_names[2])
            tree.heading(field_names[3], text=field_names[3])
            tree.heading(field_names[4], text=field_names[4])
            tree.heading(field_names[5], text=field_names[5])
            tree.heading(field_names[6], text=field_names[6])

            for i in range(0, len(result_list), 7):
                tree.insert('', 'end',
                            values=(result_list[i], result_list[i + 1], result_list[i + 2], result_list[i + 3],
                                    result_list[i + 4], result_list[i + 5], result_list[i + 6]))
            tree.pack(side= tk.TOP, fill='x')
            result_list.clear()

    def query_txt():
        clearTable()
        input_str = input_entry.get(1.0,tk.END)
        # input_str = "SELECT * FROM store"
        # input_str = "INSERT INTO location (`Lid`, `name`, `description`) VALUES ('12','Taiwan','Good place')"
        # input_str = "DELETE FROM location WHERE Lid = '12'"
        # input_str = "UPDATE location SET name = 'Japan' WHERE Lid = '12'"
        if input_str[0:6] == "SELECT":
            try:
                cursor.execute(input_str)
                result = cursor.fetchall()
                col_count = len(cursor.description)  # 欄位長度
                field_names = [i[0] for i in cursor.description]  # 欄位標題名稱

                for x in result:
                    for i in range(col_count):
                        result_list.append([x[i]])
                # print(result_list)
                # print(len(result_list))
                # print(field_names)
                showTree(field_names)
            except Error as e:
                messagebox.showinfo("查詢錯誤",e)
        elif input_str[0:6] == "INSERT":
            try:
                cursor.execute(input_str)
                connection.commit()
                clearTxt()
                messagebox.showinfo("One record was inserted.")
            except Error as e:
                messagebox.showinfo("資料新增失敗: ",e)
        elif input_str[0:6] == "DELETE":
            try:
                cursor.execute(input_str)
                connection.commit()
                clearTxt()
                messagebox.showinfo("The records was(were) delete.")
            except Error as e:
                messagebox.showinfo("資料刪除失敗: ",e)
        elif input_str[0:6] == "UPDATE":
            try:
                cursor.execute(input_str)
                connection.commit()
                clearTxt()
                messagebox.showinfo("One record was affected.")
            except Error as e:
                messagebox.showinfo("資料更新失敗: ",e)

    def change_bar(event):
        select = select_tool_combobox.get()
        if select == 'Use UI buttons':
            # print("Use UI buttons")
            table_entry.configure(state='normal')
            attr_entry.configure(state='normal')
            condition_entry.configure(state='normal')

        elif select == 'Use MySQL comment':
            # print("Use MySQL comment")
            table_entry.configure(state='disabled')
            attr_entry.configure(state='disabled')
            condition_entry.configure(state='disabled')
            query_txt()

    def query_btn(*args):
        select = select_tool_combobox.get()
        if select == 'Use UI buttons':
            print()
        elif select == 'Use MySQL comment':
            query_txt()

    def press_sel_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END+"-1c") #tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0,tk.END+"-1c")
        condition = condition_entry.get(1.0,tk.END+"-1c")
        if len(condition) > 0 :
            input_str = "SELECT " + attr + " FROM " + table + " WHERE " + condition
        else:
            input_str = "SELECT " + attr + " FROM " + table;
        # print(input_str)
        cursor.execute(input_str)
        result = cursor.fetchall()
        col_count = len(cursor.description)  # 欄位長度
        field_names = [i[0] for i in cursor.description]  # 欄位標題名稱
        for x in result:
            for i in range(col_count):
                result_list.append([x[i]])
        clearTxt()
        showTree(field_names)

    def press_in_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        condition = condition_entry.get(1.0, tk.END + "-1c")
        input_str = "INSERT INTO " + table + "("+ attr + ") VALUES (" + condition + ")"

        cursor.execute(input_str)
        connection.commit()
        clearTxt()
        messagebox.showinfo("One record was inserted.")
        print("One record was inserted.")

    def press_del_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        condition = condition_entry.get(1.0, tk.END + "-1c")
        input_str = "DELETE FROM " + table + " WHERE " + condition

        # print(input_str)
        cursor.execute(input_str)
        connection.commit()
        clearTxt()
        messagebox.showinfo("The records was(were) delete.")
        print("The records was(were) delete.")

    def press_up_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        condition = condition_entry.get(1.0, tk.END + "-1c")
        input_str = "UPDATE " + table + " SET " + attr + " WHERE " + condition

        cursor.execute(input_str)
        connection.commit()
        clearTxt()
        messagebox.showinfo("One record was affected.")
        print("One record was affected.")

    search_btn.bind("Button", query_btn)
    select_tool_combobox.bind("<<ComboboxSelected>>", change_bar)
    select_btn.bind("<Button>", press_sel_btn)
    insert_btn.bind("<Button>", press_in_btn)
    delete_btn.bind("<Button>", press_del_btn)
    update_btn.bind("<Button>", press_up_btn)

    # 運行主程式
    window.mainloop()

except Error as e:
    print("資料庫連接失敗：", e)

# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("資料庫連線已關閉")