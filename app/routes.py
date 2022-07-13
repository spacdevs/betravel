def init_app(app):
    @app.get('/')
    def index():
        return 'Olá, Flask!'

