from modules.items_helper import all_light_helments

def handle_item(item):
    return "itm_" + item[0]


items = all_light_helments

results = map(handle_item, items)

for item in results:
    print('"%s",' % item)
