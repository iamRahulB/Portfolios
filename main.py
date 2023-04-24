from flask import Flask, render_template, request
import os
import openai
from image_generator import generate_image
from flask import session

app = Flask(__name__)
app.secret_key = 'ihfheiufhiweuhf7efyw8eyf8ye4y4'

openai.api_key = os.environ["OPENAI_API"]


@app.route('/')
def index():
	return render_template("index.html")


@app.route("/projects", methods=["POST"])
def projects():
     
	name = request.form.get("name").capitalize()
	session['name'] = name

	
	if name.strip() == '':
		return render_template("index.html", name="Please Enter Your Name!")

	else:
		return render_template("projects.html", name=name)


@app.route("/project1", methods=["POST"])
def first():
	return render_template("projects/project1/first.html")


@app.route("/captions", methods=["POST"])
def project1():

	
	prompt = request.form.get("user_text")

	if not prompt:
		return 'Please enter a query'

	name = session.get('name')
# Process the image file and get the caption
	hey = generate_image(prompt,name)

	return render_template("projects/project1/result.html", name=hey)


@app.route("/project2", methods=["POST"])
def project2():
	return "Developement in Progress By Rahul"


@app.route("/project3", methods=["POST"])
def project3():
	return "Developement in Progress By Rahul"
