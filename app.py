from flaskr import app
from flasgger import Swagger

swagger = Swagger(app)
app.config.from_object("settings.DevelopmentConfig")

if __name__ == '__main__':
    app.run(
        port=12004
    )
