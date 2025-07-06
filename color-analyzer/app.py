import os
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
from collections import Counter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

def get_top_colors(image_path, num_colors=10):
    img = Image.open(image_path)
    img = img.convert('RGB')
    img = img.resize((200, 200))  # Resize to speed up

    pixels = list(img.getdata())
    color_counts = Counter(pixels)
    most_common = color_counts.most_common(num_colors)

    # Convert RGB tuples to HEX codes
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(*rgb) for rgb, count in most_common]
    return hex_colors

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file part"
        file = request.files['image']
        if file.filename == '':
            return "No selected file"
        if file:
            filename = file.filename
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            colors = get_top_colors(save_path)
            return render_template('result.html', colors=colors, filename=filename)
    return render_template('index.html')

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)