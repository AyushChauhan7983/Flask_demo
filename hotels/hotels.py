from flask import Flask,render_template

app = Flask(__name__)

@app.route("/hotels")
@app.route("/")

def hotels():
    hotel_ratings = [
        {'ID':1, 'name':'Maple Tree', 'rating':4},
        {'ID':2, 'name':'Regents', 'rating':5},
        {'ID':3, 'name':'DropInn', 'rating':3},
    ]

    rows=''
    for hotel in hotel_ratings:
        rows+='<tr><td>' + hotel.get('name') + '</td></tr>'
    return render_template("index.html",hotel_ratings=hotel_ratings)

if __name__ == "__main__":
    app.run(debug=True)