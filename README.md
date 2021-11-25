save_deep
=========

This package first saves all the children of the given oject and then the object itself. 
It solves the error:
`ValueError: save() prohibited to prevent data loss due to unsaved related object '<<foreign_object>>'.`

Note: it does not work (yet) with circular dependencies

Example
-------

Say you have this this model

```python

class Company(models.Model):
    name = models.CharField(max_length=256)

class Employee(models.Model):
    username = models.CharField(max_length=256)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
```

If you try to do

```python
Employee(username='tom', company=Company(name='some-name')).save()
```

you get

```
ValueError: save() prohibited to prevent data loss due to unsaved related object '<<foreign_object>>'.
```

But if you use save_deep, the company is saved first, then the employee

```python
employee = save_deep(Employee(username='tom', company=Company(name='some-name')))
```

This works with a deeply nested object-tree and with updates (and update/create-mixes) as well as long 
as there are no circular dependencies.