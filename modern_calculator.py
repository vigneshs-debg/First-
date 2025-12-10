import tkinter as tk
from tkinter import ttk

# ---------- COLORS & STYLES ----------
BG_COLOR = "#111827"       # window background (dark blue/black)
DISPLAY_BG = "#020617"     # display background
DISPLAY_FG = "#e5e7eb"     # display text
BTN_BG = "#1f2937"         # normal button bg
BTN_FG = "#e5e7eb"         # button text
ACCENT_BG = "#2563eb"      # = button bg (blue)
ACCENT_FG = "#f9fafb"      # = button text
DANGER_BG = "#ef4444"      # C button (red)

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("340x480")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# ---------- STYLE ----------
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Calc.TButton",
    background=BTN_BG,
    foreground=BTN_FG,
    font=("Segoe UI", 14),
    padding=(10, 8),
    borderwidth=0,
)
style.map(
    "Calc.TButton",
    background=[("active", "#374151")]
)

style.configure(
    "Accent.Calc.TButton",
    background=ACCENT_BG,
    foreground=ACCENT_FG,
)
style.map(
    "Accent.Calc.TButton",
    background=[("active", "#1d4ed8")]
)

style.configure(
    "Danger.Calc.TButton",
    background=DANGER_BG,
    foreground=ACCENT_FG,
)
style.map(
    "Danger.Calc.TButton",
    background=[("active", "#b91c1c")]
)

# ---------- DISPLAY ----------
display_frame = tk.Frame(root, bg=BG_COLOR)
display_frame.pack(fill="x", pady=(20, 10), padx=16)

display_var = tk.StringVar()
display = tk.Entry(
    display_frame,
    textvariable=display_var,
    font=("Segoe UI", 26),
    bd=0,
    bg=DISPLAY_BG,
    fg=DISPLAY_FG,
    insertbackground=DISPLAY_FG,
    relief="flat",
    justify="right"
)
display.pack(fill="both", ipady=16)
display_var.set("0")

# ---------- FUNCTIONS ----------
def append_to_display(value):
    current = display_var.get()
    if current == "0" and value not in (".", "%"):
        current = ""
    display_var.set(current + value)

def clear_display():
    display_var.set("0")

def backspace():
    current = display_var.get()
    if len(current) > 1:
        display_var.set(current[:-1])
    else:
        display_var.set("0")

def calculate():
    expression = display_var.get().replace("×", "*").replace("÷", "/")
    try:
        result = eval(expression)
        display_var.set(str(result))
    except Exception:
        display_var.set("Error")

# ---------- BUTTONS LAYOUT ----------
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(expand=True, fill="both", padx=12, pady=(0, 16))

buttons = [
    ("C", 0, 0, "Danger.Calc.TButton", clear_display),
    ("⌫", 0, 1, "Calc.TButton", backspace),
    ("%", 0, 2, "Calc.TButton", lambda: append_to_display("%")),
    ("÷", 0, 3, "Calc.TButton", lambda: append_to_display("÷")),

    ("7", 1, 0, "Calc.TButton", lambda: append_to_display("7")),
    ("8", 1, 1, "Calc.TButton", lambda: append_to_display("8")),
    ("9", 1, 2, "Calc.TButton", lambda: append_to_display("9")),
    ("×", 1, 3, "Calc.TButton", lambda: append_to_display("×")),

    ("4", 2, 0, "Calc.TButton", lambda: append_to_display("4")),
    ("5", 2, 1, "Calc.TButton", lambda: append_to_display("5")),
    ("6", 2, 2, "Calc.TButton", lambda: append_to_display("6")),
    ("-", 2, 3, "Calc.TButton", lambda: append_to_display("-")),

    ("1", 3, 0, "Calc.TButton", lambda: append_to_display("1")),
    ("2", 3, 1, "Calc.TButton", lambda: append_to_display("2")),
    ("3", 3, 2, "Calc.TButton", lambda: append_to_display("3")),
    ("+", 3, 3, "Calc.TButton", lambda: append_to_display("+")),

    ("0", 4, 0, "Calc.TButton", lambda: append_to_display("0")),
    (".", 4, 1, "Calc.TButton", lambda: append_to_display(".")),
    ("=", 4, 2, "Accent.Calc.TButton", calculate),
]

for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
for j in range(4):
    btn_frame.columnconfigure(j, weight=1)

for (text, row, col, style_name, cmd) in buttons:
    ttk.Button(
        btn_frame,
        text=text,
        style=style_name,
        command=cmd
    ).grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

# Make "=" button wide (2 columns)
btn_equal = ttk.Button(
    btn_frame,
    text="=",
    style="Accent.Calc.TButton",
    command=calculate
)
btn_equal.grid(row=4, column=2, columnspan=2, sticky="nsew", padx=4, pady=4)

root.mainloop()
