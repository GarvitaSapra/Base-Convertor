import tkinter as tk
from tkinter import ttk

def convert_number():
    number = entry_number.get()
    from_base = int(entry_from_base.get())
    to_base = int(entry_to_base.get())

    try:
        # Convert number to base 10
        base_10_number = int(str(number), from_base)
        
        # Convert base 10 number to target base
        converted_number = ''
        while base_10_number > 0:
            remainder = base_10_number % to_base
            converted_number = str(remainder) + converted_number
            base_10_number //= to_base
        
        entry_result.delete(0, tk.END)
        entry_result.insert(0, converted_number)
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Number Converter")
root.configure(bg="purple") 
root.geometry("250x200")   
frame_input = ttk.Frame(root, padding=(20, 10))
frame_input.grid(row=0, column=0)

# Create input fields
label_number = ttk.Label(root, text="Number:")
label_number.grid(row=0, column=0, padx=5, pady=5)
entry_number = ttk.Entry(root)
entry_number.grid(row=0, column=1, padx=5, pady=5)

label_from_base = ttk.Label(root, text="From Base:")
label_from_base.grid(row=1, column=0, padx=5, pady=5)
entry_from_base = ttk.Entry(root)
entry_from_base.grid(row=1, column=1, padx=5, pady=5)

label_to_base = ttk.Label(root, text="To Base:")
label_to_base.grid(row=2, column=0, padx=5, pady=5)
entry_to_base = ttk.Entry(root)
entry_to_base.grid(row=2, column=1, padx=5, pady=5)

# Create the convert button
convert_button = ttk.Button(root, text="Convert", command=convert_number)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create result field
label_result = ttk.Label(root, text="Result:")
label_result.grid(row=4, column=0, padx=5, pady=5)
entry_result = ttk.Entry(root)
entry_result.grid(row=4, column=1, padx=5, pady=5)

# Run the main event loop
root.mainloop()



dec_number= int(input("Enter a number you want to Convert:"))
bi_number= number_to_bin(dec_number)
print("BINARY REPRESENTATION of ",dec_number, "is:",  bi_number) 
"""
