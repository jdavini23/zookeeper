num_of_halls = int(input())
capacity = int(input())
number_of_viewers = int(input())

if num_of_halls * capacity >= number_of_viewers:
    print(True)
else:
    print(False)
