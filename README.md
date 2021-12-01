# token_based_rest_api
Boilerplate for a token based REST API build with Django Restframework.



This is a ready to use solution which works well with Python 3.7.

Check the urls.py for all the endpoints. To hit an endpoint you need to authenticate. At first, you can do this by sending a username and a password to the endpoint "/generate_a_token/" via POST-request. You will receive an token in JSON format. Add this token to every further request you will make to this API. Otherwise you will get an unauthorized error. 

I added two models and serializer for you which you can delete if you want. The views are function based, if you prefer class based views feel free to add them. 

Happy coding. 

CT




