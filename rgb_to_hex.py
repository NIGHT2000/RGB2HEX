import tkinter as tk
import re

def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def is_valid_input(value):
    return bool(re.match("^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", value))

def convert():
    r = entry_r.get()
    g = entry_g.get()
    b = entry_b.get()

    if not (is_valid_input(r) and is_valid_input(g) and is_valid_input(b)):
        result_label.config(text="输入错误，请输入0-255之间的整数")
        return

    try:
        r = int(r)
        g = int(g)
        b = int(b)
    except ValueError:
        result_label.config(text="转换错误，请输入有效的整数")
        return

    hex_color = rgb_to_hex(r, g, b)
    result_label.config(text="对应的16进制颜色值为：" + hex_color)

def copy_hex_code():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))

root = tk.Tk()
root.title("RGB 2 hex")

label_r = tk.Label(root, text="红色值（0-255）：")
label_r.grid(row=0, column=0)
entry_r = tk.Entry(root)
entry_r.grid(row=0, column=1)

label_g = tk.Label(root, text="绿色值（0-255）：")
label_g.grid(row=1, column=0)
entry_g = tk.Entry(root)
entry_g.grid(row=1, column=1)

label_b = tk.Label(root, text="蓝色值（0-255）：")
label_b.grid(row=2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1)

convert_button = tk.Button(root, text="转换", command=convert)
convert_button.grid(row=3, column=0, columnspan=2)

copy_button = tk.Button(root, text="复制", command=copy_hex_code)
copy_button.grid(row=4, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
