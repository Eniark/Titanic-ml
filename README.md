This is a small project I did using ML and some Web

**Results:**
I tuned the hyperparameters of the model. Best models had 82% accuracy.
Then I used some ensemble techniques - I used a VotingClassifier with top 3 best models that gave best result. The VotingClassifier gave 94.5% accuracy on test dataset.
I implemented a Flask app:
![image](https://user-images.githubusercontent.com/62321153/158474050-a59b8feb-f3ce-4ead-96d5-4d1da5c6a2e4.png)
Which would take the results of the model and show them to the user:
![image](https://user-images.githubusercontent.com/62321153/158474097-5447e446-29da-464d-a0da-e7f65f1b1e7c.png)
![image](https://user-images.githubusercontent.com/62321153/158474165-66ae6b56-610e-4ced-b86a-4c74333fc8fe.png)

**To use the app:**
1) Run 'pip install -r requirements.txt';
2) Type 'flask run' in command line in directory 'app/';
3) Go to your localhost;
