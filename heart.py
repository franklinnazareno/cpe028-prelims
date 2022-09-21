from flask import Flask, jsonify, request 

app = Flask(__name__)

hearts = []

@app.route('/hearts', methods=['POST'])
def addHearts():
    heart = request.get_json()
    heart['hearts_id'] = len(hearts)
    hearts.append(heart)
    return {'id': len(hearts)-1}, 200

@app.route('/hearts', methods=['GET'])
def getHearts():
    return jsonify(hearts), 200

@app.route('/getheart/<int:hearts_id>', methods=['GET'])
def getHeart(hearts_id):
    heart = [ heart for heart in hearts if heart['hearts_id'] == hearts_id ]
    return jsonify(heart), 200

@app.route('/delheart/<int:hearts_id>', methods=['DELETE'])
def delHeart(hearts_id):
    heart = [ heart for heart in hearts if heart['hearts_id'] == hearts_id ]
    hearts.remove(heart[0])
    return jsonify(hearts), 200

if __name__ == '__main__':
    app.run()
