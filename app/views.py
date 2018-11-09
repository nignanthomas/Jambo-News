from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''

    title = 'Home - jamboNews'
    return render_template('index.html', title = title)


@app.route('/source/<source_id>')
def source(source_id):
    '''
    View source page function that returns the source and its articles.
    '''
    return render_template('source.html', id = source_id)
