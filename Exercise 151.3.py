import copy

def move_rectangle(rect, dx, dy):
    rect2 = copy.deepcopy(rect)
    rect2.cornor.x = rect.cornor.x + dx
    rect2.cornor.y = rect.cornor.y + dy
    return rect2