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

### POST /purchase/upload

Upload purchases from a csv file in the format:

User_id,Description,Date (**strict format**), Name of Expense Type (**Case sensitive**)

    1,1000,description1,2020-03-20:17:30:00,Football
    1,2000,description2,2020-05-20:11:20:00,Football
    1,1400,description3,2020-07-20:14:30:00,Takeaway
    1,1500,description4,2020-09-20:20:30:00,Bill
    1,1100,description5,2020-11-20:17:30:00,Football

Error is thrown if user doesn't exist. If the expense type doesn't exist, it is created.

The basic form needed for this:

    <form method="post" enctype="multipart/form-data">
        <input type="file" name="purchases">
        <button type="submit">Upload File</button>
    </form>

Where 'name' has to be "**purchases**".

### POST /addition/upload

Upload additions from a csv file in the format:

User_id,Description,Date (**strict format**), Addition_id (**from select**)

    1,1000,description1,2020-03-20:17:30:00,0
    1,2000,description2,2020-05-20:11:20:00,0
    1,1400,description3,2020-07-20:14:30:00,1
    1,1500,description4,2020-09-20:20:30:00,1
    1,1100,description5,2020-11-20:17:30:00,2

Addition_id can be 0 (Salary), 1 (ATM), 2 (Sale)

Error is thrown if user doesn't exist.

The basic form needed for this:

    <form method="post" enctype="multipart/form-data">
        <input type="file" name="additions">
        <button type="submit">Upload File</button>
    </form>

Where 'name' has to be "**additions**".

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
