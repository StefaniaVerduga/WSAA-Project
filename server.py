# Flask server that links to a DAO
# Author: Stefania Verduga

from flask import Flask, request, abort, jsonify, send_file, redirect
from perfumesdao import perfumeDAO as dao

app = Flask(__name__, static_url_path="", static_folder="staticpages")

# Function root to home page
@app.route("/")
def home():
    return send_file("perfumes.html")

# Gets all data from the database
# curl http://127.0.0.1:5000/perfumes
@app.route("/perfumes")
def getAll():
    return jsonify(dao.getAll())

# Get data specified by id
# curl http://127.0.0.1:5000/perfumes/1
@app.route("/perfumes/<id>")
def findByID(id):
    return jsonify(dao.findById(id))

# Add new record to the database
# curl -X POST -H "Content-Type: application/json" -d "{\"Brand\":\"CK\", \"Gender\":\"F\", \"Name\":\"Eternity\", \"Price_eur\":36, \"Size_ml\":100}" http://127.0.0.1:5000/perfumes
@app.route("/perfumes", methods=['POST'])
def createPerfume():
    if not request.json:
        return jsonify({"error": "Bad Request"}), 400
    data = {
        "Name": request.json.get("Name"),
        "Brand": request.json.get("Brand"),
        "Size_ml": request.json.get("Size_ml"),
        "Price_eur": request.json.get("Price_eur"),
        "Gender": request.json.get("Gender")
    }
    perfume_id = dao.create(data)
    if perfume_id:
        return jsonify({"id": perfume_id}), 201
    else:
        return jsonify({"error": "Failed to create perfume"}), 500

# Update database from the webpage
# curl -X PUT -H "Content-Type: application/json" -d "{\"Brand\":\"CK\", \"Gender\":\"F\", \"Name\":\"Eternity\", \"Price_eur\":36, \"Size_ml\":85}" http://127.0.0.1:5000/perfumes/11
@app.route("/perfumes/<int:id>", methods=['PUT'])
def updatePerfume(id):
    foundPerfume = dao.findById(id)
    if foundPerfume is None:
        return jsonify({"error": "Perfume not found"}), 404
    
    foundPerfume["Name"] = request.json.get("Name", foundPerfume["Name"])
    foundPerfume["Brand"] = request.json.get("Brand", foundPerfume["Brand"])
    foundPerfume["Size_ml"] = request.json.get("Size_ml", foundPerfume["Size_ml"])
    foundPerfume["Price_eur"] = request.json.get("Price_eur", foundPerfume["Price_eur"])
    foundPerfume["Gender"] = request.json.get("Gender", foundPerfume["Gender"])

    dao.update(foundPerfume)
    return jsonify(foundPerfume), 200

# Delete by id
# curl -X DELETE  http://127.0.0.1:5000/perfumes/11
@app.route("/perfumes/<int:id>", methods=['DELETE'])
def deletePerfume(id):
    foundPerfume = dao.findById(id)
    if not foundPerfume:
        return jsonify({"error": "Perfume not found"}), 404
    dao.delete(id)
    return jsonify({"success": True}), 200

if __name__ == "__main__":
    app.run(debug=True)

