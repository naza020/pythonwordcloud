from flask import Flask,render_template,request
import tweetcraw as tw
app=Flask(__name__)


@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html")

@app.route("/result", methods=['POST', "GET"])
def result():
    output = request.form.to_dict()
    word = output["word"]
    print(word)
    tw.twetty(word)
    return render_template("image.html",word=word)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=15990)
    home();
    result();
