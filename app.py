from flask import Flask, render_template, url_for, request
import requests
import json
from flask import jsonify

from DataBase import DataBaseOfLinks


app = Flask(__name__)


@app.route ("/ShortAlink",methods=["POST"])
def Add():
	DataBase1 = DataBaseOfLinks()
	if request.method == "POST":
		Data = request.get_json()
		if Data == {}:
			return json.dumps({ }), 500
		DataBase1.AddNewLink(Data)
		return	 json.dumps({"status": "successful","slug": Data["slug"],"message": "created successfully"}),201
	
@app.route ("/ShowAll",methods=["Get"])
def ShowAll():
	DataBase1 = DataBaseOfLinks()
	return	 (DataBase1.ShowAllLinks())

@app.route ("/UpDate",methods=["POST"])
def Update ():
	DataBase1 = DataBaseOfLinks()
	Data = request.get_json()
	if Data == {}:
		return json.dumps({ }), 500
	if DataBase1.UpdateLink(Data)==1 :

		return	 json.dumps({"status": "successful","slug": Data["slug"],"message": "created successfully"}),201
	else :
		ErrorJson ={"status" :"failed","message": "not found"}

		return json.dumps(ErrorJson),404



@app.errorhandler(404)
def LinkNotFound(e):
	ErrorJson ={"status" :"failed","message": "not found"}

	return json.dumps(ErrorJson),404

@app.errorhandler(405)
def LinkNotFound(e):
	ErrorJson ={"status" :"failed","message": "You using Post and Should Use Get"}
	return json.dumps(ErrorJson),405

@app.errorhandler(400)
def JsonNotFound(e):
	ErrorJson ={"status": "failed","message": "Bad Request"}

	return json.dumps(ErrorJson),400

@app.errorhandler(500)
def LinkNot(e):
	ErrorJson ={}	
	return json.dumps(ErrorJson),500


if __name__ == "__main__":
    app.run(debug=True)
