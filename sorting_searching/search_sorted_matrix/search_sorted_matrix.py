# Problem: Search a sorted matrix for an item.
from typing import List, Tuple, Optional


def search_sorted_matrix(matrix: List[List[int]], item: int) -> Optional[Tuple[int, int]]:
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == item:
            return row, col
        elif matrix[row][col] > item:
            col -= 1
        else:
            row += 1
    return None
