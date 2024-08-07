import mock

class IOHandler:
    def prompt(self, message):
        return input(message)

    def echo(self, message):
        print(message)

io = IOHandler()

def get_boolean_response():
    response = io.prompt('y/n').lower()
    while response not in ('y', 'n', 'yes', 'no'):
        io.echo('Not a valid input. Try again')
        response = io.prompt('y/n').lower()

    return response in ('y', 'yes')
