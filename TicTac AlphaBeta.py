import math

X = "X"
O = "O"
EMPTY = None

def ImprimirTablero(tablero):
    for fila in tablero:
        print("| ", end="")
        for celda in fila:
            if celda is None:
                print(" ", end=" | ")
            else:
                print(celda, end=" | ")
        print()
        print("-" * 13)


def Ganador(tablero):
    for fila in tablero:
        if fila.count(fila[0]) == len(fila) and fila[0] is not None:
            return fila[0]
    # Check columns
    for col in range(len(tablero)):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] is not None:
            return tablero[0][col]
    # Check diagonals
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] is not None:
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] is not None:
        return tablero[0][2]
    # No Ganador
    return None

# Returns True if the tablero is TableroLLeno
def TableroLLeno(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == EMPTY:
                return False
    return True

# Returns a list of (fila, col) tuples for empty celdas
def EspaciosVacios(tablero):
    celdas = []
    for fila in range(len(tablero)):
        for col in range(len(tablero)):
            if tablero[fila][col] == EMPTY:
                celdas.append((fila, col))
    return celdas

# Evaluars the tablero
def Evaluar(tablero):
    if Ganador(tablero) == X:
        return 1
    elif Ganador(tablero) == O:
        return -1
    else:
        return 0


# Returns the optimal move using Alpha-Beta pruning
def alphabeta(tablero, profundidad, jugador, alpha, beta):
    if Ganador(tablero) == X:
        return None, None, -1
    elif Ganador(tablero) == O:
        return None, None, 1
    elif TableroLLeno(tablero):
        return None, None, 0

    if jugador == O:
        fila_opt, col_opt, mejorPuntaje = None, None, float('-inf')
        for fila, col in EspaciosVacios(tablero):
            tablero[fila][col] = O
            _, _, score = alphabeta(tablero, profundidad - 1, X, alpha, beta)
            tablero[fila][col] = EMPTY
            if score > mejorPuntaje:
                fila_opt, col_opt, mejorPuntaje = fila, col, score
            if mejorPuntaje >= beta:
                break
            alpha = max(alpha, mejorPuntaje)
        return fila_opt, col_opt, mejorPuntaje
    else:
        fila_opt, col_opt, mejorPuntaje = None, None, float('inf')
        for fila, col in EspaciosVacios(tablero):
            tablero[fila][col] = X
            _, _, score = alphabeta(tablero, profundidad - 1, O, alpha, beta)
            tablero[fila][col] = EMPTY
            if score < mejorPuntaje:
                fila_opt, col_opt, mejorPuntaje = fila, col, score
            if mejorPuntaje <= alpha:
                break
            beta = min(beta, mejorPuntaje)
        return fila_opt, col_opt, mejorPuntaje


# Main function
# Main function
def main():
    tablero = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    print("Tic Tac Toe")
    print("------------")
    ImprimirTablero(tablero)
    while not TableroLLeno(tablero):
        fila = int(input("Ingrese la fila (0-2): "))
        col = int(input("Ingrese la columna (0-2): "))
        if tablero[fila][col] != EMPTY:
           print("Movimiento invalido, pruebe denuevo")
           continue
        tablero[fila][col] = X
        ImprimirTablero(tablero)
        if Ganador(tablero) == X:
            print("Ganaste!!!")
            return
        elif TableroLLeno(tablero):
            print("Empate")
            return
        print("Turno de la computadora")
        fila, col, score = alphabeta(tablero, 4, O, float('-inf'), float('inf'))
        tablero[fila][col] = O
        ImprimirTablero(tablero)
        if Ganador(tablero) == O:
            print("Gana la computadora")
            return
        elif TableroLLeno(tablero):
            print("Empate")
            return

    

main()