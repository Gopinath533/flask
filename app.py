from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/add')
def add():
    a = 33
    b = 63
    c = a + b
    return "addition =%d"%c

@app.route('/hello')
def hello():
    return render_template('index.html')


@app.route('/name/<name>')
def name(name):
    return "my name is "+name

def disp():
    return"this is disp page"

app.add_url_rule("/about","disp",disp)
if __name__ =='__main__': 
    app.run(debug = True)




if __name__ == '__main__':
    app.run(debug=True)