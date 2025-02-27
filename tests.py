import unittest
from maze import Maze
from sys import setrecursionlimit

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
        setrecursionlimit(3000)
        num_cols = 50
        num_rows = 50
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        setrecursionlimit(1000)
    
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
    
    def test_maze_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        found_visited = False
        count = 0
        for i in m1._cells:
            for j in i:
                count += 1
                if j.visited == True:
                    found_visited = True
        self.assertEqual(count, num_cols*num_rows)
        self.assertFalse(found_visited)
    
    def test_maze_reset_visited_2(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        m1._cells[5][3].visited = True
        m1._reset_visited_cells()
        found_visited = False
        for i in m1._cells:
            for j in i:
                if j.visited == True:
                    found_visited = True
        self.assertFalse(found_visited)


if __name__ == "__main__":
    unittest.main()