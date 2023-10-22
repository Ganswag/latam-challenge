from unittest import TestCase

from src.modules.helpers import insert_sorted, get_max_value


class TestInsertSorted(TestCase):

    def test_insert_sorted_initial(self):
        INITIAL_TEST_VALUE = []
        NEW_DATA = ('a', 1)
        EXPECTED_RESULT = [('a', 1)]

        test_value = INITIAL_TEST_VALUE.copy()
        insert_sorted(test_value, NEW_DATA, 0)
        self.assertEqual(test_value, EXPECTED_RESULT)

        test_value = INITIAL_TEST_VALUE.copy()
        insert_sorted(test_value, NEW_DATA, 1)
        self.assertEqual(test_value, EXPECTED_RESULT)

        test_value = INITIAL_TEST_VALUE.copy()
        self.assertRaises(IndexError, insert_sorted, test_value, NEW_DATA, 2)

    def test_insert_sorted_begin(self):
        INITIAL_TEST_VALUE = [('c', 3),  ('b', 2), ('a', 1)]
        NEW_DATA = ('d', 4)
        EXPECTED_RESULT = [('d', 4),('c', 3),  ('b', 2), ('a', 1)]

        test_value = INITIAL_TEST_VALUE.copy()
        insert_sorted(test_value, NEW_DATA, 0)
        self.assertEqual(test_value, EXPECTED_RESULT)

        test_value = INITIAL_TEST_VALUE.copy()
        insert_sorted(test_value, NEW_DATA, 1)
        self.assertEqual(test_value, EXPECTED_RESULT)

        test_value = INITIAL_TEST_VALUE.copy()
        self.assertRaises(IndexError, insert_sorted, test_value, NEW_DATA, 2)


    def test_insert_sorted_normal(self):
        INITIAL_TEST_VALUE = [('d', 4), ('b', 2), ('a', 1)]
        NEW_DATA = ('c', 3)
        EXPECTED_RESULT = [('d', 4), ('c', 3), ('b', 2), ('a', 1)]

        test_value = INITIAL_TEST_VALUE.copy()
        insert_sorted(test_value, NEW_DATA, 0)
        self.assertEqual(test_value, EXPECTED_RESULT)

        test_value = INITIAL_TEST_VALUE.copy()
        insert_sorted(test_value, NEW_DATA, 1)
        self.assertEqual(test_value, EXPECTED_RESULT)

        test_value = INITIAL_TEST_VALUE.copy()
        self.assertRaises(IndexError, insert_sorted, test_value, NEW_DATA, 2)


    def test_insert_sorted_end(self):
        INITIAL_TEST_VALUE = [('d', 4), ('c', 3), ('b', 2)]
        NEW_DATA = ('a', 1)
        EXPECTED_RESULT = [('d', 4),('c', 3),  ('b', 2), ('a', 1)]

        test_value = INITIAL_TEST_VALUE.copy()
        insert_sorted(test_value, NEW_DATA, 0)
        self.assertEqual(test_value, EXPECTED_RESULT)

        test_value = INITIAL_TEST_VALUE.copy()
        insert_sorted(test_value, NEW_DATA, 1)
        self.assertEqual(test_value, EXPECTED_RESULT)

        test_value = INITIAL_TEST_VALUE.copy()
        self.assertRaises(IndexError, insert_sorted, test_value, NEW_DATA, 2)


class TestGetMaxValue(TestCase):

    def test_get_max(self):
        TEST_OBJECT = {
            'min': 1,
            'dummy': 2,
            'max': 3
        }
        EXPECTED_RESULT = ('max', 3)
        result = get_max_value(TEST_OBJECT)

        self.assertEqual(result, EXPECTED_RESULT)

    def test_get_duplicated(self):
        TEST_OBJECT = {
            'min': 1,
            'dummy': 2,
            'max': 2
        }
        EXPECTED_RESULT = ('dummy', 2)
        result = get_max_value(TEST_OBJECT)

        self.assertEqual(result, EXPECTED_RESULT)
