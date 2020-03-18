from flask import Flask, render_template, Response
import cv2


app = Flask(__name__)

def genFrames(id_cam):
    cap = cv2.VideoCapture(int(id_cam))
    cap.set(3,320)
    cap.set(4,240)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/video_feed/<string:id>/', methods=['GET'])
def video_feed(id):
    return Response(genFrames(id), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)