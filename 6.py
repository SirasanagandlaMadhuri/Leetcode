ZIGZAG CONVERSION 
class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s
        rows = [''] * num_rows
        current_row = 0
        going_down = False
        for char in s:
            rows[current_row] += char
            if current_row == 0:
                going_down = True
            elif current_row == num_rows - 1:
                going_down = False
            current_row += 1 if going_down else -1
        return ''.join(rows)
