import tkinter as tk

def submit_form():
    ism = ism_entry.get()
    elektron_pochta = email_entry.get()
    tarjimai_hol = tarjimai_hol_text.get("1.0", tk.END)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Ism: {ism}\n")
    output_text.insert(tk.END, f"Elektron Pochta: {elektron_pochta}\n")
    output_text.insert(tk.END, f"Tarjimai Hol:\n{tarjimai_hol}")

root = tk.Tk()
root.title("Ma'lumot Formasi")

tk.Label(root, text="Ism:").pack()
ism_entry = tk.Entry(root)
ism_entry.pack()

tk.Label(root, text="Elektron Pochta:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Qisqacha Tarjimai Hol:").pack()
tarjimai_hol_text = tk.Text(root, height=5, width=40)
tarjimai_hol_text.pack()

submit_button = tk.Button(root, text="Yuborish", command=submit_form)
submit_button.pack()

tk.Label(root, text="Olingan Ma'lumotlar:").pack()
output_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
output_text.pack()

root.mainloop()