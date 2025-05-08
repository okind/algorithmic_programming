import unittest
from two_sum import two_sum_brute_force, two_sum_bst, two_sum_hashmap


class TestTwoSumMethods(unittest.TestCase):
    def setUp(self):
        self.arr = [2, 7, 11, 15]
        self.target = 9
        self.no_solution_arr = [1, 2, 3]
        self.no_solution_target = 10

    def test_hashmap(self):
        self.assertEqual(
            sorted(two_sum_hashmap(self.arr, self.target)), [2, 7])
        self.assertIsNone(two_sum_hashmap(
            self.no_solution_arr, self.no_solution_target))


if __name__ == '__main__':
    unittest.main()
