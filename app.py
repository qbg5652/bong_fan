import certifi
ca = certifi.where()
from pymongo import MongoClient
client = MongoClient("mongodb+srv://bongdroid:qhdrbs88!@cluster0.hecgbmx.mongodb.net/Cluster0?retryWrites=true&w=majority", tlsCAFile = ca)
db = client.pracdb

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {'name': name_receive, 'comment': comment_receive}
    db.fancomment.insert_one(doc)

    return jsonify({'msg':'팬명록 등록 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    comment_list = list(db.fancomment.find({}, {'_id': False}))
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)