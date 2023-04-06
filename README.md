# Assignment_Mongodb

### Database.py
The written Python script that creates a database and collections in MongoDB and imports data from JSON files into the collections, The process is as below -

- The script first imports the required libraries pymongo and subprocess. pymongo is the official Python driver for MongoDB, and subprocess is used to run shell commands from within Python.

- Then, the script creates an instance of the MongoDB client using pymongo.MongoClient. The client connects to the default localhost MongoDB instance running on port 27017.

- Next, the script defines the names of the database and collections to be created. Four collections are defined: comments, movies, theaters, and users.

- After defining the names of the database and collections, the script creates instances of the database and collections using myclient[db_name] and db_instance[collection_name], respectively.

- The create_database_collections class defines a main method, which is where the script actually creates the database and collections and imports data from JSON files into the collections.

- The main method first creates the database using the mongo shell command db.createDatabase(). It then creates the collections using the mongo shell command db.createCollection(), passing in the database name as an argument.

- Next, the script defines the paths to the JSON files containing the data to import. The script then uses the mongoimport shell command to import the data into the corresponding collections, passing in the database name, collection name, and file path as arguments.


### Question - 4.a.1

This Python function that defines a MongoDB aggregation pipeline to find the top 10 users with the most comments. The pipeline consists of the following stages:

- $group stage groups documents by the value of the name field and counts the number of documents in each group using the $sum operator. The _id field is set to the value of the name field so that the results can be grouped by username.

- $sort stage sorts the grouped results in descending order based on the count.

- $limit stage limits the number of documents in the output to 10, i.e., only the top 10 users with the most comments are included in the output.

- $project stage projects only the User and count fields in the output, and excludes the _id field.

### Question - 4.a.2

The function defines a MongoDB aggregation pipeline to find the top 10 movies with the most comments based on the movie_id field in the input documents. The function then iterates through the results of the aggregation pipeline and prints the title of each movie, which is retrieved from a separate collection called moviesCollection, along with the count of comments for that movie.

The pipeline consists of the following stages:

- $group: This stage groups input documents by the value of the movie_id field, and calculates the count of documents in each group using the $sum operator. The result is a set of documents with unique movie_id values and a corresponding count of how many documents in the input have that movie_id value.

- $sort: This stage sorts the grouped documents in descending order based on the count calculated in the previous stage.

- $limit: This stage limits the output to only the top 10 documents based on the count field calculated in the previous stage.

After the aggregation pipeline is executed, the function iterates through the results and retrieves the title of each movie from the moviesCollection using the _id field from the previous stage. Finally, the function prints the movie title and the count of comments for each of the top 10 movies.

### Question - 4.a.3

The function defines a MongoDB aggregation pipeline to count the number of comments made in each month of a specific year. The function takes a year parameter and returns a list of dictionaries, each containing the month and count fields.

The pipeline consists of the following stages:

- $project: This stage extracts the year and month fields from the date field in the input documents using the $year and $month operators.

- $match: This stage filters the documents based on the year field, selecting only documents that match the specified year.

- $group: This stage groups the documents by month, and calculates the count of documents in each group using the $sum operator.

- $project: This stage selects the month and count fields from the grouped documents, and excludes the _id field. The output documents contain only the month and count fields.

- $sort: This stage sorts the output documents in ascending order based on the month field.

### Question - 4.b.1.1

The function defines a MongoDB aggregation pipeline to find the top N movies with the highest IMDB rating. The function takes the the value of N.

The pipeline consists of the following stages:

- $match: This stage filters the documents by selecting only the documents where the imdb.rating field is not empty.

- $sort: This stage sorts the documents in descending order based on the imdb.rating field.

- $limit: This stage limits the output to only the top N documents based on the value entered by the user.

- $project: This stage selects the title and imdb.rating fields from the output documents, and excludes the _id field.


### Question - 4.b.1.2

The function defines a MongoDB aggregation pipeline to find the top N movies with the highest IMDB rating in a specific year. The function takes a year parameter and the value of N. 

The pipeline consists of the following stages:

- $match: This stage filters the documents by selecting only the documents where the imdb.rating field is not empty and the year field matches the specified year.

- $sort: This stage sorts the documents in descending order based on the imdb.rating field.

- $limit: This stage limits the output to only the top N documents based on the value entered by the user.

