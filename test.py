from dooble.marble import Observable, Operator, Marble
from dooble.render import render_to_file
marble = Marble()

# continuing observable
obs = Observable(0, 5)
obs.on_next_at('a', 0)
obs.on_next_at('b', 1)
obs.on_next_at('c', 3)
marble.add_observable(obs)

# completed observable
obs = Observable(1, 6)
obs.on_next_at(1, 1)
obs.on_next_at(2, 5)
obs.on_completed_at(6)
marble.add_observable(obs)

# error observable
obs = Observable(0, 4)
obs.on_next_at(1, 0)
obs.on_next_at(21, 1)
obs.on_error_at(4)
marble.add_observable(obs)

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
render_to_file(marble, '/tmp/marble.png')
