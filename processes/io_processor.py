from common import lf_open


class IOProcessor:
    """ IOProcessor """

    def __init__(self, path):
        self.file = lf_open(path, "w")
        self.after_open()

    def after_open(self):
        pass

    def write(self):
        pass

    def before_close(self):
        pass

    def close(self):
        self.before_close()
        self.file.close()
