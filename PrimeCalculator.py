import tkinter as tk
from tkinter import ttk

def get_factors(n):
    #Returns a list of factors for the number n
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

def is_valid_input(value):
    #Check if the input value is a non-negative integer.
    try:
        #if num is non-negative, this line will return True
        return value >= 0
    except ValueError:
        return False

def calculate():
    #if check prime and factors selected
    if selected_option.get() == "check":
        # get the number from the input box
        num = int(number_entry.get())

        if not is_valid_input(num):
            result_label.config(text="Invalid input! Please enter a non-negative integer.")
            return

        factors = get_factors(num)

        # if the number is prime, it will only have 2 factors: 1 and itself
        if len(factors) == 2:
            result_label.config(text="Prime!")
        else:
            result_label.config(text=f"Factors: {', '.join(map(str, factors))}")

    #if check range selected
    elif selected_option.get() == "range":
        min_val = int(min_entry.get())
        max_val = int(max_entry.get())

        if not is_valid_input(min_val) or not is_valid_input(max_val):
            result_label.config(text="Invalid input! Please enter non-negative integers.")
            return

        primes = []

        for i in range(min_val, max_val + 1):
            if len(get_factors(i)) == 2:
                primes.append(str(i))

        result_label.config(text=f"Primes in range: {', '.join(primes)}")

def update_entries():
    if selected_option.get() == "check":
        number_entry.grid(row=2, column=1)
        number_label.grid(row=2, column=0)

        min_entry.grid_remove()
        min_label.grid_remove()
        max_entry.grid_remove()
        max_label.grid_remove()
    else:
        min_entry.grid(row=2, column=1)
        min_label.grid(row=2, column=0)
        max_entry.grid(row=3, column=1)
        max_label.grid(row=3, column=0)

        number_entry.grid_remove()
        number_label.grid_remove()

app = tk.Tk()
app.title("Prime Number Calculator")

title_label = ttk.Label(app, text="Prime Number Calculator", font=("Arial", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

selected_option = tk.StringVar(value="check")

check_prime_btn = ttk.Radiobutton(app, text="Check Prime and Factors", variable=selected_option, value="check", command=update_entries)
check_prime_btn.grid(row=1, column=0, sticky=tk.W, padx=10)

range_prime_btn = ttk.Radiobutton(app, text="Prime Numbers in Range", variable=selected_option, value="range", command=update_entries)
range_prime_btn.grid(row=1, column=1, sticky=tk.W, padx=10)

# Entry and label for single number
number_label = ttk.Label(app, text="Number:")
number_entry = ttk.Entry(app)
number_label.grid(row=2, column=0)
number_entry.grid(row=2, column=1)

# Entry and labels for min and max range
min_label = ttk.Label(app, text="Min:")
min_entry = ttk.Entry(app)

max_label = ttk.Label(app, text="Max:")
max_entry = ttk.Entry(app)

calculate_btn = ttk.Button(app, text="Calculate", command=calculate)
calculate_btn.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(app, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

app.mainloop()
