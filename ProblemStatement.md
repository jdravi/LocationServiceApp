                                     Location Service
<b>Problem Statement </b>:
<br>
Design and implement a location search micro service, whose sole purpose is be to
expose APIs for searching cities and their localities.
You are free to use any backend language and frameworks.
Submit your answer as a Git repository hosted on any of the major platforms like GitHub,
Bitbucket, etc.
<br>
Assumptions
<br>
1. You have a massive database of cities and their localities.<br>
2. Every request you receive contains a custom header X-Geo-LatLng which contains the
latitude and longitude of the request origin.
3. You are not expected to implement an front-end application for this problem statement,
just expose APIs that return JSON formatted results.
Tasks
<br>
Design the database schema as per the following,<br>
You have list of city names.<br>
You have list of city locality names, along with their latitude and longitude, and in
which city the locality lies.<br>
Expose an API, where a user enters some text and the service returns the first 5 relevant
city/locality simulating a type-ahead search. For e.g., if a user enters the text mum , the
results should be like Mumbai, Mumbra, Mumbai Central, etc.<br>
The result of the above should be sorted on the basis of geo-distance from the current
location (note the above assumption no. <br>2).
Expose another API, where the user enters a latitude and longitude, and the service
returns all the city localities within a geo-distance of 10 kms and sorted on the basis of
their respective distance from the user input.<br>
Since above APIs would be public, you are also required to apply Rate Limiting of 100
requests per minute per IP address on the above exposed APIs.
