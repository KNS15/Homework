file_name = 'dz.txt'
file = open(file_name, mode='rb')
file_content = file.read()
file.close()
print(file_content)
