from flask import Flask,render_template,request,redirect,url_for
import sqlite3



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here
   # return ("<h1>Jestem na stronie domowej<br><a href='addMovie'>Idź do strony dodawania</a>")
   db = sqlite3.connect('movies.db')
   cursor = db.cursor()
   cursor.execute('SELECT * FROM movies')
   lista=[]
   for row in cursor.fetchall():
        lista.append(row)
   if (request.method == 'POST'):
       db = sqlite3.connect('movies.db')
       movies_to_remove_ids = request.form.getlist('movieToRemove')
       for a in movies_to_remove_ids:
           print(a)
           cursor = db.cursor()
           cursor.execute(f'DELETE FROM movies WHERE id={a}')
           db.commit()
       return redirect(url_for('home'))


   return render_template('home.html', movies = lista)

@app.route('/addMovie', methods=['GET', 'POST'])
def add_movie():  # put application's code here
    #return ("<h1>Jestem na stronie domowej<br><a href='./'>Idź do strony glownej</a>")

    if(request.method == 'POST'):
        db = sqlite3.connect('movies.db')
        title = request.form.get('title')
        year = request.form.get('year')
        actors = request.form.get('actors')
        cursor = db.cursor()
        cursor.execute(f'INSERT INTO movies (title, year, actors) VALUES ("{title}","{year}","{actors}")')
        db.commit()
        return redirect(url_for('home'))

    return render_template('add.html')
if __name__ == '__main__':
    app.run()
