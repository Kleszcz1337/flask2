from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', zm='kleszcz')

@app.route('/innastrona') #ustalamy adres naszej podstrony
def innastrona():
    return 'inna strona' #zwracamy co ma być na tej podstronie

@app.route('/klient/<id>') #w <> tworzymy zmienna ktora jest podawana w linku
def klient(id):
    return f'Klient o podanym numerze {id}' # {} wypisuje dane podane z linka, uzywamy tej zmiennej

@app.route('/dodaj/<zmienna1>+<zmienna2>') # http://127.0.0.1:5000/dodaj/12+15
def dodaj(zmienna1,zmienna2):
    wynik = int(zmienna1) + int(zmienna2) 
    return f"Wynik to: {wynik}"



if __name__ == '__main__':
    app.run(debug=True)