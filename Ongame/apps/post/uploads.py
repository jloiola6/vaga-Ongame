import os


def handle_uploaded_file(file, path, name):
    if not os.path.exists(path):
        os.makedirs(path)

    name = path + '/' + name
    destination = open(name, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

    return name
