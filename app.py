from first_flask import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# debug mode on allow our application being synchronized everytime we changed our code.
