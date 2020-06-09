import tkinter as tk
import tkinter.ttk as tt

# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
window.title('Pokemon')
window.geometry('800x800')
window.configure(background='white')

input_str = ""
def get_text():
    global input_str
    input_str = input_entry.get("1.0", 'end-1c')
    select = select_combobox.get()
    if select == 'MySQL':
        print(input_str)
    elif select == 'Anime_ID':
        print("Anime:")
        print(input_str)
header_Label = tk.Label(window, text='寶可夢圖鑑', font=('Arial', 30))
header_Label.pack()

select_frame = tk.Frame(window)
select_frame.pack(side=tk.TOP)

select_label = tk.Label(select_frame, text='查詢工具', width=20, font=('Arial', 14), relief="groove")
select_label.configure(background='#00A600')
select_label.pack(side=tk.LEFT)

toll = ('Anime_ID', 'MySQL')
select_combobox = tt.Combobox(select_frame, width=250, value=toll)
select_combobox.pack(side=tk.RIGHT)

input_frame = tk.Frame(window, width=800, relief="solid")
input_frame.pack(side=tk.TOP)

input_label = tk.Label(input_frame, text='查詢關鍵字', width=20, height=10, font=('Arial', 14), relief="groove")
input_label.configure(background='#00A600')
input_label.pack(side=tk.LEFT)

input_entry = tk.Text(input_frame, width=250, height=10, bg='#F0F0F0', font=('Arial', 14),relief="solid")
input_entry.pack(side=tk.RIGHT)

#查詢按鈕
search_btn = tk.Button(window, text='查詢', width=400, bg='#E0E0E0', font=('Arial', 20), command=get_text, relief='raised')
search_btn.pack()

# 運行主程式
window.mainloop()