- $project: This stage selects the title, imdb.rating, and year fields from the output documents, and excludes the _id field.

### Question - 4.b.1.3

The function defines a MongoDB aggregation pipeline to find the top N movies with the highest IMDB rating and at least 1000 votes.

The pipeline consists of the following stages:

- $match: This stage filters the documents by selecting only the documents where the imdb.rating field is not empty and the imdb.votes field is greater than or equal to 1000.

- $sort: This stage sorts the documents in descending order based on the imdb.rating field.

- $limit: This stage limits the output to only the top N documents based on the value entered by the user.

- $project: This stage selects the title, imdb.rating, and imdb.votes fields from the output documents, and excludes the _id field.

### Question - 4.b.1.4

The function defines a MongoDB aggregation pipeline to find the top N movies whose titles match a given regular expression pattern, sorted by their highest tomatoes viewer rating. 

The pipeline consists of the following stages:

- $match: This stage filters the documents by selecting only the documents where the title field matches the regular expression pattern entered by the user.

- $sort: This stage sorts the documents in descending order based on the tomatoes.viewer.rating field.

- $limit: This stage limits the output to only the top N documents based on the value entered by the user.

- $project: This stage selects the title and tomatoes.viewer.rating fields from the output documents, and excludes the _id field.

### Question - 4.b.2.1

The function defines a MongoDB aggregation pipeline to find the top N directors with the maximum number of movies in a given collection. 

The pipeline consists of the following stages:

- $unwind: This stage creates a new document for each element in the directors array field of the input documents, effectively denormalizing the data.

- $group: This stage groups the documents by the directors field and calculates the total number of movies directed by each director using the $sum aggregation function.

- $sort: This stage sorts the output documents in descending order based on the noOfMovies field.

- $limit: This stage limits the output to only the top N documents based on the value entered by the user.

### Question - 4.b.2.2

The function builds a MongoDB aggregation pipeline to find the top N directors with the maximum number of movies in a given year.

The pipeline includes the following stages:

- $match: Filters the documents by the given year.
- $unwind: Deconstructs the directors array to create a separate document for each element in the array.
- $group: Groups the documents by the directors field and calculates the count of movies for each director using the $sum operator.
- $sort: Sorts the documents by the noOfMovies field in descending order.
- $limit: Limits the number of documents to the specified value of N.

### Question - 4.b.2.3
The function takes a genre as input and finds the top N directors with the maximum number of movies in the given genre. The pipeline for this function includes the following stages:

- $match: This stage filters the movies based on the input genre.
- $unwind: This stage splits the directors array into separate documents for each director.
- $group: This stage groups the movies based on the directors and calculates the count of movies for each director.
- $sort: This stage sorts the directors based on the number of movies they have directed in descending order.
- $limit: This stage limits the output to the top N directors based on the input value of N.

### Question - 4.b.3.1

This function will find the top N actors with the maximum number of movies they have acted in. The pipeline does the following:

- $unwind the cast array to get individual actors as separate documents.
- $group by the actor's name and count the number of movies they have acted in using $sum.
- $sort the documents by the count of movies in descending order.
- $limit the documents to N.
The value of N is taken as input from the user.

### Question - 4.b.3.2

This function uses aggregation pipeline to find the top N actors with the maximum number of movies in a given year. The pipeline first matches the documents with the given year, then it unwinds the cast array to create a document for each actor in the cast. Then it groups the documents by actor and calculates the count of movies for each actor. It then sorts the result in descending order of movie counts and limits the output to the top N actors. Finally, it returns the result as a cursor object. The value of N is taken as input from the user.

- $match: This stage filters the documents based on a given condition. In this case, it filters the documents based on the year of the movie.

- $unwind: This stage creates a new document for each element in an array. In this case, it creates a new document for each actor in the cast array.

- $group: This stage groups the documents based on a given key and applies an accumulator operation to each group. In this case, it groups the documents by the cast field and calculates the number of movies for each actor using the $sum accumulator.

- $sort: This stage sorts the documents based on a given field. In this case, it sorts the documents in descending order of the noOfMovies field.

- $limit: This stage limits the number of documents in the output to a specified number.


### Question - 4.b.3.3

The function aims to find the top N actors who have acted in the maximum number of movies in a given genre. It takes a genre as an input parameter and uses the aggregate() function to perform aggregation operations on the movies collection. The pipeline consists of the following stages:

