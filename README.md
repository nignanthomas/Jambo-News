# #jamboNews
===================

- - - -
## Author
[nignanthomas](https://github.com/nignanthomas)

## Description
jamboNews is a web appliction that displays a list of news sources. You are able to click on a news source and view a list of articles from that source. You can now click on the `Read More` button to be redirected to the full article's webpage.

------------------------------------------------------------------------

## User Story

1. As a user, I would like to see various news sources on the homepage of the application.
2. As a user, I would also want to select a news source and see all news articles from the selected news source in the application.
3. As a user, I would want to see the image, description and the time a news article was created.
4. As a user, I would want to click on an article and read the full article on the source website.

## Features

+ [x] List various news sources.
+ [x] List articles from the selected news source.
+ [x] Redirect user to the actual article.
+ [x] Categorize news sources.
+ [x] Search for articles.
+ [ ] Use flask sessions to save a users article snippet.
+ [ ] Use browser cookies to store favourite news sources.


## Installation


### Cloning the repository
```
git clone https://github.com/nignanthomas/Jambo-News.git && cd Jambo-News
```

### Creating a virtual environment
```
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```
pip3 install -r requirements
```
The following libraries are required
* Flask==0.12.2
* Flask-Bootstrap==3.3.7.1
* Flask-Script==2.0.6
* gunicorn==19.7.1


### Running Tests
```
python3 manage.py test
```

### Running the web app in development
```bash
python3 manage.py server
```
Open the app on your browser, by default on `127.0.0.1:5000`.

## Live Demo

https://jambo-news.herokuapp.com/



## Technology used

* Python3.6
* Flask
* Heroku


## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is under the MIT Open Source license, (c) 2018 [nignanthomas](https://github.com/nignanthomas)
