The application can be ran with gunicorn with the command :

    gunicorn test:app

It can then be accessed by a client through the command :

    curl -i 127.0.0.1:8000

Or directly through a web browser.