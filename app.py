from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

IMAGE_FOLDER = os.path.join('images')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def home():
    all_images = os.listdir(app.config['UPLOAD_FOLDER'])
    page = request.args.get('page', 1, type=int)
    images_per_page = 15
    total_pages = len(all_images) // images_per_page 
    if len(all_images) % images_per_page != 0:
        total_pages += 1

    start_index = (page - 1) * images_per_page
    end_index = min(start_index + images_per_page, len(all_images))

    images = all_images[start_index:end_index]

    return render_template('index.html', images=images, page=page, total_pages=total_pages, images_per_page=images_per_page)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
