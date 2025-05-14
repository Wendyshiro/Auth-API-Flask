import os
print("os.environ type:", type(os.environ))
print("os.environ.get type:", type(os.environ.get))

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
