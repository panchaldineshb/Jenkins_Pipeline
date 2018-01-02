class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    # disable track modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CSRF_ENABLED = True
    SECRET_KEY = 'devopsdemo_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:meeN$2402@localhost/sarabi'

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
