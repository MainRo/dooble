import unittest
from dooble.marble import Observable, Operator, Marble, Link



class TestMarble(unittest.TestCase):
    def test_higher_order_link(self):
        marble = Marble()

        # operator
        op = Operator(0, 5, "map(i: i*2)")
        marble.add_operator(op)

        # higher order observable
        obs = Observable(0)
        obs.on_observable_at(1)
        obs.on_completed_at(4)
        marble.add_observable(obs)

        # child observable
        obs = Observable(1, is_child=True)
        obs.on_next_at(1, 3)
        obs.on_completed_at(4)
        marble.add_observable(obs)

        marble.build()

        self.assertEqual(1, len(marble.higher_order_links))
        self.assertEqual(Link(1, 1, 1, 2), marble.higher_order_links[0])
