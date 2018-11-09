class Config:
    '''
    General configuration parent class.
    '''
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&country=us&apiKey={}'


class ProdConfig(Config):
    '''
    Production configuration class

    Args:
        Config: The parent configuration class with General configuration settings.
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent cinfiguration class with general cinfiguration settings.
    '''

    DEBUG = True
