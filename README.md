# ECS171 music genre classifier
This is a Music Genre Classifier built as a website for ECS 171 - Introduction to Machine Learning.
Users can enter in a song title and the result will be a predicted genre. 

## Installation for Local Machine:
+ **Required Libraries**
+ &nbsp;&nbsp;&nbsp;&nbsp;Keras ('pip3 install keras')
+ &nbsp;&nbsp;&nbsp;&nbsp;Tensorflow ('pip3 install tensorflow')
+ &nbsp;&nbsp;&nbsp;&nbsp;Pandas ('pip3 install pandas')
+ &nbsp;&nbsp;&nbsp;&nbsp;Flask ('pip3 install flask')
+ **Insert Instructions**
+ &nbsp;&nbsp;&nbsp;&nbsp;**Step 1:** download https://os.unil.cloud.switch.ch/fma/fma_metadata.zip
+ &nbsp;&nbsp;&nbsp;&nbsp;**Step 2:** Move all downloaded files to the Data directory
+ &nbsp;&nbsp;&nbsp;&nbsp;**Step 3:** Navigate to the Data_Management folder and run 'python3 Make_DB.py' and 'python3 makePick.py' in terminal
+ &nbsp;&nbsp;&nbsp;&nbsp;**Step 4:** Navigate to the backend folder and run 'python3 backend.py' (IMPORTANT: make sure you run it while you are in the Back_End folder or else it won't work)
+ &nbsp;&nbsp;&nbsp;&nbsp;**Step 5:** Open a new terminal tab and navigate to the Front_End folder and run 'npm install' and then 'npm start'

### Languages
+ **Front end programming languages:** JavaScript (ES6), HTML, CSS
+ **Back end programming languages:** Python (version >= 3)

### Front End
+ **Frameworks:** React
+ **Modules:** node.js, webpack, npm

### Back End
+ **Libraries:** flask
+ **NAME:** findOneSong(name, randomFlag)
+ **SYNOPSIS:** In command prompt, navigate to the backend folder and run 'python3 backend.py'
+ **DESCRIPTION:** The function will take the song tiel as @name and the random pick sonf feature as @randomFlag from url, when front-end or a browser triggers the url.Both @name and @randomFlag are string datatype. @name can be anything inside a string, but @randomFlag should be a string contains 'True' or 'False' only. The function will return a json message, which contaions one object 'error' only when there is no this song title in database or analysis result with objects, 'songName','artist', 'songGenre', 'predictedScore', 'actualGenre, 'songScore', 'modelScore', 'error'.
+ **EXAMPLES:** For example, 'http://localhost:8080/song/enter song/True', @name is 'enter song' and @randomFlag is 'True'
+ **SEE ALSO:** database.query(), ANN_class.ANN(), neuralNet.get_features(), neuralNet.predict()
+ **BUGS:** No known bugs.
+ **anything else:**

### Data Managment
+ [Data Overview](Data_Management/DataOverview.md)
+ **Data file format:**

+ **Anything else:**

### Machine Learning Group
+ **Model used:** insert what model we used
+ **Training:** how to train?
+ **Prediction:** how to predict?
+ **Metrics:**



