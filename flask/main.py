from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/trang2")
def trang2():
    return render_template("trang2.html")

@app.route("/trang3")
def trang3():
    return render_template("trang3.html")

@app.route("/trang4")
def trang4():
    return render_template("trang4.html")
    
if __name__ == "__main__":
    app.run(debug=True)
