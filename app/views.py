from flask import render_template
from app import app
from .request import get_sources,get_articles,search_articles

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''

    title = 'Home - jamboNews'

    #Getting Science Sources
    science_sources = get_sources('science')

    #Getting Business Sources
    business_sources = get_sources('business')

    #Getting Entertainment Sources
    entertainment_sources = get_sources('entertainment')

    #Getting General Sources
    general_sources = get_sources('general')

    #Getting Health Sources
    health_sources = get_sources('health')

    #Getting Sports Sources
    sports_sources = get_sources('sports')

    #Getting Technology Sources
    technology_sources = get_sources('technology')



    return render_template('index.html', title = title, science = science_sources, business = business_sources, entertainment = entertainment_sources, sports = sports_sources, health = health_sources, general = general_sources, technology = technology_sources)


@app.route('/source/<id>')
def source(id):
    '''
    View source page function that returns the source and its articles.
    '''
    all_articles = get_articles(id)
    title = f'jamboNews -- {id.upper()}'
    id_up = id.upper()

    return render_template('source.html', articles = all_articles, title = title, id_up = id_up)


@app.route('/search/<query>')
def search(query):
    '''
    View function to display the search results
    '''
    query_list = query.split(" ")
    query_format = "+".join(query_list)
    searched_articles = search_articles(query_format)
    title = f'Search results for "{query}"'
    return render_template('search.html',articles = searched_articles)
