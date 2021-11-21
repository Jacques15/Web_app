from flask import Flask,render_template,request,session

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/second", methods=['GET','POST'])
def second():
    if request.method == "POST":
        if request.form.get("button_a"):
            print("Find Pressed!!")
            session["a"] = 2
            if "a" in session:
                a = session["a"]
            return render_template('insurance.html', a = a)

        if request.form.get("Yes1"):
            print("Yes Pressed")
        if request.form.get("No1"):
            print("No Pressed")
        if request.form.get("Man"):
            print("Man Pressed")
    
    if "a" in session:
        a = session["a"]
        return render_template('insurance.html',a = a)
    else:
        return render_template('insurance.html')
    
if __name__ == '__main__':
    app.run()
