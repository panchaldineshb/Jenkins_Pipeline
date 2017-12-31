import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
print "Let's talk about %s." % config_name

app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)