- $match: This stage filters the movies collection to include only those movies that have the given genre.

- $unwind: This stage deconstructs the cast array field into individual documents, creating a new document for each actor who acted in the movie.

- $group: This stage groups the documents by the cast field and calculates the count of movies in which each actor has acted.

- $sort: This stage sorts the grouped documents in descending order based on the count of movies in which each actor has acted.

- $limit: This stage limits the output to the top N actors based on the count of movies in which each actor has acted.
collection named "moviesCollection". The pipeline of the function works as follows:

### Question - 4.b.4

- The first stage of the pipeline is "$unwind" stage. It creates a copy of each document for every element in the "genres" array, allowing for grouping by genre later.

- The second stage groups the documents by "genres" field and creates a new document with the "_id" field representing the genre.

- The function then loops through the list of genres and creates a pipeline for each genre.

- The pipeline for each genre starts with an "$unwind" stage that creates a copy of each document for every element in the "genres" array.

- The next stage "$match" filters the documents where the "genres" field matches the current genre.

- The next stage "$sort" sorts the matching documents by descending "imdb.rating" values.

- The next stage "$match" filters out documents with empty "imdb.rating" fields.

- The next stage "$project" outputs the "title" and "imdb.rating" fields.

Finally, the "$limit" stage limits the output to the top N movies, where N is taken as input from the user.

### Question - 4.c.1

The top10CitiesMostTheaters function retrieves the top 10 cities with the most number of theaters. It does this by using the aggregate function to apply a pipeline of aggregation stages to the theatersCollection.

- The first stage is $group which groups the documents by the city in the location.address field and applies a $sum accumulator to count the number of documents per city. The result of this stage is an intermediate collection where each document has a _id field corresponding to the city name and a cnt field with the count of documents.

- The second stage is $sort which sorts the documents in descending order based on the cnt field.

- The third and last stage is $limit which limits the number of documents in the output to 10.

### Question - 4.c.2

The function top10CitiesMostTheaters() retrieves the top 10 cities with the most number of theaters. It does so by using the aggregate() method to perform aggregation on the theaters collection.

The aggregation pipeline consists of the following stages:

- $group: This stage groups documents by the location.address.city field and calculates the count of documents in each group using the $sum operator. The result of this stage is a document for each unique city with the count of theaters in that city.

- $sort: This stage sorts the documents in descending order based on the cnt field, which is the count of theaters in each city.

- $limit: This stage limits the output to the first 10 documents, which are the cities with the highest count of theaters.

### Test Run

<img width="964" alt="Screenshot 2023-04-05 at 11 08 53 PM" src="https://user-images.githubusercontent.com/123494344/230160796-7b8abc31-9424-4152-a358-0cdcf77c70fc.png">
<img width="669" alt="Screenshot 2023-04-05 at 11 09 16 PM" src="https://user-images.githubusercontent.com/123494344/230160950-a6989e88-097e-402a-abae-a46cbd00fe17.png">
<img width="607" alt="Screenshot 2023-04-05 at 11 09 32 PM" src="https://user-images.githubusercontent.com/123494344/230160991-b5e59334-e420-4be6-8699-d5574e9e8130.png">
<img width="705" alt="Screenshot 2023-04-05 at 11 09 45 PM" src="https://user-images.githubusercontent.com/123494344/230161006-03841406-2939-4131-bde7-ef7c4f93cafb.png">
<img width="654" alt="Screenshot 2023-04-05 at 11 09 55 PM" src="https://user-images.githubusercontent.com/123494344/230161038-b8ba186f-c09d-4650-ab59-4d9fc8daa16f.png">
<img width="605" alt="Screenshot 2023-04-05 at 11 10 10 PM" src="https://user-images.githubusercontent.com/123494344/230161066-013d3ec6-7ad4-4cdb-94a6-34d8aa7e89ec.png">
<img width="808" alt="Screenshot 2023-04-05 at 11 10 28 PM" src="https://user-images.githubusercontent.com/123494344/230161272-470fc962-225a-4e7e-9f1a-e90c3a86ed8a.png">
<img width="674" alt="Screenshot 2023-04-05 at 11 10 37 PM" src="https://user-images.githubusercontent.com/123494344/230161120-f187709b-16f3-4dcf-b4c8-c1b7a018363e.png">


