from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <h1>Python Operations with Flask Routing and Views</h1>
    ''')

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:count>')
def count(count):
    result = ''
    for i in range(1, count + 1):
        result += f"{i}\n"
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Supported operations: +, -, *, div, %"
    return str(result)

if __name__ == '__main__':
    app.run(debug=True, port=5555)