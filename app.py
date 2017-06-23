
from flask import Flask, jsonify, request
from bson.objectid import ObjectId
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'prettyprintedconnect'
app.config['MONGO_URI'] = 'mongodb://rest:rest@192.168.177.183:27017/admin'

mongo = PyMongo(app)
@app.route('/api/v1/article', methods=['GET'])
def get_all():
    articlesf=mongo.db.articlesf
    output = []
    for q in articlesf.find():
        output.append({'id':str(q['_id']), 'title':q['title'], 'content':q['content'], 'coment':q['coment'], 'short':q['short']})
    return jsonify(output)

@app.route('/api/v1/article/<string:id>',methods=['GET'])
def get_one(id):
    articlesf=mongo.db.articlesf
    q=articlesf.find_one({'_id':ObjectId(id)})
    if q:
        output={'id':str(q['_id']),  'title':q['title'], 'content':q['content'], 'coment':q['coment'], 'short':q['short']}
    else:
        otput = '[]'
    return jsonify(output)

@app.route('/api/v1/article', methods=['POST'])
def add_one():
    articlesf=mongo.db.articlesf
    title=request.form['title']    
    content=request.form['content']    
    coment=request.form['coment']    
    short=request.form['short']
    articlesf_id=articlesf.insert({'title':title,'content':content,'coment':coment,'short':short})
    new_articlesf=articlesf.find_one({'_id':articlesf_id})
    output={'id':str(new_articlesf['_id']),'title':new_articlesf['title'], 'content': new_articlesf['content'], 'coment': new_articlesf['coment'], 'short': new_articlesf['short']}
    return jsonify(output)

@app.route('/api/v1/article/<string:id>',methods=['PUT'])
def put_one(id):
    articlesf=mongo.db.articlesf
    n_title=request.form['title']    
    n_content=request.form['content']    
    n_coment=request.form['coment']    
    n_short=request.form['short']
    articlesf_id=articlesf.update({'_id':ObjectId(id)},{"$set":{"title":n_title,"content":n_content,"coment":n_coment,"short":n_short}})
    new_articlesf=articlesf.find_one({'_id':articlesf_id})
    output = "OK"    
    return jsonify(output)

@app.route('/api/v1/article/<string:id>',methods=['DELETE'])
def del_one(id):
    articlesf=mongo.db.articlesf
    articlesf.remove({'_id':ObjectId(id)})
    output="OK"
    return jsonify(output)
