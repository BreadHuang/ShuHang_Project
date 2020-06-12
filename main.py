import tkinter as tk
import tkinter.ttk as tt
import mysql.connector
import textwrap
from mysql.connector import Error

query_string = ""

try:
    # 連接 MySQL 資料庫
    connection = mysql.connector.connect(
        host='127.0.0.1',          # 主機名稱
        database='pokemondb', # 資料庫名稱
        user='root',        # 帳號
        password='Henry19955112',  # 密碼
        auth_plugin='mysql_native_password')

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        for tables in cursor:
            print(tables)

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
    window.geometry('800x800')
    window.configure(background='white')

    result_list = []


    def wrap(string, lenght=50):
        return '\n'.join(textwrap.wrap(string, lenght))

    def query_txt():
        # input_str = input_entry.get(1.0,tk.END)
        input_str = "SELECT name, description FROM location"
        cursor.execute(input_str)
        result = cursor.fetchall()
        for x in result:
            # print(x[0],x[1])
            result_list.append([x[0],x[1]])


    def change_bar(*args):
        select = select_combobox.get()
        if select == 'Use UI buttons':
            show_btn()
        elif select == 'Use MySQL comment':
            query_txt()

        print(result_list)
        # print(result_list[0][0], result_list[0][1])
        tree = tt.Treeview(window)  # 表格
        tree["columns"] = ( "地區", "描述")
        tree.column("地區", width=200)  # 表示列,不显示
        tree.column("描述", width=300)

        tree.heading("地區", text="地區-name")  # 显示表头
        tree.heading("描述", text="描述-description")

        for x in result_list:
            tree.insert('', 'end', values=(x[0], wrap(x[1])))
        tree.pack()

    def show_btn():
        cursor.execute("SHOW TABLES")
        for tables in cursor:
            print(tables)

    header_Label = tk.Label(window, text='寶可夢圖鑑', font=('Arial', 30))
    header_Label.pack()

    select_frame = tk.Frame(window)
    select_frame.pack(side=tk.TOP)

    select_label = tk.Label(select_frame, text='查詢工具', width=20, font=('Arial', 14), relief="groove")
    select_label.configure(background='#00A600')
    select_label.pack(side=tk.LEFT)

    #下拉式選單
    select_bar = ['Use UI buttons', 'Use MySQL comment']
    select_combobox = tt.Combobox(select_frame, width=250, value=select_bar)
    select_combobox.pack(side=tk.RIGHT)

    input_frame = tk.Frame(window, width=800, relief="solid")
    input_frame.pack(side=tk.TOP)

    input_label = tk.Label(input_frame, text='查詢關鍵字', width=20, height=10, font=('Arial', 14), relief="groove")
    input_label.configure(background='#00A600')
    input_label.pack(side=tk.LEFT)

    #Query輸入
    input_entry = tk.Text(input_frame, width=250, height=10, bg='#F0F0F0', font=('Arial', 14), relief="solid")
    input_entry.pack(side=tk.RIGHT)

    #查詢按鈕
    search_btn = tk.Button(window, text='查詢', width=400, bg='#E0E0E0', font=('Arial', 20), command=change_bar, relief='raised')
    search_btn.pack()

    result_title = tk.Label(window, text='查詢結果', width=800, font=('Roman', 30))
    result_title.configure(background='white')
    result_title.pack(anchor='center')

    # 運行主程式
    window.mainloop()

except Error as e:
    print("資料庫連接失敗：", e)

# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("資料庫連線已關閉")

