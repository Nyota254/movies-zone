from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initialising the flask extensions
    bootstrap.init_app(app)

    #Will add the views and forms

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app

































""" from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

#Initialising the application
app = Flask(__name__)

#Creating app configurations
app.config.from_object(config_options[config_name])

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing flask extensions
bootstrap = Bootstrap(app)

# from app import views
# from app import error

#We will add the views and forms

return app """