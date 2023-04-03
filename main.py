# Contains the logic for the flask web app to serve model's predictions.  

from flask import Flask, render_template, Response
from camera import VideoCamera


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # Specifies the name of the HTML template file. 

# Activates video camera feed and gets the feed one frame at a time. 
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Outputs the prediction image to the web interface. VideoCamera class sends images to the model which outputs the predictions to the main.py scripts. 
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
