import unittest

from dooble.idl import Idl


class TestIdl(unittest.TestCase):
    def test_empty_observable(self):
        text = '----->'

        expected_result = [
            {'obs': [
                [],
                [ 
                    {'ts': '-', 'item': None},
                    {'ts': '-', 'item': None},
                    {'ts': '-', 'item': None},
                    {'ts': '-', 'item': None},
                    {'ts': '-', 'item': None},
                ],
                '>'
            ], 'op': None}
        ]

        idl = Idl()
        ast = idl.parse(text)
        self.assertEqual(expected_result, ast)

    def test_observable_items(self):
        text = '-a-b-c-->'

        expected_result = [
            { 'obs': [
                [], 
                [ 
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'a'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'b'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'c'},
                    {'ts': '-', 'item': None},
                    {'ts': '-', 'item': None},
                ],
                '>'
            ], 'op': None}
        ]


        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_observable_skipspan(self):
        text = '  -a-b-c-->'

        expected_result = [
            { 'obs': [
                [' ', ' '],
                [ 
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'a'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'b'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'c'},
                    {'ts': '-', 'item': None},
                    {'ts': '-', 'item': None},
                ],
                '>'
            ], 'op': None}
        ]


        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)


    def test_observable_completed(self):
        text = '-a-b-c--|'

        expected_result = [
            { 'obs' : [
                [],
                [ 
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'a'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'b'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'c'},
                    {'ts': '-', 'item': None},
                    {'ts': '-', 'item': None},
                ],
                '|'
            ], 'op': None}
        ]


        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)


    def test_observable_error(self):
        text = '-a-b-c--*'

        expected_result = [
            { 'obs': [
                [],
                [ 
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'a'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'b'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'c'},
                    {'ts': '-', 'item': None},
                    {'ts': '-', 'item': None},
                ],
                '*'
            ], 'op': None}
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
            { 'obs': [
                [],
                [ 
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'a'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'b'},
                    {'ts': '-', 'item': None},
                ],
                '>'
            ], 'op': None}, 
            { 'obs': [
                [],
                [ 
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': '1'},
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': '2'},
                    {'ts': '-', 'item': None},
                ],
                '>'
            ], 'op': None}
        ]


        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_operator(self):
        text = '[ map(i: i*2) ]'

        expected_result = [{ 'op': [
            '[',
            ' map(i: i*2) ',
            ']'
            ],
            'obs': None}
        ]


        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_higer_order_observable(self):
        text = '-+->'

        expected_result = [
            { 'obs' : [
                [],
                [
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': '+'},
                    {'ts': '-', 'item': None},
                ],
                '>'
            ], 'op': None}
        ]


        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)

    def test_child_observable(self):
        text = '+-a->'

        expected_result = [
            { 'obs' : [
                [], '+',
                [
                    {'ts': '-', 'item': None},
                    {'ts': None, 'item': 'a'},
                    {'ts': '-', 'item': None},
                ],
                '>'
            ], 'op': None}
        ]


        idl = Idl()
        ast = idl.parse(text)
        print(ast)
        self.assertEqual(expected_result, ast)