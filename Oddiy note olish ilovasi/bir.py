import tkinter as tk

def note_qoshish():
    note = note_entry.get()
    if note:
        text_area.insert(tk.END, note + "\n")
        note_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Oddiy Note Olish Ilovasi")

note_entry = tk.Entry(root, width=50)
note_entry.pack(pady=10)

save_button = tk.Button(root, text="Saqlash", command=note_qoshish)
save_button.pack(pady=10)

text_area = tk.Text(root, width=50, height=10)
text_area.pack(pady=10)

root.mainloop()