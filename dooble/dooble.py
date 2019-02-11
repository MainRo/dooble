from dooble.marble import Marble, Observable, Operator


def create_observable(layer):
    step = 0

    observable = Observable(step)
    for ts in layer[1]:
        if 'ts' in ts and ts['ts'] is not None:
            step += 1
        else:
            item = ts['item']
            observable.on_next_at(item, step)
            step += len(item)

    completion = layer[2]

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

    return marble
