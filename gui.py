import tkinter as tk
from tkinter import ttk, messagebox
from processing import analyze


def run_analysis():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Vui lòng nhập tiếng Trung")
        return

    result = analyze(text)

    output.set(
        f"Số chữ Hán: {result['characters']}\n"
        f"Số từ: {result['words']}\n"
        f"Phân bố level: {result['level_distribution']}\n"
        f"Ước lượng HSK: {result['estimated_level']}\n"
        f"Cảnh báo: {result['warning']}"
    )

# ===== GUI =====
root = tk.Tk()
root.title("HSK Text Analyzer")
root.geometry("520x420")

ttk.Label(root, text="Nhập đoạn tiếng Trung:", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)

input_text = tk.Text(root, height=6)
input_text.pack(fill="x", padx=10)

ttk.Button(root, text="Phân tích", command=run_analysis).pack(pady=10)

output = tk.StringVar()
ttk.Label(root, textvariable=output, justify="left", font=("Consolas", 10)).pack(anchor="w", padx=10)

root.mainloop()
