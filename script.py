from flask import Flask,render_template,request
app = Flask(__name__)  
 
@app.route('/<name>')  
def message(name):  
      return render_template('index1.html',name=name)  
@app.route('/add/<int:num>')
def add(num):
    return render_template('house.html',num=num)
@app.route('/customer')  
def customer():  
   return render_template('customer.html')  
  
@app.route('/success',methods = ['POST'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("result.html",result = result)  
       
if __name__ == '__main__':  
   app.run(debug = True)