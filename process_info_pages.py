# import string

from module_info import export_dir
from module_info_pages import info_pages

# from process_common import *

def save_info_pages():
  ofile = open(export_dir + "info_pages.txt","w", -1, "utf-8")
  ofile.write("infopagesfile version 1\n")
  ofile.write("%d\n"%(len(info_pages)))
  for i_info_page in range(len(info_pages)):
    info_page = info_pages[i_info_page]
    ofile.write("ip_%s %s %s"%(info_page[0], info_page[1].replace(" ", "_"), info_page[2].replace(" ", "_")))
    ofile.write("\n")
  ofile.close()

def save_python_header():
  ofile = open("./ID_info_pages.py","w")
  for i_info_page in range(len(info_pages)):
    ofile.write("ip_%s = %d\n"%(info_pages[i_info_page][0],i_info_page))
  ofile.write("\n\n")
  ofile.close()

print("Exporting info_page data...")
save_info_pages()
save_python_header()

