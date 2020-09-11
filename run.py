


from src import create_app
# from src import db

app = create_app()
if __name__ == '__main__':
  app.run(debug=True)