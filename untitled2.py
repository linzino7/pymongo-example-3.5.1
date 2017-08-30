# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 21:04:36 2017

@author: linzino
"""

from pymongo import MongoClient
import urllib.parse
import datetime

username = urllib.parse.quote_plus('user')
password = urllib.parse.quote_plus('passwd')


client = MongoClient('mongodb://%s:%s@127.0.0.1/ir_message_db?authMechanism=SCRAM-SHA-1' % (username, password))


db = client['ir_message_db'] 


#-------列出全部----------
collect = db['abc']
for post in collect.find():
    print(post)

#-------insert----------
#post = {"author": "Mike",
#        "text": "My first blog post!",
#        "tags": ["mongodb", "python", "pymongo"],
#        "date": datetime.datetime.utcnow()}
#posts = db.abc #選擇插入的collect 如同table
#post_id = posts.insert_one(post).inserted_id


#工具 MongoDB Compass