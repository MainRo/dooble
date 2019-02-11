import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from dooble.marble import Operator, Observable

area = np.pi*80
end_area = np.pi*50


def render_to_file(marble, filename):
    fig, ax = plt.subplots()

    layer_index = 0
    for layer in reversed(marble.layers):

        if type(layer) is Observable:
            observable = layer
            # time line
            ax.plot([observable.start, observable.end], [layer_index, layer_index], color='tab:blue', linestyle=':')

            # end marker
            if observable.completed is not None:
                ax.scatter([observable.completed], [layer_index], s=end_area, color='tab:blue', marker='|')
            elif observable.error is not None:
                ax.scatter([observable.error], [layer_index], s=end_area, color='tab:blue', marker='x')
            else:
                ax.scatter([observable.end], [layer_index], s=end_area, color='tab:blue', marker='>')

            # items
            x = []
            y = []
            for item in observable.items:
                x.append(item.at)
                y.append(layer_index)
            ax.scatter(x, y, s=area, c=None, edgecolors='navy', color='tab:blue', alpha=1.0)

            # items text
            for item in observable.items:
                ax.text(item.at, layer_index, str(item.item), horizontalalignment='center', verticalalignment='center')

        elif type(layer) is Operator:
            operator = layer
            y = layer_index - 0.1
            #ax.plot([operator.start, operator.end], [layer_index, layer_index], color='tab:blue', linestyle=':')
            ax.add_patch(Rectangle((operator.start, y), operator.end-operator.start, 0.2, alpha=1, edgecolor='black', facecolor='none'))
            #ax.add_patch(Rectangle((operator.start, layer_index), operator.end, layer_index+0.2, alpha=1, edgecolor='black', facecolor='none'))
            ax.text(operator.start+ (operator.end-operator.start)/2, y + 0.1, operator.text, horizontalalignment='center', verticalalignment='center')
            #ax.text(2.5, y, 'Operator', horizontalalignment='center', verticalalignment='center')

        layer_index += 1

    ax.set_axis_off()
    plt.savefig(filename)
