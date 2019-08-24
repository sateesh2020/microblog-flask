# microblog-flask

## Initializing Database

```sh
    flask db init
```

## Database Migrations

### Users

```sh
    flask db migrate -m "users table"
```

And the migration needs to be applied to the database:

```sh
    flask db upgrade
```

### Posts

```sh
    flask db migrate -m "posts table"
```

And the migration needs to be applied to the database:

```sh
    flask db upgrade
```
