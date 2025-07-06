import tkinter as tk
from tkinter import messagebox
import time
import random
from datetime import datetime
counter=60

texts = "The quick brown fox jumps over the lazy dog.,Practice makes perfect in every skill you learn.,Typing speed depends on accuracy and consistency.,Python is a popular programming language for beginners.Artificial intelligence is transforming the world rapidly."


class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("700x450")

        self.text_to_type = random.choice(texts)
        self.start_time = None
        self.time_left = counter

        # UI components
        self.title_label = tk.Label(root, text="Typing Speed Tester", font=("Helvetica", 20))
        self.title_label.pack(pady=10)

        self.text_label = tk.Label(root, text=texts, wraplength=600, font=("Helvetica", 14))
        self.text_label.pack(pady=10)

        self.timer_label = tk.Label(root, text=f"Time left: {self.time_left}s", font=("Helvetica", 14), fg="red")
        self.timer_label.pack(pady=5)

        self.entry = tk.Text(root, height=5, width=80, font=("Helvetica", 12))
        self.entry.pack(pady=10)
        self.entry.config(state=tk.DISABLED)

        self.start_button = tk.Button(root, text="Start", command=self.start_test, bg="green", fg="white",
                                      font=("Helvetica", 12))
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_test, bg="blue", fg="white",
                                      font=("Helvetica", 12))
        self.reset_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def start_test(self):
        self.entry.delete(1.0, tk.END)
        self.entry.config(state=tk.NORMAL)

        self.entry.focus()
        self.start_time = time.time()
        self.time_left = counter
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        self.result_label.config(text="")
        self.start_button.config(state=tk.DISABLED)

        self.countdown()

    def countdown(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.finish_test()

    def finish_test(self):
        self.entry.config(state=tk.DISABLED)
        elapsed_time = counter - self.time_left
        elapsed_minutes = elapsed_time / 60
        typed_text = self.entry.get(1.0, tk.END).strip()
        word_count = len(typed_text.split())
        wpm = int(word_count / elapsed_minutes) if elapsed_minutes > 0 else 0

    def save_score(self, elapsed_time, wpm, accuracy):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"{timestamp} | Time: {elapsed_time:.2f}s | WPM: {wpm} | Accuracy: {accuracy}%\n"
        try:
            with open("typing_scores.txt", "a") as f:
                f.write(record)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save score: {e}")

    def reset_test(self):
        self.text_to_type = texts
        self.text_label.config(text=self.text_to_type)
        self.entry.config(state=tk.DISABLED)
        self.entry.delete(1.0, tk.END)
        self.result_label.config(text="")
        self.timer_label.config(text="Time left: 60s")
        self.time_left = 60
        self.start_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
