# Zelthy Challenge


## Assignment - 1

Write a python class that is able to send an email from the terminal to a given email address 
using smtplib library. 

### Solution

#### class Email

Created a class Email which uses utils_email.py to get the necesaary utilities for sending an email.
Parameters

##### Parameters
@:param: subject - str

A string which describes the subject of the e-mail.

@:param: body - str

A string which describes the body of the e-mail.

@:param: subject - str

A string which describes the recipient of the e-mail.

##### Methods
send_email()

Builds a EmailMessage object and sends the email to recipient with provided subject and body.

##
## Assignment - 2

Write a python class that is able to return the meaning of an English language word provided to it 
in the terminal. (Use https://dictionaryapi.dev/) 

### Solution

#### class Dictionary

Created a class Dictionary which takes the word as an input and prints its part of speech and definition.

#### Prerequisites 
requirement.txt file consists the requirements for this class.

Requires requests module to interact with the api.

##### Parameters
@:param: query - @instr

A string whose meaning need to be displayed.

##### Methods
search_dictionary()

Queries the word using the dictionary api.
Extracts Part of speech, meaning of the word.


##
## Assignment - 3

Write a python class that is able to return the flight distance between two cities given their 
latitude and longitude coordinates.

### Solution

#### class Points
Created a class Points which stores latitude and longitude of a place as an object.
##### Parameters

@:param: latitude - str

A string which consists of latitude.

@:param: longitude - str

A string which consists of longitude.

##### Methods
split_string(str)

Extracts and Returns the point in the input string.

to_float(point)

Casts the input to float and returns

to_radians(point)

Casts the input to radians and returns

#### class Distance
Created a class Distance used to calculate distance between two points.
##### Parameters
@:param: source - Point

A Point instance which consists of latitude and longitude of source.
    
@:param: destination - Point
    
A Point instance which consists of latitude and longitude of destination.

##### Methods
calculate_distance()

Calculates and prints the distance between two points.

haversine(theta)

Calculates and returns the squared sine(theta).
