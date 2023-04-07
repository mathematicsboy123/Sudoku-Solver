board = [[0, 0, 0, 0, 2, 9, 0, 0, 1],
         [0, 5, 6, 3, 0, 7, 0, 0, 2],
         [0, 0, 9, 0, 0, 0, 3, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 8, 3],
         [0, 0, 1, 0, 0, 0, 4, 0, 0],
         [7, 9, 0, 4, 0, 0, 0, 0, 0],
         [0, 0, 7, 0, 0, 0, 6, 0, 0],
         [4, 0, 0, 8, 0, 5, 1, 9, 0],
         [5, 0, 0, 9, 7, 0, 0, 0, 0]]


def get_boxes(bo):
    list1 = [bo[0], bo[1], bo[2]]
    list2 = [bo[3], bo[4], bo[5]]
    list3 = [bo[6], bo[7], bo[8]]
    box1, box2, box3, box4, box5, box6, box7, box8, box9 = [], [], [], [], [], [], [], [], []
    count = 1
    for thing in list1:
        count = 1
        for item in thing:
            if count <= 3:
                box1.append(item)
                count += 1
            elif 3 < count <= 6:
                box2.append(item)
                count += 1
            else:
                box3.append(item)
                count += 1
    count = 1
    for thing in list2:
        count = 1
        for item in thing:
            if count <= 3:
                box4.append(item)
                count += 1
            elif 3 < count <= 6:
                box5.append(item)
                count += 1
            else:
                box6.append(item)
                count += 1
    count = 1
    for thing in list3:
        count = 1
        for item in thing:
            if count <= 3:
                box7.append(item)
                count += 1
            elif 3 < count <= 6:
                box8.append(item)
                count += 1
            else:
                box9.append(item)
                count += 1
    return [box1, box2, box3, box4, box5, box6, box7, box8, box9]


def valid(bo, pos, num):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num:
            return False

    # Check box
    boxes = get_boxes(bo)
    for every_list in boxes:
        for item in every_list:
            if every_list.count(item) != 1 and item != 0:
                return False

    return True


def blank(bo):
    for i in range(len(bo)):
        for k in range(len(bo[0])):
            if bo[i][k] == 0:
                return (i, k)


def solve(bo):
    find = blank(bo)
    if not find:
        return True
    else:
        x, y = find
    for i in range(1, 10):
        if valid(bo, (x, y), i):
            bo[x][y] = i

            if solve(bo):
                return bo
            
            bo[x][y] = 0
        else:
            continue

    return False


def board_valid(bo):
    #Check rows
    for row in bo:
        for i in range(1, 10):
            if row.count(i) > 1:
                return False
            else:
                continue
    #Check columns
    for i in range(0, 9):
        new_list= []
        for k in range(0, 9):
            new_list.append(bo[k][i])
        for l in range(1, 10):
            if new_list.count(l) > 1:
                return False
            else:
                continue
    #Check boxes
    boxes = get_boxes(bo)
    for every_list in boxes:
        for item in every_list:
            if every_list.count(item) != 1 and item != 0:
                return False

    return True


def print_board(board):
    print("------------------------------")
    for item in board:
        print(f"{item[0]}, {item[1]}, {item[2]}  | {item[3]}, {item[4]}, {item[5]}  | {item[6]}, {item[7]}, {item[8]}")
        print("------------------------------")
    print("\n")


if __name__ == "__main__":
    print_board(solve(board))
