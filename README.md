# LocationServiceApp


This Application is based on Flask framework and IDE used Pycharam 

<h3>Requirement for This App:</h3><br>

 -Framework : Flask
 <br>
 -Database : MySql<br>
 -Database Connector : pymysql<br>
 -Request Limiting for user  : flask-limiter <br>
 -Python : 3  or above <br>
 
 
<h2> To run this Application:</h2><br>
 install all dependancies  <br>
 
<h2>  To create Data </h2>  <br>
 run db_table_schema_with_data.sql to create data or<br>
 if you want to use schema of db , run db_table_schema.sql <br>
 and to enter your data use script DataPreparation.py script to generate the data <br>
 sample data is provide in final_geo_data.txt<br>
 
 <br>
 Note :<br>
        /user : to get the list of location based on entered text (user input is harcoded in app.py )<br>
        /location : to get the list of location based on given lat, long with a range <br>
 
 To restrict a perricular IP address to request to a certain number is handled by the flask-limiter<br>
        
        
 
 
 
