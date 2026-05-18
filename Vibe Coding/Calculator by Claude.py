# ─────────────────────────────────────────────
#  Calculator  –  Fixed Layout
# ─────────────────────────────────────────────

from tkinter import Tk, Label, Button, Frame


class Calculator:

    BUTTONS = [
        ("C",  0, 0, 1, "clear"),
        ("±",  0, 1, 1, "func"),
        ("%",  0, 2, 1, "func"),
        ("÷",  0, 3, 1, "op"),

        ("7",  1, 0, 1, "digit"),
        ("8",  1, 1, 1, "digit"),
        ("9",  1, 2, 1, "digit"),
        ("×",  1, 3, 1, "op"),

        ("4",  2, 0, 1, "digit"),
        ("5",  2, 1, 1, "digit"),
        ("6",  2, 2, 1, "digit"),
        ("−",  2, 3, 1, "op"),

        ("1",  3, 0, 1, "digit"),
        ("2",  3, 1, 1, "digit"),
        ("3",  3, 2, 1, "digit"),
        ("+",  3, 3, 1, "op"),

        ("0",  4, 0, 2, "digit"),
        (".",  4, 2, 1, "digit"),
        ("=",  4, 3, 1, "equals"),
    ]

    COLORS = {
        "bg":     "#1c1c1e",
        "digit":  "#2c2c2e",
        "op":     "#ff9f0a",
        "func":   "#636366",
        "clear":  "#636366",
        "equals": "#ff9f0a",
        "fg":     "#ffffff",
        "expr":   "#8e8e93",
    }

    KEY_MAP = {
        "0":"0","1":"1","2":"2","3":"3","4":"4",
        "5":"5","6":"6","7":"7","8":"8","9":"9",
        ".":".",
        "+":"+", "-":"−", "*":"×", "/":"÷",
        "Return":"=", "Escape":"C",
        "c":"C", "percent":"%",
    }

    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg=self.COLORS["bg"])

        self._current        = "0"
        self._expression     = ""
        self._first          = None
        self._operator       = None
        self._just_evaluated = False

        self._build_ui()
        self._bind_keyboard()

    # ── Build UI ──────────────────────────────

    def _build_ui(self):
        # Root has ONE column; display and button frame stack vertically
        self.root.columnconfigure(0, weight=1)

        # ── Display ──
        disp = Frame(self.root, bg=self.COLORS["bg"], padx=16, pady=16)
        disp.grid(row=0, column=0, sticky="ew")
        disp.columnconfigure(0, weight=1)

        self.expr_label = Label(
            disp, text="", anchor="e",
            bg=self.COLORS["bg"], fg=self.COLORS["expr"],
            font=("Courier", 15),
        )
        self.expr_label.grid(row=0, column=0, sticky="ew")

        self.result_label = Label(
            disp, text="0", anchor="e",
            bg=self.COLORS["bg"], fg=self.COLORS["fg"],
            font=("Courier", 38, "bold"),
        )
        self.result_label.grid(row=1, column=0, sticky="ew")

        # ── Button grid ──
        btn_frame = Frame(self.root, bg=self.COLORS["bg"])
        btn_frame.grid(row=1, column=0, sticky="ew")

        # 4 equal columns
        for c in range(4):
            btn_frame.columnconfigure(c, weight=1, uniform="col")

        for label, row, col, colspan, style in self.BUTTONS:
            bg = self.COLORS[style]
            btn = Button(
                btn_frame,
                text=label,
                bg=bg, fg=self.COLORS["fg"],
                activebackground=self._lighten(bg),
                activeforeground=self.COLORS["fg"],
                font=("Courier", 18, "bold"),
                relief="flat", bd=0,
                # NO width/height — let the grid size them
                padx=20, pady=18,
                command=lambda lbl=label: self._on_button(lbl),
            )
            btn.grid(
                row=row, column=col,
                columnspan=colspan,
                padx=2, pady=2,
                sticky="nsew",
            )

    def _bind_keyboard(self):
        for key, label in self.KEY_MAP.items():
            self.root.bind(f"<KeyPress-{key}>",
                           lambda e, lbl=label: self._on_button(lbl))

    # ── Logic ─────────────────────────────────

    def _on_button(self, label):
        if label.isdigit() or label == ".":
            self._input_digit(label)
        elif label in ("+", "−", "×", "÷"):
            self._set_operator(label)
        elif label == "=":
            self._evaluate()
        elif label == "C":
            self._clear()
        elif label == "±":
            self._negate()
        elif label == "%":
            self._percent()

    def _input_digit(self, char):
        if self._just_evaluated:
            self._current        = ""
            self._just_evaluated = False
        if char == "." and "." in self._current:
            return
        if self._current in ("0", "") and char != ".":
            self._current = char
        else:
            if len(self._current) >= 12:
                return
            self._current += char
        self._refresh()

    def _set_operator(self, op):
        if self._operator and not self._just_evaluated:
            self._evaluate(chain=True)
        self._first          = float(self._current)
        self._operator       = op
        self._expression     = f"{self._fmt(self._first)} {op}"
        self._current        = "0"
        self._just_evaluated = False
        self._refresh()

    def _evaluate(self, chain=False):
        if self._operator is None or self._first is None:
            return
        second = float(self._current)
        op     = self._operator
        if op == "÷" and second == 0:
            self._current    = "Error"
            self._expression = ""
            self._operator   = None
            self._first      = None
            self._refresh()
            return
        result = {
            "+": lambda a, b: a + b,
            "−": lambda a, b: a - b,
            "×": lambda a, b: a * b,
            "÷": lambda a, b: a / b,
        }[op](self._first, second)
        if not chain:
            self._expression     = f"{self._fmt(self._first)} {op} {self._fmt(second)} ="
            self._just_evaluated = True
        self._current  = self._fmt(result)
        self._operator = None
        self._first    = None
        self._refresh()

    def _clear(self):
        self._current        = "0"
        self._first          = None
        self._operator       = None
        self._expression     = ""
        self._just_evaluated = False
        self._refresh()

    def _negate(self):
        if self._current not in ("0", "Error"):
            self._current = self._fmt(-float(self._current))
            self._refresh()

    def _percent(self):
        if self._current not in ("0", "Error"):
            self._current = self._fmt(float(self._current) / 100)
            self._refresh()

    # ── Helpers ───────────────────────────────

    def _fmt(self, value):
        if isinstance(value, str):
            return value
        if value == int(value) and abs(value) < 1e12:
            return str(int(value))
        return f"{value:.10g}"

    def _refresh(self):
        self.expr_label.config(text=self._expression)
        self.result_label.config(text=self._current)

    @staticmethod
    def _lighten(hex_color):
        h = hex_color.lstrip("#")
        r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
        return "#{:02x}{:02x}{:02x}".format(
            min(r+40, 255), min(g+40, 255), min(b+40, 255))


# ── Entry point ───────────────────────────────

if __name__ == "__main__":
    root = Tk()
    Calculator(root)
    root.mainloop()