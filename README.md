# USAGE
## login
POST  
```
/api/v1/rest-auth/login
```

parameters
```
username, password, email
```

response
```
token
```

## logout
GET
```
/api/v1/rest-auth/logout
```
## register
POST
```
/api/v1/rest-auth/registration
```

parameters
```
username, email, password, confirm_password
```

response
```
token
```

## user list
GET
```
/api/v1/users
```

response
```
userlist
```

GET
```
/api/v1/user/{userID}
```

response
```
username
```