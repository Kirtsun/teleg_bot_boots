
data = {'24.5': 39, '25': 40, '25.5': 40, '26': 41, '26.5': 42, '27': 42,
        '27.5': 43, '28': 44, '28.5': 44, '29': 45, '29.5': 46, '30': 46,
        '30.5': 47, '31': 48, '31.5': 48}


async def check_right_sm(sm: str, size: int):
    for key, value in data.items():
        if key == str(sm) and value == int(size):
            return True
    return False
