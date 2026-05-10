from flask import Flask, jsonify, request

# 1. Create the Flask app
app = Flask(__name__)

# 2. This is our fake "database" (a simple Python list)
students = [
    {'id': 1, 'name': 'Memoona', 'grade': 'A'},
    {'id': 2, 'name': 'Sara', 'grade': 'B'}
]
next_id = 3

# 3. The Health Check (Required for Lab 11 Deployment)
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "Flask is running"}), 200

# 4. READ (GET): Give the user the list of all students
@app.route('/api/students', methods=['GET'])
def get_students():
    # jsonify converts our Python list into JSON text the browser can read
    return jsonify(students), 200

# 5. CREATE (POST): Let the user add a new student
@app.route('/api/students', methods=['POST'])
def add_student():
    global next_id
    # Get the data the user sent us
    data = request.get_json()
    
    # Check if they forgot the name or grade
    if not data or 'name' not in data or 'grade' not in data:
        return jsonify({'error': 'name and grade are required'}), 400
        
    # Create a new student dictionary and add it to our list
    new_student = {'id': next_id, 'name': data['name'], 'grade': data['grade']}
    students.append(new_student)
    next_id += 1
    
    return jsonify(new_student), 201

# 6. Start the server
if __name__ == '__main__':
    # debug=True means it automatically restarts if you change the code
    # port=5000 is the door it listens on
    app.run(debug=True, port=5000)