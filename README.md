A FastAPI project that stores brittanica books.
CRUD functionality available
Docs are available at ../docs

[SWAGGER DOCUMENTATION](https://britanncaflask.pythonanywhere.com/)
![Library Gif](https://media1.tenor.com/images/94a98af4e6d102c32034b46920d0317e/tenor.gif?itemid=9965365)

# BOOKS

### GET ALL BOOKS (GET)

                https://britanncaflask.pythonanywhere.com/api/books

### GET SPECIFIC BOOK (GET)
                https://britanncaflask.pythonanywhere.com/api/books/{id}


### CREATE NEW BOOK (POST)
                https://britanncaflask.pythonanywhere.com/api/books


*payload (Example Value)*
```js
{
  "title": "string",
  "user_id": 0,
  "locccn": 0
}
```

### UPDATE A BOOK (PUT)
                https://britanncaflask.pythonanywhere.com/api/books/{id}

*payload (Example value)*
```js
{
  "title": "string",
  "user_id": 0,
  "locccn": 0
}
```
### DELETE A BOOK
                https://britanncaflask.pythonanywhere.com/api/books/{id}

# USERS
### GET ALL USERS (GET)
                https://brittanica-books.onrender.com/api/v1/users

### GET SPECIFIC USER (GET)
                https://brittanica-books.onrender.com/api/v1/users{id}

### CREATE NEW USER (POST)
                https://brittanica-books.onrender.com/api/v1/users


*payload (Example Value)*
```js
{
  "username": "string"
}
```

### UPDATE A USER (PUT)
            https://brittanica-books.onrender.com/api/v1/users/{id}

*payload (Example value)*
```js
{
  "username": "string"
}
```

### DELETE A USER (DELETE)
                https://britanncaflask.pythonanywhere.com/api/users/{id}
