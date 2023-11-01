from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
	X = "作者：邓佳钲<br>"
	X += "<a href=/db>课程</a><br>"
	X +="<a href=/khen?nick=khen>个人简介</a><br>"
	X +="<a href=/account>表单传值</a><br>"
	return X

@app.route("/db")
def db():
	return "<a href='https://www.youtube.com/'>海青班资料库管理课程</a>"

@app.route("/khen", methods=["GET", "POST"])
def khen():
	now = str(datetime.now())
	user = request.values.get("nick")
	return render_template("khen.html", datetime=now, name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
	if request.method == "POST":
		user = request.form["user"]
		pwd = request.form["pwd"]
		result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd
		return result

	else:
		return render_template("acc.html")

if __name__ == "__main__":
	app.run()