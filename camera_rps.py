import random
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_computer_choice():
    rps_list = ["Rock", "Paper", "Scissors"]
    return random.choice(rps_list)

def get_prediction():
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        rps_list = ["Rock", "Scissors", "Paper", "Nothing"]
        # print([rps_list[index] for index, item in enumerate(prediction[0]) if item==max(prediction[0])])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return [rps_list[index] for index, item in enumerate(prediction[0]) if item==max(prediction[0])][0]


def get_user_choice():
    user_choice = input("Rock, paper, scissors?")
    return user_choice

def get_winner(computer_choice, user_choice):
    if (computer_choice == user_choice):
        print("It is a tie!") 
    elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
        print("You won!")
    else:
        print("You lost!")

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)
