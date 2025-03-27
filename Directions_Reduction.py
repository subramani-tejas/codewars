def dir_reduc(arr):
    if not arr:
        return []

    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }

    s = []
    for direction in arr:
        if s and opposites.get(s[-1]) == direction:
            s.pop()
        else:
            s.append(direction)
    return s


def mine(arr):
    if not arr:
        return []

    s = []
    s.append(arr[0])

    for i in range(1, len(arr)):
        opp = ""
        if s:
            top = s[-1]
            if top == "NORTH":
                opp = "SOUTH"
            elif top == "SOUTH":
                opp = "NORTH"
            elif top == "EAST":
                opp = "WEST"
            elif top == "WEST":
                opp = "EAST"

            if arr[i] == opp:
                s.pop()
            else:
                s.append(arr[i])
        else:
            s.append(arr[i])
    return s
