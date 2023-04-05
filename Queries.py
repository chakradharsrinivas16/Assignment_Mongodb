from database import moviesCollection,commentsCollection,theatersCollection,usersCollection # importing created instances from database.py
# Importing required libraries
import datetime
from dateutil import parser
from pprint import pprint
class Queries():
    # Inserting record into their respective collections
    def insert_record_dict(collection,data_dict):
        collection.insert_one(data_dict)
    def insert_record(col_no):
        if col_no==1:
            record={
            "name":input("Enter name: "),
            "email":input("Enter email: "),
            "moviesno":{"$oid":input("Enter movie no: ")},
            "text":input("Enter text: "),
            "date":datetime.datetime.utcnow()}
            commentsCollection.insert_one(record)
        if col_no==2:
            record={
                    "plot":input("Enter plot: "),
                    "genres":[input("Enter generes: ") for i in range(int(input("Enter no of generes: ")))],
                    "runtime":int(input("Enter the runtime: ")),
                    "cast":[input("Enter actor: ") for i in range(int(input("Enter no of actors: ")))],
                    "num_mflix_comments":int(input("Enter no of comments: ")),
                    "title":input("Enter tittle: "),
                    "fullplot":input("Enter full plot: "),
                    "countries":[input("Enter country: ") for i in range(int(input("Enter no of countries: ")))],
                    "released":parser.parse(input("Enter the date: ")),
                    "directors":[input("Enter director: ") for i in range(int(input("Enter no of directors: ")))],
                    "rated":input("Enter whether rated or unrated: "),
                    "awards":{"wins":int(input("Enter no of awards won: ")),"nominations":int(input("Enter no of nominatinos: ")),"text":input("Enter text about awards: ")},
                    "lastupdated":datetime.datetime.utcnow(),
                    "year":int(input("Enter the year: ")),"imdb":{"rating":float(input("Enter the imdb rating: ")),"votes":int(input("Enter no of votes in imdb: ")),"id":int(input("Enter the id in imdb: "))},
                    "type":input("Enter type: "),
                    "tomatoes":{"viewer":{"rating":int(input("Enter the tomatoes rating: ")),"numReviews":int(input("Enter the no of reviews in tomato: ")),"meter":int(input("Enter the meter: "))},"lastUpdated":datetime.datetime.utcnow()}}
            moviesCollection.insert_one(record)
        if col_no==3:
            record={"theaterId":int(input("Enter the theater ID: ")),
                    "location":{"address":{"street1":input("Enter the street-1: " ),"city":input("Enter the city: "),"state":input("Enter the state: "),"zipcode":int(input("Enter the zipcode: "))},
                                "geo":{"type":"Point","coordinates":[float(input("Enter the longitude: ")),float(input("Enter the latitude: "))]}}}
            theatersCollection.insert_one(record)
        if col_no==4:
            record={"name":input("Enter name: "),
                    "email":input("Enter email: "),"password":input("Enter password: ")}
            usersCollection.insert_one(record)

    def top10UserWithMaxComment():
        pipe=[
            {"$group":{"_id":"$name","count":{"$sum":1} }},
            {"$sort":{"count":-1}},
            {"$limit":10},
            {"$project" : {"_id":0,"User":"$_id","count":1}}
        ]
        pprint(list(commentsCollection.aggregate(pipeline=pipe)))
    def top10MoviesWithMaxComment():
        pipe=[
            {"$group":{"_id":"$movie_id","count":{"$sum":1} }},
            {"$sort":{"count":-1}},
            {"$limit":10}
        ]
        for doc in commentsCollection.aggregate(pipeline=pipe):
            print("Title: " + moviesCollection.find_one({ "_id":doc["_id"] })['title'] + ", No of Comments: " + str(doc['count']))
    def monthWiseComment(year):
        pipe=[
            { "$project": {"year":{"$year":"$date"} , "month":{"$month":"$date"} }},
            {"$match" : { "year":year }},
            {"$group" : {"_id" : "$month", "count" : {"$sum":1}}},
            {"$project": {"month":"$_id","count":1,"_id":0 }},
            {"$sort" : {"month":1 }}
        ]
        pprint(list(commentsCollection.aggregate(pipe)))
    def Find_top_N_movies_with_the_highest_IMDB_rating():
        pipe=[
                {"$match": {"imdb.rating":{"$ne":""}}},
                {"$sort":{ "imdb.rating":-1}},
                {"$limit":int(input("Enter the value of N: "))},
                {"$project":{"_id":0,"title":1,"imbd.rating":1}}
            ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def Find_top_N_movies_with_the_highest_IMDB_rating_in_year(year):
        pipe=[
                    {"$match": { "$and":[ {"imdb.rating":{"$ne":""}},{"year":year} ]}},
                    {"$sort":{ "imdb.rating":-1}},
                    {"$limit":int(input("Enter the value of N: "))},
                    {"$project":{"_id":0,"title":1,"imbd.rating":1,"year":1}}
                ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def Find_top_N_movies_with_the_highest_IMDB_rating_and_votes_greater_than_1000():
        pipe=[
                {"$match": { "$and":[ {"imdb.rating":{"$ne":""}},{"imdb.votes":{"$gte":1000}} ]}},
                {"$sort":{ "imdb.rating":-1}},
                {"$limit":int(input("Enter the value of N: "))},
                {"$project":{"_id":0,"title":1,"imbd.rating":1,"imdb.votes":1}}
            ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def Find_top_N_movies_with_title_matching_pattern_sorted_by_highest_tomatoes_ratings():
        pipe=[
                {"$match": { "title": {"$regex":input("Enter the regex pattern: "),"$options":"i"}}},
                {"$sort":{ "tomatoes.viewer.rating":-1}},
                {"$limit":int(input("Enter the value of N: "))},
                {"$project":{"_id":0,"title":1,"rating":"$tomatoes.viewer.rating"}}
            ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def Find_top_N_directors_with_maximum_no_of_movies():
        pipe=[
                {"$unwind":"$directors"},
                {"$group":{"_id":"$directors","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$limit":int(input("Enter the value of N: "))}
            ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def Find_top_N_directors_with_maximum_no_of_movies_in_an_year(year):
        pipe=[
                {"$match":{"year":year}},
                {"$unwind":"$directors"},
                {"$group":{"_id":"$directors","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$limit":int(input("Enter the value of N: "))}
            ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def Find_top_N_directors_with_maximum_no_of_movies_in_given_genre(genre):
        pipe=[
                {"$match":{"genres":genre}},
                {"$unwind":"$directors"},
                {"$group":{"_id":"$directors","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$limit":int(input("Enter the value of N: "))}
            ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def Find_top_N_actors_with_maximum_no_of_movies():
        pipe=[
                {"$unwind":"$cast"},
                {"$group":{"_id":"$cast","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$limit":int(input("Enter the value of N: "))}
            ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def Find_top_N_actors_with_maximum_no_of_movies_in_given_year(year):
        pipe=[
                {"$match":{"year":year}},
                {"$unwind":"$cast"},
                {"$group":{"_id":"$cast","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$limit":int(input("Enter the value of N: "))}
            ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def Find_top_N_actors_with_maximum_no_of_movies_in_give_genre(genre):
        pipe=[
                {"$match":{"genres":genre}},
                {"$unwind":"$cast"},
                {"$group":{"_id":"$cast","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$limit":int(input("Enter the value of N: "))}
            ]
        pprint(list(moviesCollection.aggregate(pipe)))
    def top_N_Movies_For__every_Genre():
            pipe=[
                {"$unwind":"$genres"},
                {"$group":{"_id":"$genres"}}
            ]
            for i in list(moviesCollection.aggregate(pipe)):
                genre=i['_id']
                print("Genre: "+genre)
                pipe=[
                    {"$unwind":"$genres"},
                    {"$match":{"genres":genre}},
                    {"$sort":{"imdb.rating":-1}},
                    {"$match":{"imdb.rating":{"$ne":""}}},
                    {"$project":{"_id":0,"title":1,"rating":"$imdb.rating"}},
                    {"$limit":int(input("Enter the value of N: "))}
                ]
                pprint(list(moviesCollection.aggregate(pipe)))    
    def top10CitiesMostTheaters():
            pipe=[
                {"$group":{"_id":"$location.address.city","cnt":{"$sum":1}}},
                {"$sort":{"cnt":-1}},
                {"$limit":10}
            ]
            pprint(list(theatersCollection.aggregate(pipe)))
    def top10theatersNear(cod):
        theatersCollection.create_index([("location.geo", "2dsphere")])
        pprint(list(theatersCollection.find(
        {
        "location.geo": {
            "$near": {
            "$geometry": {
                "type": "Point" ,
                "coordinates": cod
            }}
        }
        }).limit(10)))

    if __name__ == "__main__":
        if(int(input("Choose among the following to perform operation \n    1.To insert new document into any collection. \n    2.To run all the queries\n"))==1):
            insert_record(int(input("Choose where to insert the document \n   1.Comments \n   2.Movies \n   3.Theaters \n   4.Users\n")))
        else:
            print("Question-1.1 Find top 10 users who made the maximum number of comments")
            top10UserWithMaxComment()
            print("Question-1.2 Find top 10 movies who made the maximum number of comments")
            top10MoviesWithMaxComment()
            print("Question-1.3 Given a year find the total number of comments created each month in that year")
            monthWiseComment(int(input("Enter the year: ")))
            print("Question-2.1.1 Find top `N` movies with the highest IMDB rating")
            Find_top_N_movies_with_the_highest_IMDB_rating()
            print("Question-2.1.2 Find top `N` movies with the highest IMDB rating in a given year")
            Find_top_N_movies_with_the_highest_IMDB_rating_in_year(int(input("Enter the year: ")))
            print("Question-2.1.3 Find top `N` movies with the highest IMDB rating, votes more than 1000")
            Find_top_N_movies_with_the_highest_IMDB_rating_and_votes_greater_than_1000()
            print("Question-2.1.4 with title matching a given pattern sorted by highest tomatoes ratings")
            Find_top_N_movies_with_title_matching_pattern_sorted_by_highest_tomatoes_ratings()
            print("Question-2.2.1 Find top `N` directors who created the maximum number of movies")
            Find_top_N_directors_with_maximum_no_of_movies()
            print("Question-2.2.2 Find top `N` directors who created the maximum number of movies in given year")
            Find_top_N_directors_with_maximum_no_of_movies_in_an_year(int(input("Enter the year: ")))
            print("Question-2.2.3 Find top `N` directors who created the maximum number of movies in given genre")
            Find_top_N_directors_with_maximum_no_of_movies_in_given_genre(input("Enter the genre: "))
            print("Question-2.3.1 Find top `N` actors who created the maximum number of movies")
            Find_top_N_actors_with_maximum_no_of_movies_in_given_year(int(input("Enter the year: ")))
            print("Question-2.3.2 Find top `N` actors who created the maximum number of movies in given year")
            Find_top_N_actors_with_maximum_no_of_movies_in_given_year(int(input("Enter the year: ")))
            print("Question-2.3.3 Find top `N` actors who created the maximum number of movies in given genre")
            Find_top_N_actors_with_maximum_no_of_movies_in_give_genre(input("Enter the genre: "))
            print("Question-2.4 Find top `N` movies for each genre with the highest IMDB rating")
            top_N_Movies_For__every_Genre()
            print("Question-3.1 Top 10 cities with the maximum number of theatres")
            top10CitiesMostTheaters()
            print("Question-3.2 Top 10 theatres nearby given coordinates")
            top10theatersNear([float(input("Enter Longitude: ")),float(input("Enter Latitude: "))])
