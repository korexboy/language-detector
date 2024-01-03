import customtkinter
from customtkinter import messagebox


def detect_language():
    input_text = textbox.get()

    if not input_text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Language Detector")

label = customtkinter.CTkLabel(root, text="Language Detector System", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = customtkinter.CTkText(root, height=3, font=('Arial', 16))
textbox.pack(padx=30, pady=30)

button = customtkinter.CTkButton(root, text="Detect Language", command=detect_language)
button.pack()

output_label = customtkinter.CTkLabel(root, text="", font=("Arial", 12))
output_label.pack(pady=10)

root.mainloop()