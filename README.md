# Timski Proekt Back-end

## Endpoints

### POST /customer/login

    {
       "email": "",
       "password": ""
    }


### POST /customer/login/refresh

    {
       "refresh": ""
    }

### POST /customer/register/

    {
        "password": "",
        "password2": "",
        "email": "",
        "first_name": "",
        "last_name": "",
        "date_of_birth": "YYYY-MM-DD"
    }

### POST /customer/logout/
### POST /customer/logout_all/
### GET /purchase/ 
Get all purchases from the user that is logged in - Requires Authentication

### GET /addition/ 

Get all additions from the user that is logged in - Requires Authentication

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
