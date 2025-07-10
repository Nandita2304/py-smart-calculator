import tkinter as tk
from tkinter import ttk, messagebox
import math

history = []

# Core calculation functions
def calculate_basic(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result = None
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b if b != 0 else "Err: Div by 0"
        result_label.config(text=f"Result: {result}")
        history.append(f"{a} {op} {b} = {result}")
    except:
        messagebox.showerror("Input Error", "Enter valid numbers.")

def calculate_advanced(choice):
    try:
        x = float(entry1.get())
        if choice == 'Power':
            y = float(entry2.get())
            result = math.pow(x, y)
            history.append(f"{x}^{y} = {result}")
        elif choice == 'Sqrt':
            result = math.sqrt(x)
            history.append(f"√{x} = {result}")
        elif choice == 'Log':
            result = math.log(x)
            history.append(f"log({x}) = {result}")
        result_label.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Input Error", "Check your inputs.")

def calculate_trig(func):
    try:
        angle = float(entry1.get())
        rad = math.radians(angle)
        result = None
        if func == 'sin':
            result = math.sin(rad)
        elif func == 'cos':
            result = math.cos(rad)
        elif func == 'tan':
            result = math.tan(rad)
        result_label.config(text=f"{func}({angle}) = {round(result, 4)}")
        history.append(f"{func}({angle}) = {round(result, 4)}")
    except:
        messagebox.showerror("Error", "Invalid angle input.")

def calculate_bmi():
    try:
        weight = float(entry1.get())
        height = float(entry2.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {round(bmi, 2)}")
        history.append(f"BMI: W={weight}, H={height}, BMI={round(bmi, 2)}")
    except:
        messagebox.showerror("Input Error", "Enter valid weight and height.")

def unit_convert(option):
    try:
        val = float(entry1.get())
        if option == 'C to F':
            result = (val * 9/5) + 32
            label = f"{val}°C = {round(result, 2)}°F"
        elif option == 'M to Ft':
            result = val * 3.28084
            label = f"{val}m = {round(result, 2)}ft"
        result_label.config(text=label)
        history.append(label)
    except:
        messagebox.showerror("Error", "Invalid input for conversion.")

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("History")
    history_window.geometry("300x300")
    text = tk.Text(history_window, wrap=tk.WORD)
    text.pack(expand=True, fill="both")
    for h in history:
        text.insert(tk.END, h + '\n')

# GUI Setup
root = tk.Tk()
root.title("Smart Multi-Utility Calculator")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="#f0f0f0")

title = tk.Label(root, text="Smart Multi-Utility Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Entry Fields
entry1 = tk.Entry(root, width=20, font=("Arial", 12))
entry1.pack(pady=5)
entry2 = tk.Entry(root, width=20, font=("Arial", 12))
entry2.pack(pady=5)

# Button Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

# Basic Buttons
tk.Button(frame, text="+", width=5, command=lambda: calculate_basic('+')).grid(row=0, column=0, padx=5)
tk.Button(frame, text="-", width=5, command=lambda: calculate_basic('-')).grid(row=0, column=1, padx=5)
tk.Button(frame, text="*", width=5, command=lambda: calculate_basic('*')).grid(row=0, column=2, padx=5)
tk.Button(frame, text="/", width=5, command=lambda: calculate_basic('/')).grid(row=0, column=3, padx=5)

# Advanced Buttons
tk.Button(frame, text="Power", width=7, command=lambda: calculate_advanced("Power")).grid(row=1, column=0, pady=5)
tk.Button(frame, text="Sqrt", width=7, command=lambda: calculate_advanced("Sqrt")).grid(row=1, column=1, pady=5)
tk.Button(frame, text="Log", width=7, command=lambda: calculate_advanced("Log")).grid(row=1, column=2, pady=5)

# Trig Buttons
tk.Button(frame, text="sin", width=5, command=lambda: calculate_trig("sin")).grid(row=2, column=0)
tk.Button(frame, text="cos", width=5, command=lambda: calculate_trig("cos")).grid(row=2, column=1)
tk.Button(frame, text="tan", width=5, command=lambda: calculate_trig("tan")).grid(row=2, column=2)

# BMI & Unit
tk.Button(root, text="Calculate BMI", width=20, command=calculate_bmi).pack(pady=5)
tk.Button(root, text="Celsius to Fahrenheit", width=20, command=lambda: unit_convert("C to F")).pack(pady=5)
tk.Button(root, text="Meters to Feet", width=20, command=lambda: unit_convert("M to Ft")).pack(pady=5)

# Result Label
result_label = tk.Label(root, text="Result:", font=("Arial", 14), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

# History Button
tk.Button(root, text="Show History", width=20, command=show_history).pack(pady=5)

# Exit
tk.Button(root, text="Exit", width=10, command=root.destroy).pack(pady=10)

root.mainloop()
