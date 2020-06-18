import tkinter as tk
import tkinter.ttk as tt
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

is_first_check = 0
try:
    # 連接 MySQL 資料庫
    connection = mysql.connector.connect(
        host='140.116.82.152',          # 主機名稱
        database='pokemondb', # 資料庫名稱
        user='root',        # 帳號
        password='Henry19955112',  # 密碼
        auth_plugin='mysql_native_password',
        charset='utf8')


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
    #標題設定
    header_Label = tk.Label(window, text='寶可夢圖鑑', font=('Arial', 30))
    header_Label.pack()

    #查詢工具列
    select_tool_frame = tk.Frame(window, width=800, relief="solid")
    select_tool_frame.pack(side=tk.TOP)
    select_tool = tk.Label(select_tool_frame, text='查詢工具', width=20, font=('Arial', 14), relief="groove")
    select_tool.configure(background='#F75000')
    select_tool.pack(side=tk.LEFT)
    tool_bar = ['Use UI buttons', 'Use MySQL comment']
    select_tool_combobox = tt.Combobox(select_tool_frame, width=250, value=tool_bar)
    select_tool_combobox.current(0)
    select_tool_combobox.pack(side=tk.RIGHT)

    #Query輸入
    input_query_frame = tk.Frame(window, width=800, relief="solid")
    input_query_frame.pack(side=tk.TOP)
    input_label = tk.Label(input_query_frame, text='Query命令', width=20, height=5, font=('Arial', 14), relief="groove")
    input_label.configure(background='#00A600')
    input_label.pack(side=tk.LEFT)
    input_entry = tk.Text(input_query_frame, width=250, height=5, bg='#ADADAD', font=('Arial', 14), relief="solid")
    input_entry.configure(state='disabled')
    input_entry.pack(side=tk.RIGHT)

    #快捷條件輸入
    query_frame = tk.Frame(window, width=800, relief="solid")
    query_frame.pack(side=tk.TOP)
    select_attr_Label = tk.Label(query_frame, text='Select欄位', width=20, font=('Arial', 14), relief="groove")
    select_attr_Label.configure(background='#6FB7B7')
    select_attr_Label.grid(row=0, column=0)
    attr_entry = tk.Text(query_frame, width=250, height=1, bg='#ADADAD', font=('Arial', 14), relief="solid")
    attr_entry.grid(row=0, column=1)
    table_Label = tk.Label(query_frame, text='FROM', width=20, font=('Arial', 14), relief="groove")
    table_Label.configure(background='#FFDC35')
    table_Label.grid(row=1,column=0)
    table_entry = tk.Text(query_frame, width=250, height=1, bg='#ADADAD', font=('Arial', 14), relief="solid")
    table_entry.grid(row=1, column=1)
    condition_Label = tk.Label(query_frame, text='WHERE(GROUP BY)', width=20, font=('Arial', 14), relief="groove")
    condition_Label.configure(background='#FF9224')
    condition_Label.grid(row=2, column=0)
    condition_entry = tk.Text(query_frame, width=250, height=1, bg='#ADADAD', font=('Arial', 14), relief="solid")
    condition_entry.grid(row=2, column=1)
    sub_condition_Label = tk.Label(query_frame, text='IN/NOT IN 條件(HAVING)', width=20, font=('Arial', 14), relief="groove")
    sub_condition_Label.configure(background='#2894FF')
    sub_condition_Label.grid(row=3, column=0)
    sub_condition_entry = tk.Text(query_frame, width=250, height=1, bg='#ADADAD', font=('Arial', 14), relief="solid")
    sub_condition_entry.grid(row=3, column=1)

    #快捷查詢按鈕
    query_btn_frame = tk.Frame(window, width=800)
    query_btn_frame.pack(side=tk.TOP)
    query_Label = tk.Label(query_btn_frame, text='一般搜尋快捷：', width=20, font=('Arial', 12) )
    query_Label.pack(side=tk.LEFT)
    select_btn = tk.Button(query_btn_frame,  text='Select', bg='#E0E0E0', font=('Arial', 12),  relief='raised')
    select_btn.pack(side=tk.LEFT)
    insert_btn = tk.Button(query_btn_frame, text='Insert',  bg='#E0E0E0', font=('Arial', 12),  relief='raised')
    insert_btn.pack(side=tk.LEFT)
    delete_btn = tk.Button(query_btn_frame,  text='Delete',  bg='#E0E0E0', font=('Arial', 12), relief='raised')
    delete_btn.pack(side=tk.LEFT)
    update_btn = tk.Button(query_btn_frame,  text='Update',  bg='#E0E0E0', font=('Arial', 12), relief='raised')
    update_btn.pack(side=tk.LEFT)

    #Nested queries
    nested_btn_frame = tk.Frame(window, width=800, relief="solid")
    nested_btn_frame.pack(side=tk.TOP)
    nested_Label = tk.Label(nested_btn_frame, text='Nested queries：', width=20, font=('Arial', 12))
    nested_Label.configure(background='#E0E0E0')
    nested_Label.pack(side=tk.LEFT)
    in_btn = tk.Button(nested_btn_frame,  text='IN',  bg='#E0E0E0', font=('Arial', 12), relief='raised')
    in_btn.pack(side=tk.LEFT)
    not_in_btn = tk.Button(nested_btn_frame,  text='NOT IN',  bg='#E0E0E0', font=('Arial', 12), relief='raised')
    not_in_btn.pack(side=tk.LEFT)
    exists_btn = tk.Button(nested_btn_frame,  text='EXISTS/NOT EXISTS',  bg='#E0E0E0', font=('Arial', 12), relief='raised')
    exists_btn.pack(side=tk.LEFT)

    #Aggregate function
    aggregate_btn_frame = tk.Frame(window, width=800, relief="solid")
    aggregate_btn_frame.pack(side=tk.TOP)
    aggregate_Label = tk.Label(aggregate_btn_frame, text='Aggregation functions：', width=20, font=('Arial', 12))
    aggregate_Label.configure(background='#E0E0E0')
    aggregate_Label.pack(side=tk.LEFT)
    count_btn = tk.Button(aggregate_btn_frame, text='Count', bg='#E0E0E0', font=('Arial', 12), relief='raised')
    count_btn.pack(side=tk.LEFT)
    sum_btn = tk.Button(aggregate_btn_frame, text='Sum', bg='#E0E0E0', font=('Arial', 12), relief='raised')
    sum_btn.pack(side=tk.LEFT)
    max_btn = tk.Button(aggregate_btn_frame, text='Max', bg='#E0E0E0', font=('Arial', 12), relief='raised')
    max_btn.pack(side=tk.LEFT)
    min_btn = tk.Button(aggregate_btn_frame, text='Min', bg='#E0E0E0', font=('Arial', 12), relief='raised')
    min_btn.pack(side=tk.LEFT)
    avg_btn = tk.Button(aggregate_btn_frame, text='Avg', bg='#E0E0E0', font=('Arial', 12), relief='raised')
    avg_btn.pack(side=tk.LEFT)
    having_btn = tk.Button(aggregate_btn_frame, text='Having', bg='#E0E0E0', font=('Arial', 12), relief='raised')
    having_btn.pack(side=tk.LEFT)

    #查詢的frame
    show_frame = tk.Frame(window, width=800, relief="solid")
    show_frame.pack(side=tk.TOP)
    # 查詢按鈕
    search_btn = tk.Button(show_frame, text='查詢', width=400, bg='#E0E0E0', font=('Arial', 18), relief='raised')
    search_btn.configure(state='disabled')
    search_btn.pack(side=tk.TOP, anchor='center')

    #查詢結果的標題顯示
    result_title = tk.Label(show_frame, text='查詢結果', width=800, font=('Roman', 30))
    result_title.configure(background='white')
    result_title.pack(side=tk.TOP, anchor='center')

    #顯示表格的frame
    result_frame = tk.Frame(window, width=800, relief="solid")
    result_frame.pack(side=tk.TOP, fill='x')

    #字串加入撇號
    def apostrophe(input):
        temp_str = ''
        temp_split = input.split(',')
        for i in temp_split:
            temp_str += '`' + i + '`,'
        temp_str = temp_str[:-1]
        return temp_str

    #字串加入單引號
    def single_quotation(input):
        temp_str = ''
        temp_split = input.split(',')
        for i in temp_split:
            temp_str += '\'' + i + '\','
        temp_str = temp_str[:-1]
        return temp_str
        # print(temp_str)

    #清除文字
    def clearTxt():
        table_entry.delete("1.0","end")
        attr_entry.delete("1.0","end")
        condition_entry.delete("1.0","end")
        input_entry.delete("1.0","end")
        sub_condition_entry.delete("1.0","end")

    #清除顯示表格
    def clearTable():
        global is_first_check
        # print(is_first_check)
        if is_first_check > 0:
            for i in result_frame.winfo_children():
                i.destroy()
        is_first_check = is_first_check + 1

    #顯示下方的表格
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

    #執行query 命令的function
    def query_txt(event):
        clearTable()
        input_str = input_entry.get(1.0, tk.END)
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
                messagebox.showinfo("Information","One record was inserted.")
            except Error as e:
                messagebox.showinfo("資料新增失敗",e)
        elif input_str[0:6] == "DELETE":
            try:
                cursor.execute(input_str)
                connection.commit()
                clearTxt()
                messagebox.showinfo("Information", "The records was(were) delete.")
            except Error as e:
                messagebox.showinfo("資料刪除失敗",e)
        elif input_str[0:6] == "UPDATE":
            try:
                cursor.execute(input_str)
                connection.commit()
                clearTxt()
                messagebox.showinfo("Information", "One record was affected.")
            except Error as e:
                messagebox.showinfo("資料更新失敗: ",e)

    #當上方的工具選項有變動時，需要做的動作
    def change_bar(event):
        select = select_tool_combobox.get()
        if select == 'Use UI buttons':
            table_entry.configure(state='normal')
            attr_entry.configure(state='normal')
            condition_entry.configure(state='normal')
            sub_condition_entry.configure(state='normal')

            input_entry.configure(state='disabled')
            search_btn.configure(state='disabled')
            select_btn.configure(state='normal')
            insert_btn.configure(state='normal')
            delete_btn.configure(state='normal')
            update_btn.configure(state='normal')
            count_btn.configure(state='normal')
            in_btn.configure(state='normal')
            not_in_btn.configure(state='normal')
            exists_btn.configure(state='normal')
            sum_btn.configure(state='normal')
            max_btn.configure(state='normal')
            min_btn.configure(state='normal')
            avg_btn.configure(state='normal')
            having_btn.configure(state='normal')

        elif select == 'Use MySQL comment':
            table_entry.configure(state='disabled')
            attr_entry.configure(state='disabled')
            condition_entry.configure(state='disabled')
            sub_condition_entry.configure(state='disabled')

            input_entry.configure(state='normal')
            search_btn.configure(state='normal')
            select_btn.configure(state='disabled')
            insert_btn.configure(state='disabled')
            delete_btn.configure(state='disabled')
            update_btn.configure(state='disabled')
            count_btn.configure(state='disabled')
            in_btn.configure(state='disabled')
            not_in_btn.configure(state='disabled')
            exists_btn.configure(state='disabled')
            sum_btn.configure(state='disabled')
            max_btn.configure(state='disabled')
            min_btn.configure(state='disabled')
            avg_btn.configure(state='disabled')
            having_btn.configure(state='disabled')

    #執行Select的query
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

    # 執行Insert的query
    def press_insert_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        condition = condition_entry.get(1.0, tk.END + "-1c")
        condition = single_quotation(condition)
        if attr != '*':
            attr = apostrophe(attr)
            input_str = "INSERT INTO " + table + "(" + attr + ") VALUES (" + condition + ")"
        else:
            input_str = "INSERT INTO " + table + " VALUES (" + condition + ")"
        print(input_str)
        try:
            cursor.execute(input_str)
            connection.commit()
            clearTxt()
            messagebox.showinfo("Information", "One record was inserted.")
            print("One record was inserted.")
        except Error as e:
            messagebox.showinfo("資料新增失敗", e)

    # 執行Delete的query
    def press_del_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        condition = condition_entry.get(1.0, tk.END + "-1c")
        input_str = "DELETE FROM " + table + " WHERE " + condition
        try:
            # print(input_str)
            cursor.execute(input_str)
            connection.commit()
            clearTxt()
            messagebox.showinfo("Information","The records was(were) delete.")
            # print("The records was(were) delete.")
        except Error as e:
            messagebox.showinfo("資料新增失敗", e)

    # 執行Update的query
    def press_up_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        condition = condition_entry.get(1.0, tk.END + "-1c")
        input_str = "UPDATE " + table + " SET " + attr + " WHERE " + condition
        try:
            cursor.execute(input_str)
            connection.commit()
            clearTxt()
            messagebox.showinfo("Information","One record was affected.")
            # print("One record was affected.")
        except Error as e:
            messagebox.showinfo("資料新增失敗", e)

    # 處理關於IN的query
    def press_in_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        condition = condition_entry.get(1.0, tk.END + "-1c")
        sub_condition = sub_condition_entry.get(1.0, tk.END + "-1c")
        sub_condition = single_quotation(sub_condition)
        input_str = "SELECT " + attr + " FROM " + table + " WHERE " + condition + " IN (" + sub_condition + ")"
        try:
            cursor.execute(input_str)
            result = cursor.fetchall()
            col_count = len(cursor.description)  # 欄位長度
            field_names = [i[0] for i in cursor.description]  # 欄位標題名稱
            for x in result:
                for i in range(col_count):
                    result_list.append([x[i]])
            clearTxt()
            showTree(field_names)
        except Error as e:
            messagebox.showinfo("查詢錯誤", e)

    # 處理關於 NOT IN的query
    def press_not_in_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        condition = condition_entry.get(1.0, tk.END + "-1c")
        sub_condition = sub_condition_entry.get(1.0, tk.END + "-1c")
        sub_condition = single_quotation(sub_condition)
        input_str = "SELECT " + attr + " FROM " + table + " WHERE " + condition + " NOT IN (" + sub_condition + ")"

        try:
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
        except Error as e:
            messagebox.showinfo("查詢錯誤", e)

    # 處理關於EXISTS和NOT EXISTS的query
    def press_exists_btn(event):
        clearTable()
        def send_query(event):
            exists_select = exists_combobox.get()
            # 以下五行就是獲取我們所輸入的資訊
            sel_obj = select_object.get()
            f_obj = from_object.get()
            e_sel_obj = E_select_object.get()
            e_f_obj = E_from_object.get()
            e_wh_obj = E_where_object.get()

            if exists_select == 'EXISTS':
                input_str = "SELECT " + sel_obj + " FROM " + f_obj + " WHERE EXISTS ( SELECT " + e_sel_obj + " FROM " + e_f_obj + " WHERE " + e_wh_obj + ")"
            elif exists_select == 'NOT EXISTS':
                input_str = "SELECT " + sel_obj + " FROM " + f_obj + " WHERE NOT EXISTS ( SELECT " + e_sel_obj + " FROM " + e_f_obj + " WHERE " + e_wh_obj + ")"
            print(input_str)
            try:
                cursor.execute(input_str)
                result = cursor.fetchall()
                col_count = len(cursor.description)  # 欄位長度
                field_names = [i[0] for i in cursor.description]  # 欄位標題名稱
                for x in result:
                    for i in range(col_count):
                        result_list.append([x[i]])
                showTree(field_names)
            except Error as e:
                messagebox.showinfo("查詢錯誤", e)

            input_window.destroy()

        # 定義長在視窗上的視窗
        input_window = tk.Toplevel(window)
        input_window.geometry('500x300')
        input_window.title('Other conditions window')

        select_object = tk.StringVar()  # 將輸入賦值給變數
        tk.Label(input_window, text='SELECT').place(x=10, y=10)  # 將`User name:`放置在座標（10,10）。
        entry_select_object = tk.Entry(input_window, textvariable=select_object, width=40)  # 建立一個名為`entry`，變數為`select_object`
        entry_select_object.place(x=160, y=10)  # `entry`放置在座標（160,10）.

        from_object = tk.StringVar()
        tk.Label(input_window, text='FROM').place(x=10, y=50)
        entry_from_object = tk.Entry(input_window, textvariable=from_object, width=40)
        entry_from_object.place(x=160, y=50)

        E_select_object = tk.StringVar()
        tk.Label(input_window, text='WHERE').place(x=10, y=90)
        tool_bar = ['EXISTS', 'NOT EXISTS']
        exists_combobox = tt.Combobox(input_window, width=20, value=tool_bar)
        exists_combobox.current(0)
        exists_combobox.place(x=160, y=90)

        E_select_object = tk.StringVar()
        tk.Label(input_window, text='             SELECT').place(x=10, y=130)
        entry_E_select_object = tk.Entry(input_window, textvariable=E_select_object, width=40)
        entry_E_select_object.place(x=160, y=130)

        E_from_object = tk.StringVar()
        tk.Label(input_window, text='             FROM').place(x=10, y=170)
        entry_E_from_object = tk.Entry(input_window, textvariable=E_from_object, width=40)
        entry_E_from_object.place(x=160, y=170)

        E_where_object = tk.StringVar()
        tk.Label(input_window, text='             WHERE').place(x=10, y=210)
        entry_E_where_object = tk.Entry(input_window, textvariable=E_where_object, width=40)
        entry_E_where_object.place(x=160, y=210)

        # 下面的 sign_to_Hongwei_Website
        comfirm_btn = tk.Button(input_window, text='Send query')
        comfirm_btn.place(x=200, y=250)
        comfirm_btn.bind("<Button>", send_query)

    # 處理Count的query
    def press_count_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END+"-1c") #tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        condition = condition_entry.get(1.0,tk.END+"-1c")
        if len(condition) > 0 and len(attr) > 0 :
            input_str = "SELECT COUNT(`" + attr + "`) FROM " + table + " WHERE " + condition
        elif len(condition) == 0 and len(attr) > 0:
            input_str = "SELECT COUNT(`" + attr + "`) FROM " + table
        elif len(condition) > 0 and len(attr) == 0:
            input_str = "SELECT COUNT(*) FROM " + table + " WHERE " + condition
        else:
            input_str = "SELECT COUNT(*) FROM " + table;
        cursor.execute(input_str)
        result = cursor.fetchall()
        col_count = len(cursor.description)  # 欄位長度
        field_names = [i[0] for i in cursor.description]  # 欄位標題名稱
        for x in result:
            for i in range(col_count):
                result_list.append([x[i]])
        clearTxt()
        showTree(field_names)

    # 處理SUM的query
    def press_sum_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        input_str = "SELECT SUM(`" + attr + "`) FROM " + table

        cursor.execute(input_str)
        result = cursor.fetchall()
        col_count = len(cursor.description)  # 欄位長度
        field_names = [i[0] for i in cursor.description]  # 欄位標題名稱
        for x in result:
            for i in range(col_count):
                result_list.append([x[i]])
        clearTxt()
        showTree(field_names)

    # 處理MAX的query
    def press_max_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        input_str = "SELECT MAX(`" + attr + "`) FROM " + table

        cursor.execute(input_str)
        result = cursor.fetchall()
        col_count = len(cursor.description)  # 欄位長度
        field_names = [i[0] for i in cursor.description]  # 欄位標題名稱
        for x in result:
            for i in range(col_count):
                result_list.append([x[i]])
        clearTxt()
        showTree(field_names)

    # 處理MIN的query
    def press_min_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        input_str = "SELECT MIN(`" + attr + "`) FROM " + table

        cursor.execute(input_str)
        result = cursor.fetchall()
        col_count = len(cursor.description)  # 欄位長度
        field_names = [i[0] for i in cursor.description]  # 欄位標題名稱
        for x in result:
            for i in range(col_count):
                result_list.append([x[i]])
        clearTxt()
        showTree(field_names)

    # 處理AVG的query
    def press_avg_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")  # tk.END有加上'\n'，如果不希望換行則加上 +"-1c"
        attr = attr_entry.get(1.0, tk.END + "-1c")
        input_str = "SELECT AVG(`" + attr + "`) FROM " + table

        cursor.execute(input_str)
        result = cursor.fetchall()
        col_count = len(cursor.description)  # 欄位長度
        field_names = [i[0] for i in cursor.description]  # 欄位標題名稱
        for x in result:
            for i in range(col_count):
                result_list.append([x[i]])
        clearTxt()
        showTree(field_names)

    # 處理關於HAVING的query
    def press_having_btn(event):
        clearTable()
        table = table_entry.get(1.0, tk.END + "-1c")
        attr = attr_entry.get(1.0, tk.END + "-1c")
        condition = condition_entry.get(1.0, tk.END + "-1c")
        sub_condition = sub_condition_entry.get(1.0, tk.END + "-1c")
        if len(condition) > 0:
            input_str = "SELECT " + attr + " FROM " + table + " GROUP BY " + condition + " HAVING " + sub_condition
        elif len(condition) == 0:
            input_str = "SELECT " + attr + " FROM " + table + " HAVING " + sub_condition
        print(input_str)
        try:
            cursor.execute(input_str)
            result = cursor.fetchall()
            col_count = len(cursor.description)  # 欄位長度
            field_names = [i[0] for i in cursor.description]  # 欄位標題名稱
            for x in result:
                for i in range(col_count):
                    result_list.append([x[i]])
            clearTxt()
            showTree(field_names)
        except Error as e:
            messagebox.showinfo("查詢錯誤", e)

    #將按鈕與上方的事件連接
    search_btn.bind("<Button>", query_txt)
    select_tool_combobox.bind("<<ComboboxSelected>>", change_bar)
    select_btn.bind("<Button>", press_sel_btn)
    insert_btn.bind("<Button>", press_insert_btn)
    delete_btn.bind("<Button>", press_del_btn)
    update_btn.bind("<Button>", press_up_btn)
    count_btn.bind("<Button>", press_count_btn)
    in_btn.bind("<Button>", press_in_btn)
    not_in_btn.bind("<Button>", press_not_in_btn)
    exists_btn.bind("<Button>", press_exists_btn)
    sum_btn.bind("<Button>", press_sum_btn)
    max_btn.bind("<Button>", press_max_btn)
    min_btn.bind("<Button>", press_min_btn)
    avg_btn.bind("<Button>", press_avg_btn)
    having_btn.bind("<Button>", press_having_btn)

    # 運行主程式
    window.mainloop()

except Error as e:
    print("資料庫連接失敗：", e)

# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("資料庫連線已關閉")