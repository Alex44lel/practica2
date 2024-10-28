import tkinter as tk
from tkinter import messagebox


class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        self.root.geometry("1200x600")

        # User list frame
        self.user_list_frame = tk.Frame(
            self.root, bg="lightgray")
        self.user_list_frame.pack(
            side=tk.LEFT, fill=tk.Y, expand=False)

        # TODO: Load users from database
        self.users = ["Alice", "Bob", "Charlie charlie charlie", "Dave"]
        # self.user_buttons = []

        tk.Label(self.user_list_frame, text="Available users",
                 bg="lightgray", font=("Vedana", 11, "bold")).pack(pady=10)
        for user in self.users:
            button = tk.Button(self.user_list_frame, text=user,
                               command=lambda u=user: self.load_chat(u))
            button.pack(fill=tk.X, pady=0, padx=20)
            # self.user_buttons.append(button)

        # Chat display frame
        self.chat_display_frame = tk.Frame(self.root, bg="white")
        self.chat_display_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.chat_label = tk.Label(
            self.chat_display_frame, text="Select a user to start chatting", bg="white", font=("Vedana", 14, "bold"))
        self.chat_label.pack(pady=10)

        self.chat_text = tk.Text(
            self.chat_display_frame, state=tk.DISABLED, wrap=tk.WORD, relief="solid", bd=1)
        self.chat_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Message entry frame
        self.message_frame = tk.Frame(self.chat_display_frame, bg="white")
        self.message_frame.pack(fill=tk.X, padx=10, pady=7)

        self.message_entry = tk.Text(
            self.message_frame, relief="solid", bd=1, height=3)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

        self.send_button = tk.Button(
            self.message_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        self.current_user = None

    def load_chat(self, user):
        self.current_user = user
        self.chat_label.config(text=f"Chat with {user}")
        self.chat_text.yview(tk.END)

        # TODO: Load chats from database

        # Clear the chat text widget
        # self.chat_text.config(state=tk.NORMAL)
        # self.chat_text.delete(1.0, tk.END)

        # # Example: Load some previous messages (for demo purposes)
        # self.chat_text.insert(tk.END, f"{user}: Hello!\n", ("user",))
        # self.chat_text.insert(tk.END, f"You: Hi {user}!\n", ("you",))
        # self.chat_text.config(state=tk.DISABLED)

    def add_message_to_chat(self):
        # TODO: Listens from the websocket to add new received messages
        pass

    def send_message(self):
        if self.current_user is None:
            messagebox.showwarning(
                "Warning", "You need to select an user first.")
            return

        message = self.message_entry.get("1.0", "end-1c")

        if message:
            self.chat_text.config(state=tk.NORMAL)
            self.chat_text.insert(tk.END, f"You: {message}\n", ("you",))
            self.chat_text.config(state=tk.DISABLED)

        # this is used to scroll to the end of the chat
        self.chat_text.yview(tk.END)
        # TODO: Send message to the other user


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)

    # Tag configurations for different users
    app.chat_text.tag_configure("you", foreground="blue")
    app.chat_text.tag_configure("user", foreground="green")

    root.mainloop()
