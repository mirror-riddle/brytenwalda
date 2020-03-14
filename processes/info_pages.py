from modules.info_pages import info_pages
from module_processor import ModuleProcessor
from common import replace_spaces


class InfoPageProcessor(ModuleProcessor):
    id_prefix = "ip_"    
    id_name = "info_pages.py"
    export_name = "info_pages.txt"

    def after_open_export_file(self):
        self.export_file.write("infopagesfile version 1\n")
        self.export_file.write("%d\n" % len(info_pages))

    def write_export_file(self, info_page):
        title = replace_spaces(info_page[1])
        content = replace_spaces(info_page[2])
        self.export_file.write("ip_%s %s %s\n" % (info_page[0], title, content))


def process_info_pages():
    print("exporting info_pages...")
    processor = InfoPageProcessor()
    for index, info_page in enumerate(info_pages):
        processor.write(info_page, index)
    processor.close()