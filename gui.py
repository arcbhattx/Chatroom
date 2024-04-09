import tkinter as tk
from tkinter import scrolledtext

class ChatroomApp:
    def __init__(self, master):
        self.master = master
        master.title("Chatroom")

        # Create scrolled text widget to display messages
        self.chat_box = scrolledtext.ScrolledText(master, width=40, height=20)
        self.chat_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create entry widget for typing messages
        self.message_entry = tk.Entry(master, width=30)
        self.message_entry.grid(row=1, column=0, padx=10, pady=5)

        # Create send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=5)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.chat_box.insert(tk.END, "You: " + message + "\n")
            self.message_entry.delete(0, tk.END)

root = tk.Tk()
app = ChatroomApp(root)
root.mainloop()
