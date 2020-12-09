from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/softserve")
def soft():
    return render_template("softserve.html")

@app.route("/sorbet")
def sorbet():
    return render_template("sorbet.html")

@app.route("/mochi")
def mochi():
    return render_template("mochi.html")

@app.route("/snowcream")
def snow():
    return render_template("snowcream.html")

@app.route("/dondurma")
def dondurma():
    return render_template("dondurma.html")

@app.route("/faloodeh")
def creme():
    return render_template("faloodeh.html")

@app.route("/frozenyogurt")
def frozen():
    return render_template("frozen.html")

@app.route("/gelato")
def gelato():
    return render_template("gelato.html")

@app.route("/granita")
def granita():
    return render_template("granita.html")

@app.route("/italianice")
def italianice():
    return render_template("italianice.html")

@app.route("/kulfi")
def kulfi():
    return render_template("kulfi.html")

@app.route("/rolled")
def rolled():
    return render_template("rolled.html")

if __name__ == "__main__":
    app.run(debug=True)
