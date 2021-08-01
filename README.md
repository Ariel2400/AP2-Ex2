# AP2-Ex2

### Video explanation about our project: https://screenrec.com/share/NVhC7tX4ge

Project by: Yair koskas, Tsela Gam Zo Letova, Ariel Grosh , Itay Gradenwits .
Special requirements for this project: 
        We used python and some of its libraries to built this project. in order to install them download the requirements.txt file
        we put at the repesitory and run the next command from the shell at the present of the file:
        pip install -r requirements.txt
        
Explanation about the directories hierarchy of the project:
  - In AP1_code you'll see the files that our lecturer Eli gave us. this directory is actually the server of runs the anomalies detection algorithms.
  - In algorithm directory you'll see the client side files who parse the csv files and uses the server functionallity to detect anomallies.
  - In config directory you'll see the configuration files for this project.
  - In Templates you'll see css and html files for the web app.
  - In tests you'll see some tests we used to check our code.
  - In app.py you'll see the main program which implements the get and post requests that our app supports and also run the app.
    
how to run the project:
   1. first we need to run the anomaly detection server. Run the next command from the shell (please run it from AP2-Ex2 directory):
            ./AP1_code 8081

   2. Next we need to run the app. Run the next command from the shell (please run it from AP2-Ex2 directory):
            ./app.py

   3. now the app is running:
          1) for user story 1 go to : "http://127.0.0.1:8080/".
              That's would lead you to our app. The app support the next functionality:
                - choose an algorithm type  for the anomalie detection.
                - choose a csv file who doesn't contains anomalies.
                - choose a csv file whi might contains anomalies.
                - press submit and you'll see information about the files and the anomalies at it.
           2) for user story 2 send an http post request to: "http://127.0.0.1:8080/" and add json object as argument.
                  please decode the json in this format: {'algo_type': <algorithm Type>, 'reg_csv': <path1> , 'irreg_csv': <path2>}
                   - <algorithm type> is a string who represnt the algorithm type we'll run use to detect the anomalies,
                     choose between hybrid and regression.
                   - <path1> is a path to a correct csv file without anomalies.
                   - <path2> is a path ao a csv file that might contains anomalies.
                  the post request will return a json object represnt the anomalies at the file.
                                    
                                    
                                       
                                       
