def write_file(file_path, content):
    with open(f'{file_path}.txt', mode='w') as file:
        file.write(content)

def append_file(file_path, content):
    with open(f'{file_path}.txt', mode='a') as file:
        file.write(content)

def read_file(file_path):
    with open(f'{file_path}.txt', mode='r') as file:
        return file.read()