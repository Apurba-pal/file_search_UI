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
file_listbox = ctk.CTkTextbox(file_add_frame, height=60, width=600)
file_listbox.pack(side="left", fill="x", expand=True)
file_listbox.configure(state="disabled")

# --- Add File Button ---
def add_file():
    path = fd.askopenfilename()
    if path and path not in file_list:
        file_list.append(path)
        file_listbox.configure(state="normal")
        file_listbox.insert("end", os.path.basename(path) + "\n")
        file_listbox.configure(state="disabled")

add_file_button = ctk.CTkButton(file_add_frame, text="Add File", command=add_file, width=100)
add_file_button.pack(side="left", padx=(10, 5))

# --- Add Folder Button ---
def add_folder():
    folder_path = fd.askdirectory()
    if folder_path:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                if full_path not in file_list:
                    file_list.append(full_path)
                    file_listbox.configure(state="normal")
                    relative_path = os.path.relpath(full_path, folder_path)
                    file_listbox.insert("end", f"{os.path.basename(folder_path)}/{relative_path}\n")
                    file_listbox.configure(state="disabled")

add_folder_button = ctk.CTkButton(file_add_frame, text="Add Folder", command=add_folder, width=100)
add_folder_button.pack(side="left")

# --- Terminal (Non-editable log view) ---
terminal = ctk.CTkTextbox(app)
terminal.pack(side="right", fill="both", expand=True, padx=10, pady=10)
terminal.configure(state="disabled")

# --- Submit Button ---
def submit_files():
    global submitted_files
    submitted_files = file_list.copy()
    update_dropdown()

    # Terminal output
    terminal.configure(state="normal")
    terminal.delete("1.0", "end")
    folder_map = {}

    # Map each file to its folder
    for path in submitted_files:
        folder = os.path.dirname(path)
        folder_map.setdefault(folder, []).append(path)

    for folder, files in folder_map.items():
        folder_name = os.path.basename(folder)
        if len(files) > 1:
            terminal.insert("end", f"Analyzing {folder_name}...\n")
        for file_path in files:
            filename = os.path.basename(file_path)
            relative = os.path.relpath(file_path, folder)
            terminal.insert("end", f"Analyzing {folder_name}/{relative}\n")

    terminal.configure(state="disabled")

    # Clear file list display
    file_listbox.configure(state="normal")
    file_listbox.delete("1.0", "end")
    file_listbox.configure(state="disabled")

    file_list.clear()

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

# Frame to hold dropdown and open button
file_dropdown_frame = ctk.CTkFrame(main_frame)
file_dropdown_frame.pack(padx=10, pady=(10, 0), fill="x")

dropdown = ctk.CTkOptionMenu(file_dropdown_frame, variable=selected_file, command=on_file_select)
dropdown.pack(side="left", fill="x", expand=True)
dropdown.set("No file submitted yet")

def open_in_folder():
    # Find the full path of the selected file
    selected = selected_file.get()
    for f in submitted_files:
        if os.path.basename(f) == selected:
            folder = os.path.dirname(f)
            os.startfile(folder)
            break

open_button = ctk.CTkButton(file_dropdown_frame, text="Open in Folder", command=open_in_folder)
open_button.pack(side="left", padx=(10, 0))

# --- AI Summary and Chat Section ---
summary_chat_frame = ctk.CTkFrame(main_frame)
summary_chat_frame.pack(padx=10, pady=(10, 0), fill="both", expand=True)



# --- Summary Display ---
summary_box = ctk.CTkTextbox(summary_chat_frame, height=300)
summary_box.pack(padx=5, pady=(5, 0), fill="x")
summary_box.configure(state="disabled")

save_button = ctk.CTkButton(summary_chat_frame, text="Save")
save_button.pack(anchor="ne", padx=5, pady=5)

# --- Chat Box ---
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

# Run the app
app.mainloop()
