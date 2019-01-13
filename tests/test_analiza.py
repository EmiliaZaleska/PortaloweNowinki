import unittest
from datetime import date

from unittest.mock import Mock, patch

from analiza import parse_csv, get_new_tags


sample_data_dict = {
    "Robert Lewandowski":
        {
            date.fromisoformat('2019-01-12'):
                {
                    "pudelek": 1
                }
        }
}


class TestAnaliza(unittest.TestCase):
    def test_parse_csv(self):
        data_dict = parse_csv('test_data.csv')
        self.assertEqual(
            data_dict["Dżoana Krupa"][date(2019, 1, 13)]['pudelek'],
            1
        )

    def test_parse_csv_adds_correctly(self):
        data_dict = parse_csv('test_data2.csv')
        self.assertEqual(
            data_dict["Dżoana Krupa"][date(2019, 1, 13)]['pudelek'],
            2
        )

    @patch('analiza.date')
    @patch('analiza.parse_csv', Mock(return_value=sample_data_dict))
    def test_get_new_tags(self, date_mock):
        date_mock.today = Mock(return_value=date(2019, 1, 12))
        self.assertListEqual(get_new_tags('pudelek'), ['Robert Lewandowski'])

    @patch('analiza.date')
    @patch('analiza.parse_csv', Mock(return_value=sample_data_dict))
    def test_get_new_tags_fail(self, date_mock):
        date_mock.today = Mock(return_value=date(2019, 1, 13))
        self.assertNotEqual(get_new_tags('pudelek'), ['Robert Lewandowski'])


if __name__ == '__main__':
    unittest.main()
