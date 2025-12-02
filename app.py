from flask import Flask, render_template, redirect, request, url_for
app=Flask("__name__")
@app.route("/",methods=["GET","POST"])
def home():
	if request.method=="POST":
		print("registration successfull")
		print("form submitted")
	return render_template("register.html")
if __name__=="__main__":
	app.run(debug=True)
