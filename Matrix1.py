import sys

def chess_knight_path(start, end):
    def chess_to_coords(chess):
        return ord(chess[0]) - ord('A'), int(chess[1:]) - 1

    def coords_to_chess(coords):
        return chr(coords[0] + ord('A')) + str(coords[1] + 1)

    def valid_move(coords):
        x, y = coords
        return 0 <= x < 26 and 0 <= y < 26

    def knight_moves(coords):
        x, y = coords
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        return [(x + dx, y + dy) for dx, dy in moves]

    start_coords = chess_to_coords(start)
    end_coords = chess_to_coords(end)
    visited = {start_coords}
    queue = [[start_coords]]

    while queue:
        path = queue.pop(0)
        current_coords = path[-1]

        if current_coords == end_coords:
            return [coords_to_chess(coords) for coords in path]

        for move in knight_moves(current_coords):
            if valid_move(move) and move not in visited:
                new_path = list(path)
                new_path.append(move)
                queue.append(new_path)
                visited.add(move)

    return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your-solution.py <start_coordinate> <end_coordinate>")
    else:
        start_coord = sys.argv[1]
        end_coord = sys.argv[2]
        result = chess_knight_path(start_coord, end_coord)
        print(result)