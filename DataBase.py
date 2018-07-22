import pymongo
from pymongo import MongoClient
import json
import bson

class DataBaseOfLinks:
	db  = None
	def __init__(self):
		DB_NAME = "shortenerlink"
		DB_HOST = "ds245971.mlab.com"
		DB_PORT = 45971
		DB_USER = "AHmedTaher"
		DB_PASS = "ahmed01118641255adeltaher"
		connection = MongoClient(DB_HOST, DB_PORT)
		DataBaseOfLinks.db = connection[DB_NAME]
		DataBaseOfLinks.db.authenticate(DB_USER, DB_PASS)

	def AddNewLink(self , Data):
		new_one={"slug" :Data["slug"] ,"ios":[{"primary":Data["ios"][0]["primary"] , "fallback":Data["ios"][0]["fallback"]}],"android":[{
		"primary": Data["android"][0]["primary"],
		"fallback": Data["android"][0]["fallback"]}],"web": Data["web"]}
		DataBaseOfLinks.dp = DataBaseOfLinks.db['shortenerlink']
		
		link_id = DataBaseOfLinks.dp.insert_one(new_one).inserted_id
		print (link_id)
		return link_id

	def ShowAllLinks(self):
		DataBaseOfLinks.dp = DataBaseOfLinks.db['shortenerlink']
		Links  = []
		for Link in DataBaseOfLinks.dp.find():
			Old_one={"slug" :Link["slug"] ,"ios":[{"primary":Link["ios"][0]["primary"] , "fallback":Link["ios"][0]["fallback"]}],"android":[{
		"primary": Link["android"][0]["primary"],
		"fallback": Link["android"][0]["fallback"]}],"web": Link["web"]}
			Links.append(Old_one)
		return json.dumps (Links)

	def UpdateLink(self,Link):

		DataBaseOfLinks.dp = DataBaseOfLinks.db['shortenerlink']
		link =DataBaseOfLinks.dp.find_one({"slug": Link["slug"]})
		if link == None:
			return 0
		link["ios"][0]["primary"] = Link["ios"][0]["primary"]
		link["ios"][0]["fallback"] = Link["ios"][0]["fallback"]
		link["android"][0]["primary"]= Link["android"][0]["primary"]
		link["android"][0]["primary"] = Link["android"][0]["primary"]
		link["web"] = Link["web"]
		link["_id"] = bson.ObjectId(link["_id"])
		DataBaseOfLinks.dp.update({"_id": link["_id"] },{"$set": Link})
		link2 = DataBaseOfLinks.dp.find_one({"slug": Link["slug"]})
		return 1
		
