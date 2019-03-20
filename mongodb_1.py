# Import Mongo client in order to work with MongoDB
from pymongo import MongoClient 
import pprint
import pymongo
# Assign client to the localhost
client = MongoClient()

#Create database called test-dababase
db = client['test-database'] 
courses = db.course

#Creating an index and setting it to unique
courses.create_index(
    [('course', 1)],
    unique=True
)
#Create a document
#course = {
#    'author': 'Thembela',
#    'course': 'MongoDB Tutorial',
#    'price': 200,
#    'ratings': 4
#}

#creating an array of objects

arr_courses = [
    {
    'author': 'Thembela',
    'course': 'MongoDB Tutorial',
    'price': 200,
    'ratings': 4
},
{
    'author': 'Lebohang',
    'course': 'Mathematics',
    'price': 290,
    'ratings': 5
},
{
    'author': 'Tlhalefo',
    'course': 'Physics',
    'price': 400,
    'ratings': 3
},
{
    'author': 'Colleen',
    'course': 'Life Orientation',
    'price': 500,
    'ratings': 5
},
{
    'author': 'Kabelo',
    'course': 'Life Sciences',
    'price': 390,
    'ratings': 5
}

]

course = {
    'author': 'Thembela',
    'course': 'Something else',
    'price': 200,
    'ratings': 4
}

#Pass document to the dababase created
#result = courses.insert_one(course)

# To check if the data was added in to the database correcntly 

#if result.acknowledged:
   # print('Course data was added ' + str(result.inserted_id))

# Pass array document to database
#results = courses.insert_many(arr_courses)
results = courses.insert_one(course)

#if results.acknowledged:
#    print("Courses added to database " + str(results.inserted_ids))

# For each ID print out___
#for object_id in results.inserted_ids:
 #   print('Courses addad '+ str(object_id))


# Returns the document from the database 
# Returns document where the author is Tlhalefo
#courses = courses.find({
#    'price': {
#        '$gt': 100
#    }
#}).sort('author',pymongo.ASCENDING) #Sort the data in ascending order
#for course in courses:
#    pprint.pprint(course)

# Find all where the price is greater than 100
#courses = courses.find({
#    'price': {
#        '$gt': 100
#    }
#})
#for course in courses:
#    pprint.pprint(course)


#Prints out all the documents in the database
#finds = courses.find()
#for find in courses:
#    print(find)

# Delete all documents from collection where the author is Thembela
#db.course.delete_many({ 'author': "Thembela" })

# Update all the courses to MongoDB Tutorial only
#course.update({
#    'course': "MongoDB Tutorial"
#}, multi= False)


#print(course.find({'author': 'Lebohang'}).count()) # Print out how many Lebohangs are there



#Aggregation
#group by the author name_
#Aggregate function groups the records in a collection, and can be used to provide total number(sum), average, minimum, maximum etc out of the group selected.
#print(list(courses.aggregate([
#    {
#        '$group':{
#            '_id': '$author',
#            '_rate': {
#               '$avg': '$ratings'
#            }

#        }
#    }
# ])))

