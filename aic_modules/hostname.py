import socket

from aic.interface import AicModule


class Hostname(AicModule):

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    def run(self):
        return {'hostname': socket.gethostname()}

    def module_name(self):
        return "Hostname"
