from django.db.models.fields.related import ForeignKey

def save_deep(obj):
    """
    This function first saves all the children of the given oject
    and then the object itself. It solves the error:
    ValueError: save() prohibited to prevent data loss due to unsaved related object '<<foreign_object>>'.
    Note: it does not work (yet) with circular dependencies
    """
    if not obj:
        return obj
    for field in obj._meta.get_fields():
        if isinstance(field, ForeignKey):
            foreign = getattr(obj, field.name)
            if foreign:
                saved = save_deep(foreign)
                setattr(obj, field.name, saved)
    obj.save()
    return obj