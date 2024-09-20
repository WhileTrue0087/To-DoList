import customtkinter as ctk

class ScrollableFrame(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.canvas = ctk.CTkCanvas(self)
        self.scrollbar = ctk.CTkScrollbar(self, orientation="horizontal", command=self.canvas.xview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="bottom", fill="x")
        
    def add_widget(self, widget):
        widget.pack(side="left")  # Add widgets to the scrollable frame

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Scrollable Frame Example")

    scrollable_frame = ScrollableFrame(app)
    scrollable_frame.pack(fill="both", expand=True)

    # Add some example widgets
    for i in range(20):
        button = ctk.CTkButton(scrollable_frame.scrollable_frame, text=f"Button {i+1}")
        scrollable_frame.add_widget(button)

    app.mainloop()
