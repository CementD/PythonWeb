from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/multiply/<int:n>')
def multiply(n):
    m = []
    for i in range(1, 10):
        m.append(f'{n} * {i} = {i * n}')
    return m

@app.route('/factorial')
def factorial():
    a = int(request.args.get('a'))
    m = 1
    for i in range (1, a+1):
        m *= i
    return str(m)

@app.route('/even_odd/<int:n>')
def even_odd(n):
    if n % 2 == 0:
        return f'{n} is Even'
    else:
        return f'{n} is Odd'

@app.route('/calc')
def calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    op = request.args.get('op')
    result = ''
    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        if b != 0:
            result = a / b
        else:
            return "You can't divide by 0"
    else:
        return "False operation"

    return f'Result of {a} {op} {b} = {result}'

@app.route('/primes')
def primes():
    limit = int(request.args.get('limit'))
    m = []
    for i in range(2, limit):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            m.append(i)

    return str(m)



if __name__ == '__main__':
    app.run()
