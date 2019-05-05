import unittest

from dooble.idl import Idl


class TestIdl(unittest.TestCase):

    def test_empty_observable(self):
        text = '----->'

        expected_result = [
            {'obs': [
                [],
                [ 
                    {'ts': '-'},
                    {'ts': '-'},
                    {'ts': '-'},
                    {'ts': '-'},
                    {'ts': '-'},
                ],
                '>'
            ]}
        ]

        idl = Idl()
        ast = idl.parse(text)
        self.assertEqual(expected_result, ast)

    def test_observable_items(self):
        text = '-a-b-c-->'

        expected_result = [
            {'obs': [
                [], 
                [ 
                    {'ts': '-'},
                    {'item': 'a'},
                    {'ts': '-'},
                    {'item': 'b'},
                    {'ts': '-'},
                    {'item': 'c'},
                    {'ts': '-'},
                    {'ts': '-'},
                ],
                '>'
            ]}
        ]

        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_observable_skipspan(self):
        text = '  -a-b-c-->'

        expected_result = [
            {'obs': [
                [' ', ' '],
                [ 
                    {'ts': '-'},
                    {'item': 'a'},
                    {'ts': '-'},
                    {'item': 'b'},
                    {'ts': '-'},
                    {'item': 'c'},
                    {'ts': '-'},
                    {'ts': '-'},
                ],
                '>'
            ]}
        ]

        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_observable_completed(self):
        text = '-a-b-c--|'

        expected_result = [
            {'obs': [
                [],
                [ 
                    {'ts': '-'},
                    {'item': 'a'},
                    {'ts': '-'},
                    {'item': 'b'},
                    {'ts': '-'},
                    {'item': 'c'},
                    {'ts': '-'},
                    {'ts': '-'},
                ],
                '|'
            ]}
        ]

        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_observable_error(self):
        text = '-a-b-c--*'

        expected_result = [
            {'obs': [
                [],
                [ 
                    {'ts': '-'},
                    {'item': 'a'},
                    {'ts': '-'},
                    {'item': 'b'},
                    {'ts': '-'},
                    {'item': 'c'},
                    {'ts': '-'},
                    {'ts': '-'},
                ],
                '*'
            ]}
        ]

        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_multiple_observables(self):
        text = '''-a-b->
-1-2->
'''

        expected_result = [
            {'obs': [
                [],
                [ 
                    {'ts': '-'},
                    {'item': 'a'},
                    {'ts': '-'},
                    {'item': 'b'},
                    {'ts': '-'},
                ],
                '>'
            ]},
            {'obs': [
                [],
                [ 
                    {'ts': '-'},
                    {'item': '1'},
                    {'ts': '-'},
                    {'item': '2'},
                    {'ts': '-'},
                ],
                '>'
            ]}
        ]

        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_operator(self):
        text = '[ map(i: i*2) ]'

        expected_result = [{'op': [
            '[',
            ' map(i: i*2) ',
            ']'
            ]}
        ]

        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_higer_order_observable(self):
        text = '-+->'

        expected_result = [
            {'obs': [
                [],
                [
                    {'ts': '-'},
                    {'item': '+'},
                    {'ts': '-'},
                ],
                '>'
            ]}
        ]

        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_child_observable(self):
        text = '+-a->'

        expected_result = [
            {'obs': [
                [], '+',
                [
                    {'ts': '-'},
                    {'item': 'a'},
                    {'ts': '-'},
                ],
                '>'
            ]}
        ]

        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)
