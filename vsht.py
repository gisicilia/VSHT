import tkinter as tk
from tkinter import messagebox

class HabitTracker:
    def __init__(self, master):
        self.master = master
        master.title("Habit Tracker")

        self.habits = []

        self.label = tk.Label(master, text="Enter a habit:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.add_button = tk.Button(master, text="Add Habit", command=self.add_habit)
        self.add_button.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.complete_habit)
        self.complete_button.pack()

    def add_habit(self):
        habit = self.entry.get()
        if habit:
            self.habits.append(habit)
            self.listbox.insert(tk.END, habit)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a habit.")

    def complete_habit(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
            completed_habit = self.habits.pop(selected_index[0])
            messagebox.showinfo("Success", f"You completed the habit: {completed_habit}")
        else:
            messagebox.showwarning("Warning", "Please select a habit to mark as completed.")

root = tk.Tk()
habit_tracker = HabitTracker(root)
root.mainloop()