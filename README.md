# Blog API
An API for simple blog built with Django, Django Rest Framework and Postgres database.
User authorization is provided by Djoser.

API Endpoints allow to sign up and sing in, view all posts and comments, browse comments for specific post, like posts and comments.

## Run server with Docker

- Clone this repo
- In terminal hit `docker-compose run blogserver`
- Close running process with `Ctrl + C`
- Go to the server container with `docker exec -it blogserver bash`
- Migrate database with `python manage.py migrate`
- Run server with `docker-compose up`

## Returning objects

### User object
```json
{
    "user": {
        "id": 2,
        "username": "marco123",
        "first_name": "Marco",
        "last_name": "Polo",
        "bio": "",
        "imageURL": "http://127.0.0.1:7000/static/images/default.png",
        "following": false
    }
}
```

### Post object
```json
{
    "post": {
        "id": 2,
        "author": {
            "id": 2,
            "username": "marco123",
            "first_name": "Marco",
            "last_name": "Polo",
            "bio": "",
            "imageURL": "http://127.0.0.1:7000/static/images/default.png",
            "following": false
        },
        "title": "Spaghetti",
        "content": "Cook the ground beef in a large pot over high heat, stirring quickly and constantly until completely browned 7 to 10 minutes. Stir the onion into the beef; cook and stir until the onion begins to turn translucent, about 5 minutes more. Drain excess grease from meat mixture. Add the mushroom to the mixture; allow to cook until it begins to soften, 1 to 2 minutes. Pour the diced tomatoes and tomato soup into the pot, stir, reduce heat to medium, and bring the mixture to a simmer.",
        "imageURL": "http://127.0.0.1:7000/static/images/post_pics/spaghetti_5z2btZM.png",
        "favorited": false,
        "favoritesCount": 0
    }
}
```

### Multiple Posts objects
```json
{
    "posts": [
        {
            "id": 3,
            "author": {
                "id": 2,
                "username": "marco123",
                "first_name": "Marco",
                "last_name": "Polo",
                "bio": "",
                "imageURL": "http://127.0.0.1:7000/static/images/default.png",
                "following": false
            },
            "title": "Space",
            "content": "Space is the boundless three-dimensional extent in which objects and events have relative position and direction.[1] In classical physics, physical space is often conceived in three linear dimensions, although modern physicists usually consider it, with time, to be part of a boundless four-dimensional continuum known as spacetime.",
            "imageURL": "http://127.0.0.1:7000/static/images/post_pics/spaghetti_NXtUkRY.png",
            "favorited": true,
            "favoritesCount": 1
        },
        {
            "id": 2,
            "author": {
                "id": 2,
                "username": "marco123",
                "first_name": "Marco",
                "last_name": "Polo",
                "bio": "",
                "imageURL": "http://127.0.0.1:7000/static/images/default.png",
                "following": false
            },
            "title": "Spaghetti",
            "content": "Cook the ground beef in a large pot over high heat, stirring quickly and constantly until completely browned 7 to 10 minutes. Stir the onion into the beef; cook and stir until the onion begins to turn translucent, about 5 minutes more. Drain excess grease from meat mixture. Add the mushroom to the mixture; allow to cook until it begins to soften, 1 to 2 minutes. Pour the diced tomatoes and tomato soup into the pot, stir, reduce heat to medium, and bring the mixture to a simmer.",
            "imageURL": "http://127.0.0.1:7000/static/images/post_pics/spaghetti_5z2btZM.png",
            "favorited": false,
            "favoritesCount": 0
        }
    ],
    "postsCount": 2
}
```

### Comment object

```json
{
    "comment": {
        "id": 3,
        "post": 3,
        "author": {
            "id": 2,
            "username": "marco123",
            "first_name": "Marco",
            "last_name": "Polo",
            "bio": "",
            "imageURL": "http://127.0.0.1:7000/static/images/default.png",
            "following": false
        },
        "content": "Great article",
        "favorited": false,
        "favorites_count": 0
    }
}
```

### Multiple Comments object

```json
{
    "comments": [
        {
            "id": 1,
            "post": 2,
            "author": {
                "id": 2,
                "username": "marco123",
                "first_name": "Marco",
                "last_name": "Polo",
                "bio": "",
                "imageURL": "http://127.0.0.1:7000/static/images/default.png",
                "following": false
            },
            "content": "Great article",
            "favorited": false,
            "favorites_count": 0
        },
        {
            "id": 2,
            "post": 2,
            "author": {
                "id": 2,
                "username": "marco123",
                "first_name": "Marco",
                "last_name": "Polo",
                "bio": "",
                "imageURL": "http://127.0.0.1:7000/static/images/default.png",
                "following": false
            },
            "content": "Great article",
            "favorited": false,
            "favorites_count": 0
        }
    ],
    "commentsCount": 2
}
```

## Endpoints

- `post/`
  - `GET` Returns all [posts](#multiple-posts-objects) on the service
  - `POST` Creates new [post](#post-object)

- `post/<id>/`
  - `GET` Returns [post](#post-object) specified by id
  - `PUT` Allows to update post specified by id
  - `DELETE` Allows to delete post specified by id

- `post/<id>/comments/`
  - `GET` Returns comments for post specified by id specified
  - `POST` Create comment for post specified by id

- `post/<id>/favorite/` (Authentication required)
  - `POST` Adds [post](#post-object) specified by id to favorites
  - `DELETE` Deletes [post](#post-object) specified by id from favorites

- `user/<username>/`
  - `GET` Returns [user](#user-object) object specified by username
