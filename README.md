This is a small project I did using ML and some Web

**Results:**
I tuned the hyperparameters of the model. Best models had 82% accuracy.
Then I used some ensemble techniques - I used a VotingClassifier with top 3 best models that gave best result. The VotingClassifier gave 94.5% accuracy on test dataset.
I implemented a Flask app:
![image](https://user-images.githubusercontent.com/62321153/158413080-a2ab141b-8b18-4444-b5cf-b21fb237ca89.png)
Which would take the results of the model and show them to the user:
1) ![image](https://user-images.githubusercontent.com/62321153/158414041-5eb3e332-e4a5-4385-a2fb-4d806006ac46.png)
2) ![image](https://user-images.githubusercontent.com/62321153/158414156-424fd1e5-9209-4827-ad79-1280f3478da2.png)

**To use the app:**
1) Check requirements.txt;
2) Write 'flask run' in command line in the flask app directory;
3) Go to your localhost;

