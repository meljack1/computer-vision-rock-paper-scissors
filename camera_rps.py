import random
import time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class Rock_Paper_Scissors_Game():
    def __init__(self):
        self.rps_list = ["Rock", "Scissors", "Paper", "Nothing"]
        self.computer_wins = 0
        self.user_wins = 0
        self.rounds_played = 0
    def get_computer_choice(self):
        return random.choice(self.rps_list[:-1])
    def get_prediction(self):
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
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        prediction_final = [self.rps_list[index] for index, item in enumerate(prediction[0]) if item==max(prediction[0])][0]
        return prediction_final
    def get_winner(self, computer_choice, user_choice):
        if (computer_choice == user_choice):
            print(f"It's a tie this round! (Your choice: {user_choice} / Computer's choice: {computer_choice})")
            return "Tie"
        elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
            print(f"You win this round! (Your choice: {user_choice} / Computer's choice: {computer_choice})")
            return "User"
        elif (user_choice == "Rock" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Scissors") or (user_choice == "Scissors" and computer_choice == "Rock"):
            print(f"You lose this round (Your choice: {user_choice} / Computer's choice: {computer_choice})")
            return "Computer"
        else:
            return "Error"
    def play(self):
        while self.computer_wins < 3 and self.user_wins < 3 and self.rounds_played < 5:
            self.rounds_played += 1
            computer_choice = self.get_computer_choice()
            user_choice = self.get_prediction()
            while user_choice == "Nothing":
                print("No rock, paper or scissors detected")
                user_choice = self.get_prediction()
            winner = self.get_winner(computer_choice, user_choice)
            if winner == "User":
                self.user_wins += 1
            elif winner == "Computer":
                self.computer_wins += 1
        if self.user_wins == 3:
            print("You have won 3 games! Congratulations.")
        elif self.computer_wins == 3:
            print("You lose - the computer has won 3 games.")
        else: 
            print("Game over - too many rounds.")

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

rps = Rock_Paper_Scissors_Game()

rps.play()