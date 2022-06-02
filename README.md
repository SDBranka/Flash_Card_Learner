# Flash Card Learner

##### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)

---


<p float="center">
    <img src="https://github.com/SDBranka/PW_Generator_with_Recall/blob/main/Pw_Generator_Screenshot0.png" width=30% alt="app pic two" />
    <img src="https://github.com/SDBranka/PW_Generator_with_Recall/blob/main/Pw_Generator_Screenshot1.png" width=31% alt="app pic two" />
    <img src="https://github.com/SDBranka/PW_Generator_with_Recall/blob/main/Pw_Generator_Screenshot2.png" width=30% alt="app pic two" />
</p>

## Description

This app allows a user to learn their preferred topic in flash card fashion. The app will present the prompt and after 3 seconds display the answer. Known cards are removed from the challenges presented in the future. Elements that still need to be learned will be stored to a file (still_to_learn.csv) within the data folder.

##### Controls

- The user should enter a valid .csv file name and click the "OK" button
    - do not include ".csv" with your entry
- If the user knew the correct answer they should click the green check mark button
- If the user does not know the correct answer they should click the red x button

##### Technologies

- Python
- Tkinter
    - messagebox
    - simpledialog
- Pandas
- Visual Studio

---

## How To Use

Download or clone this repository to your desktop. Click on the file Flash_Card_Learner.exe or run main.py in an appropriate Python environment.

- A user may contribute their own files to learn from
    - they must be a .csv file and properly formatted
        - view the examples provided
    - they must be stored in the data folder 

---

## References

##### Continuing Work on

- https://github.com/SDBranka/_100DOP_Exercises

\
[Back To The Top](#flash-card-learner)