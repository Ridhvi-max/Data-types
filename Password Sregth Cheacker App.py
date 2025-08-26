import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)
    
    if length <= 5:
        result_label.config(text="Password Strength: Weak", fg="red")
    elif 6 <= length <= 8:
        result_label.config(text="Password Strength: Medium", fg="yellow")
    elif 9 <= length <= 12:
        result_label.config(text="Password Strength: Strong", fg="light green")
    else:
        result_label.config(text="Password Strength: Very Strong", fg="dark green")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

root.mainloop()
