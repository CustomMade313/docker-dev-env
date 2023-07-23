import os
import sys

COMMANDS = {
    'id' : 'docker ps -aqf "name={0}"',
    # docker-compose exec  {0} -> container-name {1} -> command and args
    'exec': 'docker-compose exec {0} {1}'
}

ARTISAN_PATH = '/var/www/artisan'
# test.py php artisan migrate

commnad_name = ''
args = ''

if  len(sys.argv) == 1 :
    print("{COMMAND_NAME} {ARGS}")
    print("Example command: php artisan migrate")
    command = input('$')
    splitted_data = command.split(" ")
    command_name = splitted_data.pop(0)
    args = splitted_data

else:
    splitted_data = sys.argv
    splitted_data.pop(0)
    command_name = splitted_data.pop(0)
    args = splitted_data



str_args = ""
if command_name == "php":
    for item in args:
        if item == "artisan":
            str_args += "{0} ".format(ARTISAN_PATH)
        else:
            str_args += "{0} ".format(item)
else:
    for item in args:
        str_args += "{0} ".format(item)

if command_name == "mysql":
    str_args += ';'

print(command_name)
print(str_args)
os.system(COMMANDS['exec'].format(command_name, "{0} {1}".format(command_name, str_args)))