from enum import Enum
import keyboard

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4

'''
    * Crea un programa capaz de gestionar una pieza de Tetris.
    * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
    * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
    *   🔳
    *   🔳🔳🔳
    * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
    *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
    *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
    *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
    *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
    *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
    *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
    *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
    *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
    *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
    *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
    * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
    *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en
    *   la pantalla de juego.
    * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
    * - Debes tener en cuenta los límites de la pantalla de juego.
'''

screen = [  ["🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔳","🔳","🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
            ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"]
            ]

def tetris(screen: list):
    print_screen(screen)

    rotation = 0

    while (True):

        event = keyboard.read_event()
        
        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            if event.name == "down":
                      (screen, rotation) = move_piece(screen, Movement.DOWN, rotation)
            elif event.name == "right":
                (screen, rotation) = move_piece(screen, Movement.RIGHT, rotation)
            elif event.name == "left":
                (screen, rotation) = move_piece(screen, Movement.LEFT, rotation)
            elif event.name == "space":
                (screen, rotation) = move_piece(screen, Movement.ROTATE, rotation)



def move_piece(screen: list, movement: Movement, rotation: int) -> (list, int):

    new_screen = [["🔲"] * 10  for _ in range(10)]

    rotation_item = 0
    rotations = [[(1, 1), (0, 0), (-2, 0), (-1, -1)],
                 [(0, 1), (-1, 0), (0, -1), (1, -2)],
                 [(0, 2), (1, 1), (-1, 1), (-2, 0)],
                 [(0, 1), (1, 0), (2, -1), (1, -2)]]
    
    new_rotation = rotation
    if movement is Movement.ROTATE:
        new_rotation = 0 if rotation == 3 else rotation + 1

    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):

            if item == "🔳":

                new_row_index = 0
                new_column_index = 0

                match movement:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                    case Movement.ROTATE:
                        new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                        new_column_index = column_index + rotations[new_rotation][rotation_item][1]
                        rotation_item += 1

                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0:
                    print("\nNo se puede realizar el movimiento\n")
                    new_screen = screen
                    new_rotation = rotation
                else:
                    new_screen[new_row_index][new_column_index] = "🔳"
                
    print_screen(new_screen)

    return new_screen,new_rotation

def print_screen(screen: list):
    print("\n    Pantalla TETRIS\n")
    for row in screen:
        print("".join(map(str,row)))



## *************************************************************************** ##
## *************************************************************************** ##
## *************************************************************************** ##

tetris(screen)