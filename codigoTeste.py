from unittest import mock

from pip._internal import operations


@mock.patch('io')
def test_get_boolean_response(self, mock_io):
    #setup
    mock_io.prompt.return_value = ['x','y']
    result = operations.get_boolean_response()

    #test
    self.assertTrue(result)
    self.assertEqual(mock_io.prompt.call_count, 2)

