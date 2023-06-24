# Migrations

Create initial migration directory structure

```
FLASK_APP=script1.py flask db init
```

Detects the model changes to be made, and creates a migration file with upgrade and downgrade logic set up.

```
FLASK_APP=script1.py flask db migrate
```

Runs the upgrade comman in the migration file, to apply the migration

```
FLASK_APP=script1.py flask db upgrade
```

Runs the downgrade command in the migration file, to roll back the migration

```
FLASK_APP=script1.py flask db downgrade
```

## Working with existing data

You should be seeing ERRORS ERRORS ERRORS

`source/migrations/versions/___.py`

Modify the code as shown below

```python
op.add_column('todos', sa.Column('completed',sa.Boolean(), nullable = True))
op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
op.alter_column('todos','completed', nullable =False)
```

Terminal

```
FLASK_APP=script1.py flask db upgrade
```

## Tip

Just set:

```
export FLASK_APP=script1.py
```
