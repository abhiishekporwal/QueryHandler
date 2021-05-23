from flask import Flask, request, jsonify
import time
from redis import Redis


r = Redis(host='localhost', port=6379)

delay_seconds = 10

# queryMap = {}

app = Flask(__name__)

@app.route("/querytest")
def home():
    start = time.time()
    
    querystring = request.args.get("querystring")
    print(r.hget(querystring, 'time'))
    if(r.hget(querystring, 'time')):
        st_time = r.hget(querystring, 'time').decode("utf-8")
        time_difference = start - float(st_time)
        print("\n" + str(time_difference))
        delay = delay_seconds - time_difference
        output = r.hget(querystring, 'output').decode("utf-8")
        print("\n" + str(delay))

    else:
        r.hset(querystring, 'time', start)
        r.hset(querystring, 'output', querystring)
        output = r.hget(querystring, 'output').decode("utf-8")
        delay = delay_seconds
        
    if delay>0:
        time.sleep(delay) # simuation of processing time  
    else:
        r.hset(querystring, 'time', start)
        r.hset(querystring, 'output', querystring)
        time.sleep(delay_seconds)

    r.hdel(querystring, 'time')
    r.hdel(querystring, 'output')
    return jsonify({'data': output , 'time-taken': delay})
    

if __name__ == "__main__":
    app.run(debug=True)














































# from flask import Flask
# from celery_flask import make_celery
# from time import sleep

# flask_app = Flask(__name__)
# flask_app.config.update(
#     CELERY_BROKER_URL='redis://localhost:6379',
#     RESULT_BACKEND='redis://localhost:6379'
# )
# celery = make_celery(flask_app)

# @celery.task()
# def add_together(a, b):
#     # sleep(5)
#     return a + b


# if __name__ == "__main__":
#     app.run(debug=True)





# from flask import Flask, request, jsonify
# import time

# delay_seconds = 5

# queryMap = {}

# app = Flask(__name__)

# @app.route("/querytest")
# def home():
#     start = time.time()
#     querystring = request.args.get("querystring")
#     print(querystring)
#     if querystring in queryMap:
#         st_time = queryMap[querystring]["time"]
#         time_difference = start - st_time
#         delay = delay_seconds - time_difference
#     else:
#         queryMap[querystring] = {}
#         queryMap[querystring]["time"] = start
#         queryMap[querystring]["output"] = querystring
#         delay = delay_seconds
        
#     if delay>0:
#         time.sleep(delay) # simuation of processing time  
#     else:
#         queryMap[querystring]["time"] = start
#         queryMap[querystring]["output"] = querystring
#         time.sleep(delay_seconds)

#     return jsonify({'data':queryMap[querystring]["output"]})
    
# if __name__ == "__main__":
#     app.run(debug=True)