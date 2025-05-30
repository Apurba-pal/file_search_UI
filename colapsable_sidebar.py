import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Collapsible Navigation Bar")
        self.geometry("800x500")

        self.sidebar_expanded = True  # Track sidebar state

        # ===== Main layout =====
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar Frame
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsw")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)  # Push collapse button down

        # Sidebar content
        self.tab1_btn = ctk.CTkButton(self.sidebar_frame, text="Tab 1", width=180, anchor="w", command=lambda: self.show_tab(1))
        self.tab2_btn = ctk.CTkButton(self.sidebar_frame, text="Tab 2", width=180, anchor="w", command=lambda: self.show_tab(2))
        self.tab3_btn = ctk.CTkButton(self.sidebar_frame, text="Tab 3", width=180, anchor="w", command=lambda: self.show_tab(3))
        self.toggle_btn = ctk.CTkButton(self.sidebar_frame, text="<<", width=180, command=self.toggle_sidebar)

        self.tab1_btn.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
        self.tab2_btn.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.tab3_btn.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.toggle_btn.grid(row=6, column=0, padx=10, pady=10, sticky="sew")

        # Main content frame
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.content_label = ctk.CTkLabel(self.content_frame, text="Welcome! Click a tab.", font=ctk.CTkFont(size=20))
        self.content_label.pack(pady=20)

        self.show_tab(1)


    def toggle_sidebar(self):
        if self.sidebar_expanded:
            new_width = 50
            self.tab1_btn.configure(text="", width=new_width)
            self.tab2_btn.configure(text="", width=new_width)
            self.tab3_btn.configure(text="", width=new_width)
            self.toggle_btn.configure(text=">>", width=new_width)
        else:
            new_width = 180
            self.tab1_btn.configure(text="Tab 1", width=new_width)
            self.tab2_btn.configure(text="Tab 2", width=new_width)
            self.tab3_btn.configure(text="Tab 3", width=new_width)
            self.toggle_btn.configure(text="<<", width=new_width)
        self.sidebar_frame.configure(width=new_width + 20)
        self.sidebar_expanded = not self.sidebar_expanded

    def show_tab(self, tab_number):
        self.content_label.configure(text=f"You selected Tab {tab_number}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
