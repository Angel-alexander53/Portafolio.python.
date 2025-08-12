from flask import Flask, render_template

app = Flask(__name__)

#Ruta  principal
@app.route('/')
def index():
    return render_template('index.html')

# RUta de ejemplo
@app.route('/about')
def about():
    return "<h1>Pagina About</h1>"

if __name__ == ' __main__':
    app.run(debug=True)