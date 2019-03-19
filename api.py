#importing objects from the flask module  
from flask import Flask, jsonify, request


app = Flask (__name__)

#creating a dictionary in a list
diary = [
         {
           "entry": "going for church", 
           "date": "30/03/2019", 
           "Time": "2:00-8:00pm"
         },
         {
             "entry": "party",
             "date":"07/03/2019",
             "time":"7:00-7:30am"
         },
         {
             "entry": "road work" ,
             "time": "8:30-9:00am",
             "date":"01/02/2019"
        },
         {
             "entry": "visiting",
             "time": "08:00",
             "date": "29/02/2019"
         }
         ]


#a route that creates a url and  returns message in json form
@app.route('/' , methods = ['GET'])
def test():
    return jsonify({'message': 'my diary'})

#a route that returns all entries in the list above created in my dictionary
@app.route('/API/v1/index', methods = ['GET'])
def returnAll():
    return jsonify({'entry': diary})

#a route that returns only one entry in the list
@app.route('/API/v1/index/<string:entry>', methods = ['GET'])
def returnOne(entry):
    dia = [item for item in diary if item['entry']== entry]
    return jsonify({'ent':dia[0]})

   


#a route that uses a post method returning anything added in the dictionary
@app.route('/API/v1/index', methods = ['POST'])
def addOne():
    task = {'entry': request.json['entry']}
    diary.append(task)
    return jsonify({'diary': diary})

#a route that uses a put method to modify the API
@app.route('/API/v1/index/<string:entry>', methods = ['PUT'])
def editOne(entry):
    dia = [activity for activity in diary if activity['entry']== entry]
    dia[0]['entry'] = request.json['entry']
    return jsonify({'ent': dia[0]})




#returning app port 5000 in debug mode
if __name__ == '__main__':
    app.run(debug = True, port = 5000)#(5000)is the initial number for ports.