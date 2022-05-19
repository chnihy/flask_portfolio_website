from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', page_title='Home')

###---- PROJECTS ----###
@app.route('/projects')
def projects():
	return render_template('projects.html', page_title="Projects")

@app.route('/projects/mpm')
def mpm():
	return render_template('/projects/mpm.html', page_title="Projects - Melodic Pattern Maker")

@app.route('/projects/scales')
def scales():
	return render_template('/projects/scales.html', page_title="Projects - Scales.py")

@app.route('/projects/notereader')
def notereader():
	return render_template('/projects/notereader.html', page_title="Projects - Notereader.py")












@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/about')
def about():
	return render_template('about.html')

