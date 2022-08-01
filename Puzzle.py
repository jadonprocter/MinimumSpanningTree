def solve_puzzle(Board, Source, Destination, moves=[], path=[]):
    path.append(Source)

    if Source == Destination:
        return len(path)

    left = (Source[0], Source[1] - 1) if Source[1] - 1 >= 0 and Board[
        Source[0]][Source[1] - 1] is '-' else None

    right = (Source[0], Source[1] + 1) if Source[1] + 1 < len(Board[Source[0]]) and Board[
        Source[0]][Source[1] + 1] is '-' else None

    up = (Source[0] - 1, Source[1]) if Source[0] - 1 >= 0 and Board[Source[0] - 1][Source[1]] is '-' else None

    down = (Source[0] + 1, Source[1]) if Source[0] + 1 < len(Board[Source[0]]) and Board[Source[0] + 1][Source[1]] is '-' else None

    for i in [left, right, up, down]:
        if i is not None:
            moves.append(i)

    if len(moves) == 0:
        return float("inf")

    results = [solve_puzzle(Board, move, Destination, [], path) for move in moves]
    return min(results)


if __name__ == "__main__":
    Puzzle = [['-', '-', '-', '-', '-'],
              ['-', '-', '#', '-', '-'],
              ['-', '-', '-', '-', '-'],
              ['#', '-', '#', '#', '-'],
              ['-', '#', '-', '-', '-']]

    print(solve_puzzle(Puzzle, (0, 4), (3, 4)))
