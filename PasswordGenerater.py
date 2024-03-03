import tkinter as tk
import random
import string


def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Invalid length")
        return

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create labels and entry widgets
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
