from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import cv2
from PIL import Image
import numpy as np
from processor import BackgroundRemover
from gpu_manager import check_gpu

app = Flask(__name__)
CORS(app)

# Initialize background remover
remover = BackgroundRemover()

@app.route('/process', methods=['POST'])
def process_image():
    try:
        data = request.json
        image_path = data.get('image_path')
        mode = data.get('mode', 'standard')
        
        result = remover.remove_background(image_path, mode)
        
        return jsonify({
            'success': True,
            'result_path': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/gpu-info', methods=['GET'])
def get_gpu_info():
    return jsonify(check_gpu())

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
