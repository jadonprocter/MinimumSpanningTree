def get_moves(Board, Source, path):
    moves = []
    left = (Source[0], Source[1] - 1) if Source[1] - 1 >= 0 and Board[
        Source[0]][Source[1] - 1] == '-' and (Source[0], Source[1] - 1) not in path else None

    right = (Source[0], Source[1] + 1) if Source[1] + 1 < len(Board[Source[0]]) and Board[
        Source[0]][Source[1] + 1] == '-' and (Source[0], Source[1] + 1) not in path else None

    up = (Source[0] - 1, Source[1]) if Source[0] - 1 >= 0 and Board[Source[0] - 1][Source[1]] == '-' and (
        Source[0] - 1, Source[1]) not in path else None

    down = (Source[0] + 1, Source[1]) if Source[0] + 1 < len(Board[Source[0]]) and Board[Source[0] + 1][
        Source[1]] == '-' and (Source[0] + 1, Source[1]) not in path else None

    for i in [left, right, up, down]:
        if i is not None:
            moves.append(i)

    return moves


def solve_puzzle(Board, Source, Destination):
    path = []
    while Source != Destination:
        path.append(Source)

        moves = get_moves(Board, Source, path)

        if len(moves) == 0:
            return None

        results = [(move[0] - Destination[0]) + (move[1] - Destination[1]) for move in moves]

        Source = moves[results.index(max(results))]

    path.append(Destination)
    return path


if __name__ == "__main__":
    Puzzle = [['-', '-', '-', '-', '-'],
              ['-', '-', '#', '-', '-'],
              ['-', '-', '-', '-', '-'],  # changed 4
              ['#', '-', '#', '#', '-'],
              ['-', '#', '-', '-', '-']]  # changed 1

    print(solve_puzzle(Puzzle, (0, 4), (3, 4)))

    print(solve_puzzle(Puzzle, (0, 2), (2, 2)))
    print(solve_puzzle(Puzzle, (0, 0), (4, 4)))
    print(solve_puzzle(Puzzle, (0, 0), (4, 0)))
