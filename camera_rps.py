import random
import time
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
    rps_list = ["Rock", "Scissors", "Paper", "Nothing"]
    start_time = time.time()
    while start_time + 3 > time.time(): 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        # print([rps_list[index] for index, item in enumerate(prediction[0]) if item==max(prediction[0])])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    ## cap.release()
    # Destroy all the windows
    ## cv2.destroyAllWindows()
    prediction_final = [rps_list[index] for index, item in enumerate(prediction[0]) if item==max(prediction[0])][0]
    return prediction_final

def get_winner(computer_choice, user_choice):
    if (computer_choice == user_choice):
        print("It's a tie this round!")
    elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
        print("You win this round!")
        return "User"
    elif (user_choice == "Rock" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Scissors") or (user_choice == "Scissors" and computer_choice == "Rock"):
        print("You lose this round")
        return "Computer"
    else:
        return "Error"

def play():
    computer_wins = 0
    user_wins = 0
    rounds_played = 0
    while computer_wins < 3 and user_wins < 3 and rounds_played < 5:
        computer_choice = get_computer_choice()
        user_choice = "Nothing"
        while user_choice == "Nothing":
            user_choice = get_prediction()
        winner = get_winner(computer_choice, user_choice)
        if winner == "User":
            user_wins += 1
        elif winner == "Computer":
            computer_wins += 1
        rounds_played += 1
    if user_wins == 3:
        print("You have won 3 games!")
    elif computer_wins == 3:
        print("You have lost...")
    else: 
        print("Game over.")

play()