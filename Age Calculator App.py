import tkinter as tk
from datetime import date

def calc_age():
    try:
        today = date.today()
        age = today.year - int(year.get()) - ((today.month, today.day) < (int(month.get()), int(day.get())))
        result.config(text=f"Hi {name.get()}, you are {age} years old!")
    except:
        result.config(text="Enter valid details")

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#E6F7FF")

for i, (label, var) in enumerate([("Name", "name"), ("Date", "day"), ("Month", "month"), ("Year", "year")]):
    tk.Label(root, text=label+":", bg="#E6F7FF", fg="#003366", font=("Arial", 12, "bold")).grid(row=i, column=0, pady=5, sticky="e")
    e = tk.Entry(root, width=20)
    e.grid(row=i, column=1, pady=5)
    locals()[var] = e

tk.Button(root, text="Calculate Age", command=calc_age, bg="#66CCFF").grid(row=4, column=0, columnspan=2, pady=15)
result = tk.Label(root, text="", bg="#E6F7FF", font=("Arial", 12))
result.grid(row=5, column=0, columnspan=2)

root.mainloop()
