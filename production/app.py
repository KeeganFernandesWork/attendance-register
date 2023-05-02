# Import necessary libraries
from flask import Flask, request, render_template
import cv2
import numpy as np
import yolo8

# Create a Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for processing the uploaded image
@app.route('/process_image', methods=['POST'])
def process_image():
    # Load the YOLOv8 model
    model = yolo8.load_model()

    # Get the uploaded image
    image = request.files['image'].read()
    image = np.fromstring(image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Process the image using the YOLOv8 model
    results = yolo8.detect_objects(model, image)

    # Return the results to the HTML template
    return render_template('results.html', results=results)

# Define the route for processing the video feed
@app.route('/process_video', methods=['POST'])
def process_video():
    # Load the YOLOv8 model
    model = yolo8.load_model()

    # Capture the video feed
    cap = cv2.VideoCapture(0)

    # Process each frame in the video feed
    while True:
        ret, frame = cap.read()

        # Process the frame using the YOLOv8 model
        results = yolo8.detect_objects(model, frame)

        # Display the results on the video feed
        for result in results:
            cv2.rectangle(frame, result[0], result[1], (0, 255, 0), 2)

        # Display the processed video feed
        cv2.imshow('Video Feed', frame)

        # Exit the loop when the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the video window
    cap.release()
    cv2.destroyAllWindows()

    # Return to the home page
    return render_template('index.html')

# Run the Flask

