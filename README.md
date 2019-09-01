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

## 118n and L10n

```sh
    pybabel extract -F babel.cfg -k _l -o messages.pot .
```

To add a new language, you use:

```sh
    flask translate init <language-code>
```

To update all the languages after making changes to the \_() and \_l() language markers:

```sh
    flask translate update
```

And to compile all languages after updating the translation files:

```sh
    flask translate compile
```
