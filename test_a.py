from flask import Flask,render_template

app = Flask(__name__,
template_folder="templates")

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("test_a.html")

app.run(debug=True)