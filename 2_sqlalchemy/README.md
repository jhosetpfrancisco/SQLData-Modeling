# Some Practice forn Interactive mode for Script3

Interactive Mode

```python
from script3 import db, Person
Person.query.all()
Person.query.filter_by(name='Amy')
Person.query
Person.query.filter_by(name='Amy').all()
results = Person.query.filter_by(name='Amy').all()
results[0].id
person = Person(name='Bob 2')
db.session.add(person)
db.session.commit()
Person.query()
person1 = Person(name='New Person 1')
person2 = Person(name='New Person 2')
db.session.add_all([person1],[person2])
db.session.commit()
Person.query()
exit()
```

## Query Methods

Here are some useful query methods to get to know.

## Select records

### all()

```python
MyModel.query.all()
```

same as doing a `SELECT *`, fetching all records from the model's table. Returns a list of objects.

### first()

```python
MyModel.query.first()
```

Fetches just the first result. Returns either `None` or an object if found.

## Filtering

### filter_by

```python
MyModel.query.filter_by(my_table_attribute='some value')

```

Similar to doing a `SELECT \* from ... WHERE` SQL statement for filtering data by named attributes.

### filter

Examples:

```python
MyModel.query.filter(MyOtherModel.some_attr='some value')
OrderItem.query.filter(Product.id=3)
```

Similar to `filter_by`, but instead, you specify attributes on a given Model. It is more flexible than using `filter_by` itself, and is especially useful when querying from a joined table where you want to filter by attributes that span across multiple models.

Similar to `filter_by`, but instead, you specify attributes on a given Model.

- equals: `query.filter(User.name == 'ed')`
- not equals: `query.filter(User.name != 'ed')`
- LIKE: `query.filter(User.name.like('%ed%'))`
- ILIKE (case-insensitive LIKE): `query.filter(User.name.ilike('%ed%'))`
- IN: `query.filter(User.name.in_(['ed', 'wendy', 'jack']))`
- NOT IN: `query.filter(~User.name.in_(['ed', 'wendy', 'jack']))`
- IS NULL: `query.filter(User.name == None)`
- IS NOT NULL: `query.filter(User.name != None)`
- AND: `query.filter(User.name == 'ed', User.fullname == 'Ed Jones')` or chain filter methods together.
- OR: `query.filter(User.name == 'a' | User.name == 'b')`
- MATCH: `query.filter(User.name.match('wendy'))`

## Ordering

### order_by

```python
MyModel.order_by(MyModel.created_at)
MyModel.order_by(db.desc(MyModel.created_at))
```

To order the results by a given attribute. Use `db.desc` to order in descending order.

### limit

```python
Order.query.limit(100).all()
```

`limit(max_num_rows)` limits the number of returned records from the query. ala `LIMIT` in SQL.

## Aggregates

### count()

Example:

```python
query = Task.query.filter(completed=True)
query.count()
```

Returns an integer set to the number of records that would have been returned by running the query.

### get()

Get object by ID

```python
model_id = 3
MyModel.query.get(model_id)
```

Returns the object as a result of querying the model by its primary key.

## Bulk Deletes

Example:

```python
query = Task.query.filter_by(category='Archived')
query.delete()
```

`delete()` does a bulk delete operation that deletes every record matching the given query.

## Joined Queries

Example:

```python
Driver.query.join('vehicles')
```

Query has a method `join(<table_name>)` for joining one model to another table.
