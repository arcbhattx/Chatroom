import tkinter as tk

def on_button_click(user_input):
    # Retrieve text from the entry widget when the button is clicked
    user_input = entry.get()
    display_box.insert(tk.END, user_input + "\n")  # Insert the user's message into the display box

# Create the main window
window = tk.Tk()

# Set properties
window.title("Chat Window")  # Title of the window
window.geometry("400x400")  # Size of the window (width x height)
window.configure(bg="white")  # Background color of the window

# Create an entry widget
entry = tk.Entry(window)
entry.pack(pady=10, padx=10, fill=tk.X)  # Add some padding around the entry widget and fill it horizontally

# Create a button
button = tk.Button(window, text="Submit", command=on_button_click)
button.pack(pady=5)

# Create a display box
display_box = tk.Text(window, height=20, width=40)
display_box.pack(padx=10, pady=10)

# Run the event loop
window.mainloop()
