import tkinter as tk

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except ValueError:
        result_label.config(text="Invalid Input")

root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x200")

input_label = tk.Label(root, text="Enter length in inches:")
input_label.pack(pady=5)

entry = tk.Entry(root, width=20)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="Result will appear here", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
