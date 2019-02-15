from collections import namedtuple
from dooble.marble import Marble, Observable, Operator


Theme = namedtuple('Theme', [
    'timeline_color',
    'emission_color',
    'item_color',
    'label_color',
    'operator_color',
    'operator_edge_color',
])

default_theme = Theme(
    timeline_color=(
        float(0x33) / 0xFF, 
        float(0x7A) / 0xFF,
        float(0xB7) / 0xFF,
    ),
    emission_color=(
        float(0xC0) / 0xFF, 
        float(0xC0) / 0xFF,
        float(0xC0) / 0xFF,
    ),
    item_color=(
        float(0xE0) / 0xFF, 
        float(0xE8) / 0xFF,
        float(0xFF) / 0xFF,
    ),
    label_color=(
        float(0xF0) / 0xFF, 
        float(0xF0) / 0xFF,
        float(0xF0) / 0xFF,
    ),
    operator_color=(
        float(0xF0) / 0xFF,
        float(0xF0) / 0xFF,
        float(0xF0) / 0xFF,
    ),
    operator_edge_color=(
        float(0x33) / 0xFF,
        float(0x7A) / 0xFF,
        float(0xB7) / 0xFF,
    ),
)


def create_observable(layer):
    part = 0
    step = len(layer[part])

    part += 1
    is_child = False
    label = None
    if layer[part] == '+':
        is_child = True
        part += 1
        step += 1
    elif type(layer[part]) is str:
        label = layer[part]
        step += 1
        part += 1

    start = step if is_child is False else step - 1
    observable = Observable(start, is_child=is_child)
    if label is not None:
        observable.set_label(label)

    for ts in layer[part]:
        if 'ts' in ts and ts['ts'] is not None:
            step += 1
        else:
            item = ts['item']
            if item == '+':
                observable.on_observable_at(step)
            else:
                observable.on_next_at(item, step)
            step += len(item)

    part += 1
    completion = layer[part]

    if completion == '|':
        observable.on_completed_at(step)
    elif completion == '*':
        observable.on_error_at(step)
    else:
        observable.on_continued_at(step)

    return observable


def create_operator(layer):
    step = 0
    start = step

    content = layer[1]
    text = content.strip()

    step += 1
    operator = Operator(start, step + len(content) , text)

    return operator


def create_marble_from_ast(ast):
    marble = Marble()

    for layer in ast:
        if 'obs' in layer and layer['obs'] is not None:
            marble.add_observable(create_observable(layer['obs']))
        elif 'op' in layer and layer['op'] is not None:
            marble.add_operator(create_operator(layer['op']))

    marble.build()
    return marble
