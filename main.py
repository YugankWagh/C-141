#In the CSV that we have downloded there should added an 'id' as a colum head because since exporting data frame into a CSV misses out the name of the first column
from flask import Flask, jsonify, request
import csv
# Here we have created four seprate lists and read the CSV file 
all_movies = []

with open('movies.csv',encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)
#This the first API to get the recomendation of all movies when this API is run it is a GET request API
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })
#This the Second API to POST the liked movies to the API server
@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201
#This the thrid API to POST the unliked movies to the API server
@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201
#This the fourth API to POST the did not watch movies to the API server
@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()