from modules.info import export_dir
from modules.info_pages import info_pages
from common import lf_open, replace_spaces
from io_processor import IOProcessor


class IOIDs(IOProcessor):

    def write(self, name, index):
        self.file.write("ip_%s = %d\n" % (name, index))

    def before_close(self):
        self.file.write("\n\n")


class IOInfoPages(IOProcessor):

    def after_open(self):
        self.file.write("infopagesfile version 1\n")
        self.file.write("%d\n" % len(info_pages))

    def write(self, info_page):
        title = replace_spaces(info_page[1])
        content = replace_spaces(info_page[2])
        self.file.write("ip_%s %s %s" % (info_page[0], title, content))
        self.file.write("\n")


def process_info_pages():
    print("Exporting info_page...")

    io_ids = IOIDs("../ids/info_pages.py")
    io_info_pages = IOInfoPages(export_dir + "info_pages.txt")

    for (index, info_page) in enumerate(info_pages):
        io_info_pages.write(info_page)
        io_ids.write(info_page[0], index)

    io_ids.close()
    io_info_pages.close()
