from collections import namedtuple

Item = namedtuple('Item', ['item', 'at'])
ObsItem = namedtuple('ObsItem', ['at'])
Link = namedtuple('Link', ['from_x', 'from_y', 'to_x', 'to_y'])


class Observable(object):
    def __init__(self, start, is_child=False):
        self.label = None
        self.start = start
        self.end = start
        self.is_child = is_child
        self.items = []
        self.completed = None
        self.error = None

    def set_label(self, label):
        self.label = label

    def on_next_at(self, item, at):
        self.items.append(Item(item, at))

    def on_observable_at(self, at):
        self.items.append(ObsItem(at))

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
        self.higher_order_links = []
        self.item_links = []
        self.label_links = []
        return

    def add_observable(self, observable):
        self.layers.append(observable)

    def add_operator(self, operator):
        self.layers.append(operator)

    def _compute_higher_order_links(self):
        def nearest_links(parents, children):
            links = []
            for parent in parents:
                dist = None
                nearest = None
                for child in children:
                    d = abs(parent[0] - child[0])
                    if nearest is None or d < dist:
                        dist = d
                        nearest = child

                if nearest is not None:
                    links.append(Link(
                        from_x=parent[0], from_y=parent[1],
                        to_x=nearest[0], to_y=nearest[1],
                    ))

            return links

        children = []
        parents = []
        links = []
        for layer_index, layer in enumerate(self.layers):
            if type(layer) is Operator:
                links.extend(nearest_links(parents, children))
                children.clear()
                parents.clear()
            elif type(layer) is Observable:
                if layer.is_child is True:
                    children.append((layer.start, layer_index))
                else:
                    for item in layer.items:
                        if type(item) is ObsItem:
                            parents.append((item.at, layer_index))

        links.extend(nearest_links(parents, children))
        return links

    @staticmethod
    def _append_links(links, top_layer, bottom_layer, items):
        for item in items:
            if top_layer is not None:
                links.append(Link(
                    from_x=item[0], from_y=top_layer,
                    to_x=item[0], to_y=item[1],
                ))
            if bottom_layer is not None:
                links.append(Link(
                    from_x=item[0], from_y=item[1],
                    to_x=item[0], to_y=bottom_layer,
                ))
        return links

    def _compute_item_links(self):
        top_layer = None
        items = []
        links = []
        for layer_index, layer in enumerate(self.layers):
            if type(layer) is Operator:
                Marble._append_links(links, top_layer, layer_index, items)
                items.clear()
                top_layer = layer_index
            elif type(layer) is Observable:
                if layer.label is None:
                    for item in layer.items:
                        items.append((item.at, layer_index))

        Marble._append_links(links, top_layer, None, items)
        return links

    def _compute_label_links(self):
        top_layer = None
        items = []
        links = []
        for layer_index, layer in enumerate(self.layers):
            if type(layer) is Operator:
                Marble._append_links(links, top_layer, layer_index, items)
                items.clear()
                top_layer = layer_index
            elif type(layer) is Observable:
                if layer.label is not None:
                    items.append((layer.start, layer_index))

        Marble._append_links(links, top_layer, None, items)
        return links

    def build(self):
        self.higher_order_links = self._compute_higher_order_links()
        self.item_links = self._compute_item_links()
        self.label_links = self._compute_label_links()
