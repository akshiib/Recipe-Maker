import unittest
from unittest.mock import patch, MagicMock, mock_open
import recipe_maker


class TestRecipeMaker(unittest.TestCase):
    @patch('recipe_maker.input', create=True)
    def test_input_ingredients(self, mocked_input):
        mocked_input.side_effect = ["3", "salmon", "lemon", "dill"]
        result = recipe_maker.input_ingredients()
        self.assertEqual(result, "salmon,lemon,dill")
        print("Passed Ingredient Input Test")


if __name__ == '__main__':
    unittest.main()
