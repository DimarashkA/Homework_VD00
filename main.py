from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    context = {
        "caption": "Фильмы про мушкетеров"
    }
    return render_template("index_hw_VD02.html", **context)

@app.route("/shablon/")
def films2():
    context = {
        "caption": "Мушкетеры"
    }
    return render_template("index_hw_VD02.html", **context)

@app.route("/person/")
def person():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()