#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def look_4next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes: are List which contain all the boxes with their keys
    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    helpbox = {}
    while True:
        if len(helpbox) == 0:
            helpbox[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_4next_opened_box(helpbox)
        if keys:
            for key in keys:
                try:
                    if helpbox.get(key) and helpbox.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    helpbox[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in helpbox.values()]:
            continue
        elif len(helpbox) == len(boxes):
            break
        else:
            return False

    return len(helpbox) == len(boxes)


if __name__ == '__main__':
    """
    Entry
    """
    canUnlockAll([[]])
