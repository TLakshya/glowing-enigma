import tkinter as tk
import random

class Breakout:
    def __init__(self, root):
        self.root = root
        self.counter = 0
        self.root.title("Breakout Game")

        self.canvas = tk.Canvas(root, width=500, height=400, bg='black')
        self.canvas.pack()

        self.paddle = self.canvas.create_rectangle(200, 380, 300, 390, fill='white')
        self.ball = self.canvas.create_oval(240, 360, 260, 380, fill='red')
        self.ball_dx = random.choice([-3, 3])
        self.ball_dy = -3

        self.bricks = []
        self.create_bricks()

        # Score label
        self.score_label = tk.Label(root, text=f"Score: {self.counter}", font=("Arial", 16), fg="blue")
        self.score_label.pack()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.game_running = True
        self.update_game()

    def create_bricks(self):
        colors = ['blue', 'green', 'yellow', 'orange', 'pink']
        for i in range(5):
            for j in range(10):
                x1 = j * 50
                y1 = i * 20
                x2 = x1 + 50
                y2 = y1 + 20
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i], width=1, outline='black')
                self.bricks.append(brick)

    def move_left(self, event):
        pos = self.canvas.coords(self.paddle)
        if pos[0] > 0:
            self.canvas.move(self.paddle, -20, 0)

    def move_right(self, event):
        pos = self.canvas.coords(self.paddle)
        if pos[2] < 500:
            self.canvas.move(self.paddle, 20, 0)

    def update_game(self):
        if not self.game_running:
            return

        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_pos = self.canvas.coords(self.ball)

        if ball_pos[0] <= 0 or ball_pos[2] >= 500:
            self.ball_dx = -self.ball_dx

        if ball_pos[1] <= 0:
            self.ball_dy = -self.ball_dy

        paddle_pos = self.canvas.coords(self.paddle)
        if self.hit_paddle(ball_pos, paddle_pos):
            self.ball_dy = -self.ball_dy

        for brick in self.bricks:
            brick_pos = self.canvas.coords(brick)
            if self.hit_brick(ball_pos, brick_pos):
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.ball_dy = -self.ball_dy
                self.counter += 1  # correct: only increment when a brick is really hit
                self.score_label.config(text=f"Score: {self.counter}")  # update label
                break

        if ball_pos[3] >= 400:
            self.game_running = False
            self.canvas.create_text(250, 200, text=f"Game Over! Score: {self.counter}", fill="white", font=('Helvetica', 24))
            return

        if not self.bricks:
            self.game_running = False
            self.canvas.create_text(250, 200, text=f"You Win! Score: {self.counter}", fill="white", font=('Helvetica', 24))
            return

        self.root.after(20, self.update_game)

    def hit_paddle(self, ball, paddle):
        return (ball[2] >= paddle[0] and ball[0] <= paddle[2]) and (ball[3] >= paddle[1] and ball[1] <= paddle[3])

    def hit_brick(self, ball, brick):
        return (ball[2] >= brick[0] and ball[0] <= brick[2]) and (ball[3] >= brick[1] and ball[1] <= brick[3])

if __name__ == "__main__":
    root = tk.Tk()
    game = Breakout(root)
    root.mainloop()
