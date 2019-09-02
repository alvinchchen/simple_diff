'''
simple diff tool for dictionary and list
'''

def dict_diff(old_one, new_one):
    """ diff two dict and fill the result """
    result = {'created': [], 'deleted': [], 'modified': [], 'unchanged': []}

    old_dict = dict(old_one)
    new_dict = dict(new_one)

    for old_key, old_value in old_one.items():
        for new_key, new_value in new_one.items():
            if old_key == new_key:

                new_item = {'key': new_key, 'value': new_value}
                old_item = {'key': old_key, 'value': old_value}

                if old_value != new_value:
                    modified_item = {'new': new_item, 'old': old_item}
                    result['modified'].append(modified_item)
                else:
                    result['unchanged'].append(new_item)

                old_dict.pop(old_key)
                new_dict.pop(new_key)

    for key, value in old_dict.items():
        result['deleted'].append({'key': key, 'value': value})

    for key, value in new_dict.items():
        result['created'].append({'key': key, 'value': value})

    return result


def list_diff(old_one, new_one, key):
    """ diff two config list and fill the result , have to specify the index key """
    result = {'created': [], 'deleted': [], 'modified': [], 'unchanged': []}

    old_list = list(old_one)
    new_list = list(new_one)

    for old_item in old_one:
        for new_item in new_one:
            if old_item[key] == new_item[key]:
                if old_item != new_item:
                    modified_item = {'new': new_item, 'old': old_item}
                    result['modified'].append(modified_item)
                else:
                    result['unchanged'].append(new_item)

                old_list.remove(old_item)
                new_list.remove(new_item)

    result['created'] = new_list
    result['deleted'] = old_list

    return result
