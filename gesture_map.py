# gesture_map.py

def map_gesture(fingers):
    """
    Maps detected finger list to game actions
    fingers: list of 5 ints [thumb, index, middle, ring, pinky]
    Returns: string action
    """
    if fingers == [0,0,0,0,0]:
        return "STOP"
    elif fingers == [0,1,0,0,0]:
        return "LEFT"
    elif fingers == [0,1,1,0,0]:
        return "RIGHT"
    elif fingers == [1,1,1,1,1]:
        return "START"
    else:
        return "UNKNOWN"