from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
students = []
next_id = 1

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/students", methods=["GET"])
def list_students():
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    global next_id
    data = request.get_json()
    student = {"id": next_id, "name": data["name"], "course": data["course"]}
    next_id += 1
    students.append(student)
    return jsonify(student), 201

@app.route("/students/<int:sid>", methods=["PUT"])
def update_student(sid):
    data = request.get_json()
    for s in students:
        if s["id"] == sid:
            s["name"] = data.get("name", s["name"])
            s["course"] = data.get("course", s["course"])
            return jsonify(s)
    return jsonify(error="not found"), 404

@app.route("/students/<int:sid>", methods=["DELETE"])
def delete_student(sid):
    global students
    students = [s for s in students if s["id"] != sid]
    return jsonify(message="deleted")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)