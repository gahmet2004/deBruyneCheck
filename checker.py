# solution-445
# N = 3, K = 3, S = (0, 1, 2)
def checkIsDeBruyne(deBruyne: str):
    _list = list()
    for _id in range(0, len(deBruyne) - 2):
        _insert = f"{deBruyne[_id]}{deBruyne[_id + 1]}{deBruyne[_id + 2]}"
        if (_insert in _list):
            print(_insert + " is doubling")
            return False
        _list.append(_insert)
    return True

print(checkIsDeBruyne("01201000111020021121220222101")) # True