class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category



class Articles:
    '''
    Articles class to define Articles Objects
    '''

    def __init__(self,title,image,description,url,date):
        self.title = title
        self.image = image
        self.description = description
        self.url = url
        self.date = date
