from flask import Flask,render_template,request,session,jsonify

app = Flask(__name__)
app.secret_key = "hellos"

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/second", methods=['GET','POST'])
def second():
    text = request.form.get("text")
    print(text)
    session["text"] = text
    return render_template('insurance.html')

@app.route("/last", methods=['GET','POST'])
def last():
    print("In Last")
    if (session["text"] == "Check1"):
        plan = "Comprehensive"
        price = "$30.50 per fortnight"
    if (session["text"] == "Check2"):
        plan = "3rd Party Fire & Theft"
        price = "$22.50 per fortnight"
    if (session["text"] == "Check3"):
        plan = "3rd Party"
        price = "$10.00 per fortnight"
    
    return render_template('page3.html',plan = plan, price = price)
    
if __name__ == '__main__':
    app.run()

@app.route("/third", methods=['GET','POST'])
def third():
    text = request.form.get("text")
    print(text)
    session["text"] = text
    return render_template('Test.html')

@app.route('/process', methods = ['POST','GET'])
def process():
    name = request.form.get("name")
    surname = request.form.get("surname")

    print(name)
    print(surname)

    return jsonify({'name':"Jacques", 'surname':"Theron"})



