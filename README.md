# Computer Vision RPS

# Computer Vision
The computer vision system for the rock paper scissors game was made using [Teachable Machine](https://teachablemachine.withgoogle.com/), by training an image project model on images of myself holding up my hand in a rock, paper, scissors, or nothing (including both images of myself holding up no hand, and images of myself holding up a hand but not playing rock, paper or scissors.)

The model is saved in the repository as keras_model.h5. This model is used to detect if the user intends to play rock, paper or scissors in a game of rock-paper-scissors against a computer opponent. 

# Environment and dependencies
The dependencies for this project can be found in [requirements.txt](requirements.txt). To install these dependencies:

1. Install [Conda](https://docs.conda.io/en/latest/miniconda.html) using the Miniconda installer.
1. Create a new conda environment using this command in bash terminal:
``` conda create -n computer-vision ```
1. Activate the environment using this command: 
``` conda activate computer-vision ```
1. Check that your conda environment has successfully activated. If it has, the name of the environment should appear in brackets in the terminal as shown below:
![](images\conda.PNG)
1. Install pip using this command:
``` conda install pip ```
1. Install the dependencies from requirements.txt using the following command: 
``` pip install requirements.txt ```

The dependencies should now be installed to your conda environment. This program can be run by navigating to ``` .../computer-vision-rock-paper-scissors ``` and running the following command:
``` python manual_rps.py ```

# Manual Rock-Paper-Scissors
[manual_rps.py](manual_rps.py) contains the basic code required to play rock paper scissors against a randomised computer opponent by manually inputting "Rock", "Paper" or "Scissors". 

``` get_computer_choice ``` uses the [random](https://docs.python.org/3/library/random.html) module to randomly select "Rock", "Paper" or "Scissors" from a list of options. 

``` get_user_choice ``` prompts the user for an input and returns their input.

``` get_winner ``` compares the user's choice against the computer's, and determines who the winner is by comparing the selections, printing a relevant message. 

``` play ``` prompts a game to play, getting the user's choice and computer's choice before determining the winner using the ```get_winner``` function. 