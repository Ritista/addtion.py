import tkinter as tk

app = tk.Tk()
app.title("calculator")
app.geometry("400x400")
first_label = tk.Label(app, text="enter first number")
first_label.pack()
first_number = tk.Entry(app)
first_number.pack()
second_label = tk.Label(app, text="enter second number")
second_label.pack()
second_number = tk.Entry(app)
second_number.pack()
result = tk.Label(app, text="result")
result.pack()
def add():
    fn = int(first_number.get())
    sn = int(second_number.get())
    result.config(text=f"result: {fn+sn}")

button = tk.Button(app, text="Add", command=add)
button.pack()
app.mainloop()
