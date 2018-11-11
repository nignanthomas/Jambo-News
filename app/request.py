from app import app
import urllib.request,json
from .models import source,articles

Source = source.Source
Articles = articles.Articles

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the source base url
base_url = app.config['SOURCE_API_BASE_URL']

#Getting articles base url
articles_url = app.config['ARTICLES_BASE_URL']




def get_sources(category):
    '''
    Function that gets the json response to our url request.
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    print(source_results)
    return source_results



def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        source_object = Source(id,name,description,url,category)
        source_results.append(source_object)

    return source_results



def get_articles(id):
    '''
    Function that gets the json response to our articles url request.
    '''
    get_all_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_all_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    print(articles_results)
    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        title = articles_item.get('title')
        image = articles_item.get('urlToImage')
        description = articles_item.get('description')
        url = articles_item.get('url')
        date = articles_item.get('publishedAt')

        if image:
            articles_object = Articles(title,image,description,url,date)
            articles_results.append(articles_object)

    return articles_results


def search_articles(query):
    '''
    Function that gets the json response to our articles search url request.
    '''
    search_articles_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(query,api_key)

    with urllib.request.urlopen(search_articles_url) as url:
        search_articles_data = url.read()
        search_articles_response = json.loads(search_articles_data)

        search_articles_results = None

        if search_articles_response['articles']:
            search_articles_list = search_articles_response['articles']
            ssearch_articles_results = process_articles(search_articles_list)


    return search_articles_results
