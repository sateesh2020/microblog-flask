# microblog-flask

## Initializing Database

```sh
    flask db init
```

## Database Migrations

```sh
    flask db migrate -m "database migration"
```

And the migration needs to be applied to the database:

```sh
    flask db upgrade
```
