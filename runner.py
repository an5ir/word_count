import logging
from app import app

if __name__ == "__main__":
    if app.config['ENVIROMENT'] == 'DEV':
        logging.info('Running in development mode')
        app.run(debug=True)
        app.jinja_env.auto_reload = True
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run()