import os


def handle_uploaded_file(file, path, name):
    if not os.path.exists(path):
        os.makedirs(path)

    path_name = path + '/' + name
    destination = open(path_name, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    return path_name
