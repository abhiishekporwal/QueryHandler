# QueryHandler

### Task:

Let's say we are working on a web service (very high traffic) where you have to do some processing based on the get parameter “querystring”. To create a response for one unique querystring (say q1), it takes around one minute to complete (You can simulate it on your code by time. sleep). Many requests will come for a querystring (say q1) by the 1 minute you are creating a response in. The web service should be able to store all requests for querystring == q1 while time. sleep gets over and then returns a common output for all query == q1.


### Approach:

This application is based on Flask server and open-sourced in-memory data structure Redis to store every unique query say 'q1', 'q2' etc. in hash as a key along with their response and use time.sleep() to hold the query response. While holding, many queries will come and they will wait until the sleep time over.

To setup above environment, activate a virtual environment:

`virtualenv virtual_env_name         \n`
`source virtual_env_name/bin/activate`

Get into virtual_env_name

`cd virtual_env_name`

Install all required packages mentioned in requirement.txt as:

`pip3 install -r requirements.txt \n`
`sudo apt install redis-server    `


Clone the repository as:

`git clone https://github.com/abhiishekporwal/QueryHandler.git\n`
`cd QueryHandler`

To run following server, we first have to start redis-server

`redis-server --protected-mode no`

Open a new Terminal, move to virtual environment and set environment variable as:

`export FLASK_APP='app.py'     \n`
`export FLASK_ENV=development  `

To run the flask server run command:
`flask run`

Copy the localhost url and paste it on multiple tabs in browser(Mozilla) or POSTMAN tool where you can select request method as GET and run all of them in parallel  :
http://127.0.0.1:5000/querytest?querystring='input_your_desired_query'

Notice each and every process will end at same time and have same output if it runs in wait time. It will take x secondsd(e.g. 10 seconds) for any unique query to process and other similar queries will stand still within wait time.















