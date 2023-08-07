# Timski Proekt Back-end

## Endpoints

### POST /customer/login

    {
       "email": "",
       "password": ""
    }

Returns an Access and a Refresh token. Store these as a cookie. The access token is used 
as a credential for the user, while the refresh token is used to refresh the access token.


### POST /customer/login/refresh

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

### GET /addition/ 

Get all additions from the user that is logged in - Requires Authentication

### GET /addition/1

Get the addition with id '1' if the user has access to it. - Requires Authentication

## Models:

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
