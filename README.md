# Real-time-ML-powered-restricted-area-survilliance-
This project implements a real-time face recognition system using Python, OpenCV, and the face_recognition library. It detects and identifies known individuals from a webcam feed and raises an audible security alert for unidentified persons.

Features
Face Recognition: Identifies known faces by comparing live video feed with preloaded face encodings.
Unidentified Person Detection: Triggers a warning message and buzzer sound when an unknown person is detected for more than 5 seconds.
Live Feedback: Displays a live video feed with bounding boxes and labels for identified faces.
Customizable: Easily update the list of known individuals by adding images and names.
Requirements
Python 3.11
Libraries: cv2, face_recognition, winsound (Windows-only for buzzer sound)
Webcam for live video feed
Preloaded face images for known individuals
How It Works
Load face images and names into the system.
Start the webcam feed.
The system identifies faces and labels known individuals in real-time.
If an unknown person is detected for more than 5 seconds, a warning message is displayed, and a buzzer sound is played.
Use Cases
Security monitoring
Attendance systems
Personalized user experiences
