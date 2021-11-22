from flask import Flask,render_template,request,session

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/second", methods=['GET','POST'])
def second():
    return render_template('insurance.html')

@app.route("/last", methods=['GET','POST'])
def last():
    print("In last")
    return render_template('page3.html')
    
if __name__ == '__main__':
    app.run()

@app.route("/third", methods=['GET','POST'])
def third():
    return render_template('Test.html')


