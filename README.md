# SQL & Data Modeling

This is an excerpt from exercises in Python for handling SQL and data modeling.

## Libraries

| Library               | Url                                        |
| --------------------- | ------------------------------------------ |
| psycopg2              | https://pypi.org/project/psycopg2/         |
| SQLAlchemy (optional) | https://pypi.org/project/SQLAlchemy/       |
| Flask                 | https://pypi.org/project/Flask/            |
| Flask-SQLAlchemy      | https://pypi.org/project/Flask-SQLAlchemy/ |
| Flask-Migrate         | https://pypi.org/project/Flask-Migrate/    |

## Tips

When using the `Flask` cli, keep the following in mind:

```
FLASK_APP={relative_route} FLASK_DEBUG=true flask run

# Example
# FLASK_APP=2_sqlalchemy/script1.py FLASK_DEBUG=true flask run
```
