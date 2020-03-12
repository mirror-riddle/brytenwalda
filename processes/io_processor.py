from modules.info import export_dir
from common import lf_open


class IOProcessor:
    """ IOProcessor """

    directory = "./"
    name = "io_processor.txt"

    def __init__(self):
        path = self.directory + self.name
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


class IDIOProcessor(IOProcessor):
    name = "ids.py"
    directory = "../ids/"


class ExportIOProcessor(IOProcessor):
    name = "export.txt"
    directory = export_dir


class ModuleProcessor():
    id_prefix = "id_"
    id_name = "ids.py"
    export_name = "export.txt"

    def __init__(self):
        id_path = "../ids/" + self.id_name
        export_path = export_dir + self.export_name
        self.id_file = lf_open(id_path, "w")
        self.export_file = lf_open(export_path, "w")
        self.after_open()

    def after_open_id_file(self):
        pass

    def after_open_export_file(self):
        pass

    def after_open(self):
        self.after_open_id_file()
        self.after_open_export_file()

    def write_id_file(self, item, index):
        self.id_file.write("%s%s = %d\n" %(self.id_prefix, item[0], index))

    def write_export_file(self, item, *extra_data):
        pass

    def write(self, item, index, *extra_data):
        self.write_id_file(item, index)
        self.write_export_file(item, *extra_data)

    def before_close_id_file(self):
        self.id_file.write("\n\n")

    def before_close_export_file(self):
        pass

    def before_close(self):
        self.before_close_id_file()
        self.before_close_export_file()

    def close(self):
        self.before_close_id_file()
        self.before_close_export_file()
        self.id_file.close()
        self.export_file.close()