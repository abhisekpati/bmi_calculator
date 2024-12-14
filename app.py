from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    # Calculate BMI
    return weight / (height ** 2)

def bmi_category(bmi):
    # Determine the category based on BMI value
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    
    return render_template('result.html', bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4040)


