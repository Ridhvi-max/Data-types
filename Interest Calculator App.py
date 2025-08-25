import tkinter as tk

def calculate():
    try:
        p = float(principal.get())
        t = float(time.get())
        r = float(rate.get())
        si = (p*r*t)/100
        ci = p*((1+r/100)**t - 1)
        result.config(text=f"SI: {si:.2f}, CI: {ci:.2f}")
    except:
        result.config(text="Enter valid numbers!")

root = tk.Tk()
root.geometry("400x400")
root.title("Interest Calculator App")

tk.Label(root, text="Principal").grid(row=0, column=0)
principal = tk.Entry(root); principal.grid(row=0, column=1)

tk.Label(root, text="Time (yrs)").grid(row=1, column=0)
time = tk.Entry(root); time.grid(row=1, column=1)

tk.Label(root, text="Rate (%)").grid(row=2, column=0)
rate = tk.Entry(root); rate.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)
result = tk.Label(root, text=""); result.grid(row=4, column=0, columnspan=2)

root.mainloop()
