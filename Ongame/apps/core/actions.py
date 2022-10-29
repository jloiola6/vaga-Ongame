from apps.core.models import Historic


def save_history(edit, user, object, table, date):
    historic = Historic()
    historic.user = user
    historic.table = table
    historic.object = object
    historic.date = date
    if edit:
        historic.action = 'E'
    else:
        historic.action = 'A'
    historic.save()


