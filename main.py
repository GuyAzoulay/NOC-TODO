
from website import create_app
# we do this like this because website is python package (__init__.py)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # debug = True means that in every change in the code, the server will restart automatically
    