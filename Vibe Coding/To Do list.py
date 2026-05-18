# ─────────────────────────────────────────────
#  To Do List App
#  Built with Python + Tkinter
# ─────────────────────────────────────────────

from tkinter import Tk, Label, Entry, Button, Listbox, Frame, Scrollbar, StringVar, messagebox, END, SINGLE


# ── All colors used in the app ──
BG_COLOR       = "#1e1e2e"   # dark background
PANEL_COLOR    = "#2a2a3e"   # slightly lighter panels
ACCENT_COLOR   = "#7c6af7"   # purple accent
DONE_COLOR     = "#3a9e6f"   # green for completed
DELETE_COLOR   = "#e05c6a"   # red for delete
TEXT_COLOR     = "#ffffff"   # white text
MUTED_COLOR    = "#888aaa"   # grey muted text
ENTRY_BG       = "#33334a"   # input box background


class ToDoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        # This list stores all tasks as dictionaries
        # Each task looks like: {"text": "Buy milk", "done": False}
        self.tasks = []

        self.build_ui()

    # ── Build the whole UI ─────────────────────

    def build_ui(self):

        # ── Title at the top ──
        title = Label(
            self.root,
            text="My To Do List",
            bg=BG_COLOR, fg=TEXT_COLOR,
            font=("Courier", 22, "bold"),
            pady=20,
        )
        title.pack()

        # ── Input area (text box + Add button) ──
        input_frame = Frame(self.root, bg=BG_COLOR, pady=10)
        input_frame.pack(padx=20, fill="x")

        self.task_input = Entry(
            input_frame,
            bg=ENTRY_BG, fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,   # cursor color
            font=("Courier", 14),
            relief="flat",
            bd=8,
        )
        self.task_input.pack(side="left", fill="x", expand=True, ipady=6)
        self.task_input.bind("<Return>", lambda e: self.add_task())  # press Enter to add

        add_btn = Button(
            input_frame,
            text="Add",
            bg=ACCENT_COLOR, fg=TEXT_COLOR,
            font=("Courier", 14, "bold"),
            relief="flat", bd=0,
            padx=16, pady=6,
            cursor="hand2",
            command=self.add_task,
        )
        add_btn.pack(side="left", padx=(8, 0))

        # ── Stats row: shows how many tasks done ──
        self.stats_label = Label(
            self.root,
            text="0 of 0 tasks completed",
            bg=BG_COLOR, fg=MUTED_COLOR,
            font=("Courier", 11),
        )
        self.stats_label.pack(pady=(0, 8))

        # ── Task list ──
        list_frame = Frame(self.root, bg=BG_COLOR)
        list_frame.pack(padx=20, fill="both", expand=True)

        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(
            list_frame,
            bg=PANEL_COLOR, fg=TEXT_COLOR,
            font=("Courier", 13),
            relief="flat", bd=0,
            selectmode=SINGLE,
            selectbackground=ACCENT_COLOR,
            selectforeground=TEXT_COLOR,
            activestyle="none",
            yscrollcommand=scrollbar.set,
            height=16,
        )
        self.listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.listbox.yview)

        # ── Bottom buttons ──
        btn_frame = Frame(self.root, bg=BG_COLOR, pady=14)
        btn_frame.pack()

        done_btn = Button(
            btn_frame,
            text="Mark Done",
            bg=DONE_COLOR, fg=TEXT_COLOR,
            font=("Courier", 12, "bold"),
            relief="flat", bd=0,
            padx=14, pady=8,
            cursor="hand2",
            command=self.mark_done,
        )
        done_btn.pack(side="left", padx=6)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            bg=DELETE_COLOR, fg=TEXT_COLOR,
            font=("Courier", 12, "bold"),
            relief="flat", bd=0,
            padx=14, pady=8,
            cursor="hand2",
            command=self.delete_task,
        )
        delete_btn.pack(side="left", padx=6)

        clear_btn = Button(
            btn_frame,
            text="Clear All",
            bg=MUTED_COLOR, fg=TEXT_COLOR,
            font=("Courier", 12, "bold"),
            relief="flat", bd=0,
            padx=14, pady=8,
            cursor="hand2",
            command=self.clear_all,
        )
        clear_btn.pack(side="left", padx=6)

    # ── Actions ───────────────────────────────

    def add_task(self):
        """Read the input box and add a new task."""
        text = self.task_input.get().strip()

        if text == "":
            messagebox.showwarning("Empty Task", "Please type a task first!")
            return

        # Add to our tasks list
        self.tasks.append({"text": text, "done": False})

        # Clear the input box
        self.task_input.delete(0, END)

        # Refresh what's shown on screen
        self.refresh_list()

    def mark_done(self):
        """Toggle the selected task between done and not done."""
        selected = self.listbox.curselection()

        if not selected:
            messagebox.showinfo("No Selection", "Please click a task first!")
            return

        index = selected[0]

        # Flip done → not done, or not done → done
        self.tasks[index]["done"] = not self.tasks[index]["done"]

        self.refresh_list()

        # Keep the same item selected after refresh
        self.listbox.selection_set(index)

    def delete_task(self):
        """Remove the selected task."""
        selected = self.listbox.curselection()

        if not selected:
            messagebox.showinfo("No Selection", "Please click a task to delete!")
            return

        index = selected[0]
        task_name = self.tasks[index]["text"]

        # Ask the user to confirm before deleting
        confirm = messagebox.askyesno("Delete Task", f'Delete "{task_name}"?')
        if confirm:
            self.tasks.pop(index)
            self.refresh_list()

    def clear_all(self):
        """Delete every task after confirmation."""
        if not self.tasks:
            messagebox.showinfo("Nothing to clear", "Your list is already empty!")
            return

        confirm = messagebox.askyesno("Clear All", "Delete ALL tasks? This cannot be undone.")
        if confirm:
            self.tasks.clear()
            self.refresh_list()

    # ── Helper: redraw the list ───────────────

    def refresh_list(self):
        """Clear the listbox and redraw every task from self.tasks."""

        # Remove everything currently shown
        self.listbox.delete(0, END)

        done_count = 0

        for task in self.tasks:
            if task["done"]:
                # Show completed tasks with a checkmark and different color
                self.listbox.insert(END, f"  ✔  {task['text']}")
                self.listbox.itemconfig(END, fg=DONE_COLOR)
                done_count += 1
            else:
                # Show pending tasks with a bullet
                self.listbox.insert(END, f"  •  {task['text']}")
                self.listbox.itemconfig(END, fg=TEXT_COLOR)

        # Update the stats label
        total = len(self.tasks)
        self.stats_label.config(text=f"{done_count} of {total} tasks completed")


# ── Run the app ───────────────────────────────

if __name__ == "__main__":
    root = Tk()
    ToDoApp(root)
    root.mainloop()