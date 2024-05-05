# Flask server that links to a DAO
# Author: Stefania Verduga

from flask import Flask, request, abort, jsonify
from perfumesdao import perfumeDAO as dao

app = Flask(__name__, static_url_path="", static_folder="staticpages")

# Function root to home page
@app.route("/")
def home():
    return "Welcome to the perfumes' world!"

# Gets all data from the database
@app.route('/home')
def getAll():
    return jsonify(dao.getAll())

# Get data specified by id
@app.route("/home/<id>")
def findByID(id):
    return jsonify(dao.findById(id))

# Add new record to the database
@app.route('/home', methods=['POST'])
def createPerfume():
    if not request.json:
        abort(400)
    data = {
        "Name": request.json["Name"],
        "Brand": request.json["Brand"],
        "Size_ml": request.json["Size_ml"],
        "Price_eur": request.json["Price_eur"],
        "Gender": request.json["Gender"]
    }
    return jsonify(dao.create(data))

# Update database from the webpage
@app.route('/home/<id>', methods=['PUT'])
def updatePerfume(id):
    foundPerfume = dao.findById(id)
    if len(foundPerfume) == 0:
        return jsonify({}), 404
    currentPerfume = foundPerfume
    if "Name" in request.json:
        currentPerfume["Name"] = request.json["Name"]
    if "Brand" in request.json:
        currentPerfume["Brand"] = request.json["Brand"]
    if "Size_ml" in request.json:
        currentPerfume["Size_ml"] = request.json["Size_ml"]
    if "Price_eur" in request.json:
        currentPerfume["Price_eur"] = request.json["Price_eur"]
    if "Gender" in request.json:
        currentPerfume["Gender"] = request.json["Gender"]
    dao.update(currentPerfume)
    return jsonify(currentPerfume)

# Delete by id
@app.route('/home/<id>', methods=['DELETE'])
def deletePerfume(id):
    foundPerfume = dao.findById(id)
    if len(foundPerfume) == 0:
        return jsonify({}), 404
    dao.delete(id)
    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True, port=8080)
