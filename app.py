from flask import Flask,render_template,request
import tweetcraw as tw #import file tweetcraw.py
app=Flask(__name__)


@app.route("/")

#Main page
@app.route("/home")
def home():
    return render_template("index.html")

#Picture wordcloud
@app.route("/result", methods=['POST', "GET"])
def result():
    output = request.form.to_dict()
    word = output["word"]
    print(word)
    tw.twetty(word) ##send data to create word cloud
    return render_template("image.html",word=word)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=15990) #run server port=15990
    home();
    result();
