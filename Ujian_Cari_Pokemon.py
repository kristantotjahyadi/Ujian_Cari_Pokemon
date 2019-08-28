from flask import Flask, request, render_template,redirect,jsonify
import requests



app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/hasil',methods=['GET','POST'])
def hasil():
    body = request.form
    nama_Pokemon = body['nama'].lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{nama_Pokemon}'
    data = requests.get(url)
    if data.status_code == 404:
        return render_template('error.html')
    elif data.status_code == 200:
        pokemon = data.json()
        nama = (pokemon['forms'][0]['name']).capitalize()
        ID = str(pokemon['id'])
        tinggi = str(pokemon['height'])
        berat = str(pokemon['weight'])
        gambar = (pokemon['sprites']['back_default'])
        return render_template(
            'hasil.html',
            data = {
                'name' : nama, 'id' : ID, 'height': tinggi,'weight':berat, 'img' : gambar  
            }
        )

        
if __name__ == '__main__':
    app.run(debug=True)
