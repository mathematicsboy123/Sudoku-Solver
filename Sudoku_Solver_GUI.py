import pygame
import os
import time
from Sudoku_Solver import board_valid
from Sudoku_Solver import solve

# Demonstration
pygame.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
square = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Blank Sudoku.JPG")), (WIDTH/9, HEIGHT/9))
outline = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Selected Outline.JPG")), (WIDTH/9, HEIGHT/9))
one = pygame.transform.scale(pygame.image.load(os.path.join("assets", "One.JPG")), (70, 70))
two = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Two.JPG")), (70, 70))
three= pygame.transform.scale(pygame.image.load(os.path.join("assets", "Three.JPG")), (70, 70))
four = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Four.JPG")), (70, 70))
five = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Five.JPG")), (70, 70))
six = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Six.JPG")), (70, 70))
seven = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Seven.JPG")), (70, 70))
eight = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Eight.JPG")), (70, 70))
nine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Nine.JPG")), (70, 70))
pygame.display.set_caption("Sudoku Solver")


def main():
    clock = pygame.time.Clock()
    run = True
    run_2 = False
    FPS = 60
    initial_coords = [8.5, 8.5]
    list_of_coords = []
    list_of_squares = []
    list_of_filled_squares = []
    final_board = []
    highlighted = False


    def draw_squares():
        WIN.fill((255, 255, 255))
        for multiplier in range(81):
            sq = square
            list_of_squares.append(sq)
            WIN.blit(sq, (initial_coords[0], initial_coords[1]))
            list_of_coords.append([initial_coords[0], initial_coords[1]])
            number = ((multiplier + 1) / 9)
            if len(str(number)) == 3:
                initial_coords[0] = 8.5
                initial_coords[1] = (HEIGHT/9) * ((multiplier + 1) / 9) - 2*((multiplier + 1)/9) + 8.5
            else:
                initial_coords[0] += WIDTH/9 - 2 
        pygame.display.flip()
    

    draw_squares()


    def new_draw_squares():
            count = 0
            while count <= 80:
                WIN.blit(list_of_squares[count], (list_of_coords[count][0], list_of_coords[count][1]))
                count += 1
            pygame.display.flip()


    while run:
        clock.tick(FPS)

        new_draw_squares()

        def number_update(img, coords):
            list_of_squares[coords[0]] = img
            WIN.blit(img, (coords[1] + 7.5, coords[2] + 8))
            pygame.display.flip()

        if highlighted:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1] or keys[pygame.K_KP1]:
                def new_draw_squares():
                    number_update(one, highlighted)
                list_of_filled_squares.append([highlighted[0], one, 1])
            elif keys[pygame.K_2] or keys[pygame.K_KP2]:
                def new_draw_squares():
                    number_update(two, highlighted)
                list_of_filled_squares.append([highlighted[0], two, 2])
            elif keys[pygame.K_3] or keys[pygame.K_KP3]:
                def new_draw_squares():
                    number_update(three, highlighted)
                list_of_filled_squares.append([highlighted[0], three, 3])
            elif keys[pygame.K_4] or keys[pygame.K_KP4]:
                def new_draw_squares():
                    number_update(four, highlighted)
                list_of_filled_squares.append([highlighted[0], four, 4])
            elif keys[pygame.K_5] or keys[pygame.K_KP5]:
                def new_draw_squares():
                    number_update(five, highlighted)
                list_of_filled_squares.append([highlighted[0], five, 5])
            elif keys[pygame.K_6] or keys[pygame.K_KP6]:
                def new_draw_squares():
                    number_update(six, highlighted)
                list_of_filled_squares.append([highlighted[0], six, 6])
            elif keys[pygame.K_7] or keys[pygame.K_KP7]:
                def new_draw_squares():
                    number_update(seven, highlighted)
                list_of_filled_squares.append([highlighted[0], seven, 7])
            elif keys[pygame.K_8] or keys[pygame.K_KP8]:
                def new_draw_squares():
                    number_update(eight, highlighted)
                list_of_filled_squares.append([highlighted[0], eight, 8])
            elif keys[pygame.K_9] or keys[pygame.K_KP9]:
                def new_draw_squares():
                    number_update(nine, highlighted)
                list_of_filled_squares.append([highlighted[0], nine, 9])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    useless_list = []
                    clear_count = -1
                    new_useless_list = []
                    for item in list_of_filled_squares:
                        if [item[0], item[2]] in useless_list:
                            pass
                        else:
                            useless_list.append([item[0], item[2]])
                    
                    try:
                        while clear_count < 20:
                            cont = True
                            for item in new_useless_list:
                                if item[0] == useless_list[clear_count][0]:
                                    cont = False
                                else:
                                    continue
                            if cont:
                                new_useless_list.append(useless_list[clear_count])
                            clear_count -= 1
                    except Exception:
                        pass

                    useless_list = new_useless_list
                    for i in range(81):
                        add = True
                        for t in useless_list:
                            if i == t[0]:
                                final_board.append(t[1])
                                add = False
                            else:
                                continue
                        if add:
                            final_board.append(0)
                    run_2 = True
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    index_count = 0
                    mouse_position = pygame.mouse.get_pos()
                    for item in list_of_coords:
                        if item[0] <= mouse_position[0] <= (item[0] + WIDTH/9) and item[1] <= mouse_position[1] <= (item[1] + HEIGHT/9):
                            break
                        else:
                            index_count += 1
                    try:
                        if highlighted:
                            list_of_squares[highlighted[0]] = square
                            WIN.blit(list_of_squares[highlighted[0]], (highlighted[1], highlighted[2]))
                            pygame.display.flip()
                            try:
                                for item in list_of_filled_squares:
                                    WIN.blit(item[1], (list_of_coords[item[0]][0] + 7.5, list_of_coords[item[0]][1] + 8))
                                pygame.display.flip()
                            except Exception:
                                pass

                            def new_draw_squares():
                                count = index_count
                                for thing in list_of_filled_squares:
                                    if count == thing[0]:
                                        continue
                                    else:
                                        WIN.blit(list_of_squares[count], (list_of_coords[count][0], list_of_coords[count][1]))
                                pygame.display.flip()
                            highlighted = False
                        else:
                            list_of_squares[index_count] = outline
                            WIN.blit(list_of_squares[index_count], (list_of_coords[index_count][0], list_of_coords[index_count][1]))
                            pygame.display.flip()
                            try:
                                for item in list_of_filled_squares:
                                    WIN.blit(item[1], (list_of_coords[item[0]][0] + 7.5, list_of_coords[item[0]][1] + 8))
                                pygame.display.flip()
                            except Exception:
                                pass

                            def new_draw_squares():
                                count = index_count
                                for thing in list_of_filled_squares:
                                    if count == thing[0]:
                                        pass
                                    else:
                                        WIN.blit(list_of_squares[count], (list_of_coords[count][0], list_of_coords[count][1]))
                                pygame.display.flip()
                            highlighted = [index_count, list_of_coords[index_count][0], list_of_coords[index_count][1]]
                    except Exception:
                        pass
    while run_2:

        def draw_squares():
            WIN.fill((255, 255, 255))
            for multiplier in range(81):
                sq = square
                list_of_squares.append(sq)
                WIN.blit(sq, (initial_coords[0], initial_coords[1] - HEIGHT/9))
                list_of_coords.append([initial_coords[0], initial_coords[1]])
                number = ((multiplier + 1) / 9)
                if len(str(number)) == 3:
                    initial_coords[0] = 8.5
                    initial_coords[1] = (HEIGHT/9) * ((multiplier + 1) / 9) - 2*((multiplier + 1)/9) + 8.5
                else:
                    initial_coords[0] += WIDTH/9 - 2 
            pygame.display.flip()
    
        draw_squares()
        run_3 = True
        run_2 = False
    
    while run_3:

        clock.tick(FPS)
        counter = 1
        list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9 = [], [], [], [], [], [], [], [], []
        for item in final_board:
            if counter <= 9:
                list_1.append(item)
                counter += 1
            elif 9 < counter <= 18:
                list_2.append(item)
                counter += 1
            elif 18 < counter <= 27:
                list_3.append(item)
                counter += 1
            elif 27 < counter <= 36:
                list_4.append(item)
                counter += 1
            elif 36 < counter <= 45:
                list_5.append(item)
                counter += 1
            elif 45 < counter <= 54:
                list_6.append(item)
                counter += 1
            elif 54 < counter <= 63:
                list_7.append(item)
                counter += 1
            elif 63 < counter <= 72:
                list_8.append(item)
                counter += 1
            elif 72 < counter <= 82:
                list_9.append(item)
                counter += 1
        board = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9]

        answer = True
        if board_valid(board):
            pass
        else:
            answer = False

        if answer:
            answer = solve(board)
        else:
            pass

        if answer:
            count = 0

            def update(number, counter):
                WIN.blit(number, (list_of_coords[counter][0] + 7.5, list_of_coords[counter][1] + 8))
                pygame.display.flip()

            for item in answer:
                for thing in item:
                    if thing == 1:
                        update(one, count)
                        count += 1
                    if thing == 2:
                        update(two, count)
                        count += 1
                    if thing == 3:
                        update(three, count)
                        count += 1
                    if thing == 4:
                        update(four, count)
                        count += 1
                    if thing == 5:
                        update(five, count)
                        count += 1
                    if thing == 6:
                        update(six, count)
                        count += 1
                    if thing == 7:
                        update(seven, count)
                        count += 1
                    if thing == 8:
                        update(eight, count)
                        count += 1
                    if thing == 9:
                        update(nine, count)
                        count += 1
        else:
            text = "Invalid Sudoku ?!"
            font = pygame.font.SysFont("comicsans", 70)
            use = font.render(text, True, (255, 0, 0))
            WIN.blit(use, (WIDTH / 2 - use.get_width() / 2, 350))
            pygame.display.flip()
            time.sleep(3)
            exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__ == "__main__":
    main()
