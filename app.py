import cv2
import face_recognition
import time
import threading
import winsound  # Only works on Windows. For other OS, use appropriate sound module.

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

# Load known faces and their names here
known_person1_image = face_recognition.load_image_file("JSKV.jpg")
known_person2_image = face_recognition.load_image_file("person2.jpg") 
known_person3_image = face_recognition.load_image_file("person3.jpg")

known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)

known_face_names.append("JSKV")
known_face_names.append("Person 2")
known_face_names.append("Person 3")

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Variables to track unidentified persons
unidentified_start_time = None
warning_shown = False
buzzer_playing = False

def play_buzzer():
    global buzzer_playing
    while buzzer_playing:
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms
        time.sleep(0.5)  # Wait for 0.5 seconds before next beep

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    unidentified = False
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        else:
            unidentified = True

        # Draw a box around the face and label with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Handle unidentified persons
    if unidentified:
        if unidentified_start_time is None:
            unidentified_start_time = time.time()
        elif time.time() - unidentified_start_time >= 5:
            if not warning_shown:
                cv2.putText(frame, "Warning: Unidentified Person!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
                warning_shown = True
                buzzer_playing = True
                threading.Thread(target=play_buzzer).start()
    else:
        unidentified_start_time = None
        warning_shown = False
        buzzer_playing = False

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Break the loop and stop buzzer when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        buzzer_playing = False
        break

# Release the webcam and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
