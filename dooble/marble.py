from collections import namedtuple

Item = namedtuple('Item', ['item', 'at'])


class Observable(object):
    def __init__(self, start, end = None):
        self.start = start
        self.end = end
        self.items = []
        self.completed = None
        self.error = None

    def on_next_at(self, item, at):
        self.items.append(Item(item, at))

    def on_completed_at(self, at):
        self.completed = at
        self.end = at

    def on_error_at(self, at):
        self.error = at
        self.end = at

    def on_continued_at(self, at):
        self.end = at

class Operator(object):
    def __init__(self, start, end, text):
        self.start = start
        self.end = end
        self.text = text

class Marble(object):
    def __init__(self):
        self.layers = []
        return

    def add_observable(self, observable):
        self.layers.append(observable)

    def add_operator(self, operator):
        self.layers.append(operator)
