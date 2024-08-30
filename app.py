from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

def calculate_program(dob):
    today = datetime.today()
    birthdate = datetime.strptime(dob, '%Y-%m-%d')
    age = (today - birthdate).days // 365

    if 3 <= age < 5:
        return "Your child is eligible for Preschool."
    elif 5 <= age < 6:
        return "Your child is eligible for Kindergarten."
    else:
        return "Please check the LAUSD website for further information."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-eligibility', methods=['GET'])
def check_eligibility():
    dob = request.args.get('dob')
    message = calculate_program(dob)
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)