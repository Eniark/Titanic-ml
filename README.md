This is a small project I did using ML and some Web

**Results:**
I tuned the hyperparameters of the model. Best models had 82% accuracy.
Then I used some ensemble techniques - I used a VotingClassifier with top 3 best models that gave best result. The VotingClassifier gave 94.5% accuracy on test dataset.
I implemented a Flask app:
![image](https://user-images.githubusercontent.com/62321153/158413080-a2ab141b-8b18-4444-b5cf-b21fb237ca89.png)
Which would take the results of the model and show them to the user:
1) ![image](https://user-images.githubusercontent.com/62321153/158413226-4bc3d64e-98c8-48ea-9916-2d976a4d2aeb.png)
2) ![image](https://user-images.githubusercontent.com/62321153/158413315-de51a95b-2e6d-4141-aabf-41d68acdb466.png)

**To use the app:**
1) Check requirements.txt;
2) Write 'flask run' in command line in the flask app directory;
3) Go to your localhost;

