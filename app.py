import sys
import io
import base64
import numpy as np
import cv2
from flask import Flask, request, jsonify
from deepface import DeepFace

# Standard output stream-u UTF-8 kodlaşdırması ilə dəyişdirin
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)

def base64_to_image(base64_string):
    """Base64 string-i OpenCV image formatına çevirir"""
    image_bytes = base64.b64decode(base64_string)
    np_arr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return image

@app.route('/verify', methods=['POST'])
def verify_faces():
    try:
        # Base64 string-i qəbul edirik
        data = request.json
        image1_base64 = data['image1']
        image2_base64 = data['image2']

        # Base64 string-ləri OpenCV şəkil formatına çevirmək
        image1 = base64_to_image(image1_base64)
        image2 = base64_to_image(image2_base64)

        # Üzlərin oxşarlığını müqayisə edirik
        result = DeepFace.verify(image1, image2, enforce_detection=False, detector_backend="retinaface")

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
