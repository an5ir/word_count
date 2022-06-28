Word Count
==============================

Flask application revise a URL of a website and return the number of word occurrences of the text held within the html page.

# Installation 

## developer installation
* Create a base environment using conda `conda create --name word_count python=3.9` or any other preferred method
* Activate your new environment (for linux `source activate word_count` and  for windows `activate word_count`) then Install all required packages `pip install -r requirements.txt`
* This should hopefully allow to debug any issue with greater ease.

## docker installation
Move to the word_count folder and run `docker build -t word_count:latest .` to build word_count docker container.

# How to run the flask application

There are 3 methods of running application:
1) Activate `word_count` environment, change to `word_count` directory. Execute the runner script `python runner.py`
2) Activate `word_count` environment, change to `word_count` directory. Execute  `flask run`
3) run pre-build docker container by executing  `docker run --name word_count -d -p 5000:5000 --rm word_count:latest`

# How to use the application

Once the flask server is running locally go to the following url: http://localhost:5000/

You should see the below form:
![home_screen](references/images/home_screen.png?raw=true "home_screen")

Enter a URL into the textbox and click submit:

![home_screen](references/images/return_values.png?raw=true "home_screen")

You can check the health of the flask server by sending a get request to `http://localhost:5000/health`. a `200` status 
code will suggest the flask server is healthy.

# How to run pytest test

First add `word_count` folder to your python path:
* for windows go to `My Computer > Properties > Advanced System Settings > Environment Variables >` and add `PYTHONPATH=:/path/to/word_count/`
* else `export PYTHONPATH="${PYTHONPATH}c:/path/to/word_count"`
* cd `test\` folder and run `pytest`

         
--------

