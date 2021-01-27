from flaskr import app
app.config.from_object("settings.DevelopmentConfig")

if __name__ == '__main__':
    app.run()