import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_2(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_3(self):
        num_cols = 100
        num_rows = 200
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_start_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertTrue(
            (m1._cells[0][0].has_left_wall or m1._cells[0][0].has_top_wall)
            and not (m1._cells[0][0].has_left_wall and m1._cells[0][0].has_top_wall)
        )
        self.assertTrue(
            (m1._cells[num_cols-1][num_rows-1].has_right_wall or m1._cells[num_cols-1][num_rows-1].has_bottom_wall)
            and not (m1._cells[num_cols-1][num_rows-1].has_right_wall and m1._cells[num_cols-1][num_rows-1].has_bottom_wall)
        )


if __name__ == "__main__":
    unittest.main()