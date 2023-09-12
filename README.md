# Timski Proekt Back-end

## Overview

This is a Django project that hosts our teams back-end. It is hosted on an AWS EC2 instance using Docker Compose, on the url
https://tp.sekuloski.mk. The project consists of an NGINX container, which directs tp.sekuloski.mk request to the back-end, and the 
actual project 'timskiproekt'. Both of these are connected using the docker-compose.yml file, hosted on port 443. The Django project is 
very simple, using the added libraries 'djangorestframework' for REST API call, 'djangorestframework-simplejwt' for JWT token management,
and 'gunicorn' which is a production server hoster. To run this project locally, run the following command:

    sudo docker compose up -f ./docker-compose.dev.yml -d --build

This will run the development docker compose project and host the project on localhost:8000.

## Endpoints

One thing to note, every endpoint must end with a '/'
The following endpoints are available:

### POST /customer/login/

    {
       "email": "",
       "password": ""
    }

Returns an Access and a Refresh token. Store these as a cookie. The access token is used 
as a credential for the user, while the refresh token is used to refresh the access token.


### POST /customer/login/refresh/

    {
       "refresh": "" <- REFRESH TOKEN HERE
    }

If a logged-in user gets a 401 unauthorized, refresh the token and try again.
Returns an Access token.

### POST /customer/register/

    {
        "password": "",
        "password2": "",
        "email": "",
        "first_name": "",
        "last_name": "",
        "date_of_birth": "YYYY-MM-DD"
    }

Returns the new user, doesn't automatically log him in.

### POST /customer/logout/

Logs the user out of the current device.

### POST /customer/logout_all/

Logs the user out of all devices by disabling his refresh token.

### GET /purchase/ 

Get all purchases from the user that is logged in - Requires Authentication

### GET /purchase/1

Get the purchase with id '1' if the user has access to it. - Requires Authentication

### POST /purchase/upload/

Upload purchases from a csv file in the format:

Description,Date (**strict format**), Name of Expense Type (**Case sensitive**)

    1000,description1,2020-03-20:17:30:00,Football
    2000,description2,2020-05-20:11:20:00,Football
    1400,description3,2020-07-20:14:30:00,Takeaway
    1500,description4,2020-09-20:20:30:00,Bill
    1100,description5,2020-11-20:17:30:00,Football

Error is thrown if user isn't logged in. If the expense type doesn't exist, it is created.

The basic form needed for this:

    <form method="post" enctype="multipart/form-data">
        <input type="file" name="purchases">
        <button type="submit">Upload File</button>
    </form>

Where 'name' has to be "**purchases**".

### POST /addition/upload/

Upload additions from a csv file in the format:

Description,Date (**strict format**), Addition_id (**from select**)

    1000,description1,2020-03-20:17:30:00,0
    2000,description2,2020-05-20:11:20:00,0
    1400,description3,2020-07-20:14:30:00,1
    1500,description4,2020-09-20:20:30:00,1
    1100,description5,2020-11-20:17:30:00,2

Addition_id can be 0 (Salary), 1 (ATM), 2 (Sale)

Error is thrown if user isn't logged in

The basic form needed for this:

    <form method="post" enctype="multipart/form-data">
        <input type="file" name="additions">
        <button type="submit">Upload File</button>
    </form>

Where 'name' has to be "**additions**".

### GET /addition/ 

Get all additions from the user that is logged in - Requires Authentication

### GET /addition/1/

Get the addition with id '1' if the user has access to it. - Requires Authentication

## Models

### User
- First Name 
- Last Name 
- date of birth: DateTime 
- funds: Int

### Purchase
- amount: Int 
- description: String (reason for purchase, location, etc..)
- date: DateTime 
- OneToMany to Expense Type 
- OneToMany to User

### Expense Type
- name: String 

### Addition
- amount: int 
- description: String 
- date: DateTime 
- type: Enum 
- OneToMany to User
