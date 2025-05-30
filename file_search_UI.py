import customtkinter as ctk
import tkinter.filedialog as fd
import os

# App setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Smart File Upload System")
app.geometry("1200x700")

# File lists
file_list = []
submitted_files = []

# --- Sidebar ---
sidebar = ctk.CTkFrame(app, width=150)
sidebar.pack(side="left", fill="y")

file_button = ctk.CTkButton(sidebar, text="File")
file_button.pack(pady=10)

search_button = ctk.CTkButton(sidebar, text="Search")
search_button.pack(pady=10)

collapse_button = ctk.CTkButton(sidebar, text="Collapse")
collapse_button.pack(side="bottom", pady=10)

# --- Main Content ---
main_frame = ctk.CTkFrame(app)
main_frame.pack(side="left", fill="both", expand=True)

# Container frame for file listbox and add button (horizontal layout)
file_add_frame = ctk.CTkFrame(main_frame)
file_add_frame.pack(padx=10, pady=(10, 0), fill="x")

# --- File list display (Read-only Textbox) ---
file_listbox = ctk.CTkTextbox(file_add_frame, height=60, width=600)  # Adjust width as needed
file_listbox.pack(side="left", fill="x", expand=True)
file_listbox.configure(state="disabled")

# --- Add Button (to pick file/folder) ---
def add_file_or_folder():
    path = fd.askopenfilename() or fd.askdirectory()
    if path and path not in file_list:
        file_list.append(path)
        file_listbox.configure(state="normal")
        file_listbox.insert("end", os.path.basename(path) + "\n")
        file_listbox.configure(state="disabled")

add_button = ctk.CTkButton(file_add_frame, text="Add File/Folder", command=add_file_or_folder, width=150)
add_button.pack(side="left", padx=(10, 0))

# --- Submit Button (to simulate upload & update dropdown) ---
def submit_files():
    global submitted_files
    submitted_files = file_list.copy()
    update_dropdown()

submit_button = ctk.CTkButton(main_frame, text="Submit", command=submit_files)
submit_button.pack(padx=10, pady=(10, 0), fill="x")

# --- Dropdown Menu for Submitted Files ---
selected_file = ctk.StringVar()

def update_dropdown():
    menu = [os.path.basename(f) for f in submitted_files]
    dropdown.configure(values=menu)
    if menu:
        dropdown.set(menu[0])

def on_file_select(choice):
    summary_box.configure(state="normal")
    summary_box.delete("1.0", "end")
    summary_box.insert("end", f"AI Summary of {choice}")
    summary_box.configure(state="disabled")

dropdown = ctk.CTkOptionMenu(main_frame, variable=selected_file, command=on_file_select)
dropdown.pack(padx=10, pady=(10, 0), fill="x")
dropdown.set("No file submitted yet")

# --- AI Summary and Chat Section ---
summary_chat_frame = ctk.CTkFrame(main_frame)
summary_chat_frame.pack(padx=10, pady=(10, 0), fill="both", expand=True)

# --- Summary Display (Non-editable) ---
summary_box = ctk.CTkTextbox(summary_chat_frame, height=100)
summary_box.pack(padx=5, pady=(5, 0), fill="x")
summary_box.configure(state="disabled")

save_button = ctk.CTkButton(summary_chat_frame, text="Save")
save_button.pack(anchor="ne", padx=5, pady=5)

# --- Chat Box Display (Non-editable) ---
chat_box = ctk.CTkTextbox(summary_chat_frame)
chat_box.pack(padx=5, pady=(0, 5), fill="both", expand=True)
chat_box.configure(state="disabled")

# --- Chat Input Area ---
chat_input_frame = ctk.CTkFrame(summary_chat_frame)
chat_input_frame.pack(fill="x", pady=(0, 10), padx=5)

chat_input = ctk.CTkEntry(chat_input_frame)
chat_input.pack(side="left", fill="x", expand=True, padx=(0, 10))

def send_chat():
    user_msg = chat_input.get()
    if user_msg:
        chat_box.configure(state="normal")
        chat_box.insert("end", f"You: {user_msg}\n")
        chat_box.insert("end", "AI: This is a sample response\n")
        chat_box.configure(state="disabled")
        chat_input.delete(0, "end")

send_button = ctk.CTkButton(chat_input_frame, text="Send", command=send_chat)
send_button.pack(side="right")

# --- Terminal (Non-editable log view) ---
terminal = ctk.CTkTextbox(app)
terminal.pack(side="right", fill="both", expand=True, padx=10, pady=10)
terminal.configure(state="disabled")

# Run the app
app.mainloop()
