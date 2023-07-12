# Timski Proekt Back-end

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
