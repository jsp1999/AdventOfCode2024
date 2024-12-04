puzzle_input = []
xmas_pattern = ['X', 'M', 'A', 'S']
xmas_backwards = ['S', 'A', 'M', 'X']
mas_pattern = ['M', 'A', 'S']
mas_backwards = ['S', 'A', 'M']

with open('data.txt', 'r') as file:
    for line in file:
        puzzle_line = [char for char in line.strip()]
        puzzle_input.append(puzzle_line)

def count_XMAS():
    def is_match(segment):
        """Check if a segment matches the pattern or its reverse."""
        return segment == xmas_pattern or segment == xmas_backwards

    count = 0
    rows = len(puzzle_input)
    cols = len(puzzle_input[0])

    for i in range(rows):
        for j in range(cols):
            # Check horizontal (rightwards)
            if j <= cols - 4 and is_match(puzzle_input[i][j:j + 4]):
                count += 1
            
            # Check vertical (downwards)
            if i <= rows - 4:
                vertical_segment = [puzzle_input[i + k][j] for k in range(4)]
                if is_match(vertical_segment):
                    count += 1
            
            # Check diagonal (down-right)
            if i <= rows - 4 and j <= cols - 4:
                diagonal_segment = [puzzle_input[i + k][j + k] for k in range(4)]
                if is_match(diagonal_segment):
                    count += 1
            
            # Check anti-diagonal (up-right)
            if i >= 3 and j <= cols - 4:
                anti_diagonal_segment = [puzzle_input[i - k][j + k] for k in range(4)]
                if is_match(anti_diagonal_segment):
                    count += 1

    return count

def count_MAS():
    def is_match(segment):
        """Check if a segment matches the pattern or its reverse."""
        return segment == mas_pattern or segment == mas_backwards

    count = 0
    rows = len(puzzle_input)
    cols = len(puzzle_input[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            diagonal_segment = [puzzle_input[i + k - 1][j + k - 1] for k in range(3)]
            anti_diagonal_segment = [puzzle_input[i - k + 1][j + k - 1] for k in range(3)]

            if is_match(diagonal_segment) and is_match(anti_diagonal_segment):
                count += 1

    return count

print(count_MAS())
