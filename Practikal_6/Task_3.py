# Все равны, как на подбор.

def same_by(charcteristic, object):
    count = 0
    for element in object:
        if charcteristic(element) == 0:
            count += 1
    return len(object) == count

values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")