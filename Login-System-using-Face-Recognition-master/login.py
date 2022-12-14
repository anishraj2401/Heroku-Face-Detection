from base64 import b64decode
import cv2 as cv
import time
import os
import pickle

def login_check(email, image):
    face_match = 0
    header, encoded = image.split(",", 1)
    file_new = str(time.time_ns())
    file_exist = str(time.time_ns())

    with open(file_new + ".png", "wb") as f:
        cv.write(b64decode(encoded))

    data = pickle.loads(open("data.pickle", "rb").read())
    with open(file_exist + ".png", "wb") as cv:
        cv.write(b64decode(data[email]))
    
    try:
        try:
            got_image = cv.load_image_file(file_new + ".png")
            existing_image = cv.load_image_file(file_exist + ".png")
        except Exception as e:
            print(e.__cause__)
            return "Data does not exist!"
        got_image_facialfeatures = cv.face_encodings(got_image)[0]
        existing_image_facialfeatures = cv.face_encodings(existing_image)[0]
        results = cv.compare_faces([existing_image_facialfeatures], got_image_facialfeatures)
        if(results[0]):
            return "Successfully Logged in!"
        else:
            return "Failed to Log in!"
    except Exception as e:
        print(e.__cause__)
        return "Image not clear! Please try again!"