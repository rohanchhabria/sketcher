import cv2
import os
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from sketch import Sketch
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sketch', methods=['POST'])
def sketch():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image = cv2.imread(f'{UPLOAD_FOLDER}/{filename}')
        sketcher = Sketch()
        sketch = sketcher.draw(image)
        sketch_name = f'{filename.split(".")[0]}_sketch.jpg'
        cv2.imwrite(f'{UPLOAD_FOLDER}/{sketch_name}', sketch)
        return render_template('home.html', orignal_image=filename, sketch_image=sketch_name)
    
if __name__ == '__main__':
    app.run(debug=True)