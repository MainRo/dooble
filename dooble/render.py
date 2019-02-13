import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from dooble.marble import Operator, Observable, Item

area = np.pi*80
end_area = np.pi*50


def render_to_file(marble, filename):
    fig, ax = plt.subplots()

    def plt_y(y):
        return len(marble.layers) - y - 1

    # higher observable links
    for link in marble.higher_order_links:
        ax.plot(
            [link.from_x, link.to_x],
            [plt_y(link.from_y), plt_y(link.to_y)],
            color='tab:blue', linestyle='-')

    for layer_index, layer in enumerate(marble.layers):
        if type(layer) is Observable:
            observable = layer
            # time line
            ax.plot(
                [observable.start, observable.end],
                [plt_y(layer_index), plt_y(layer_index)],
                color='tab:blue', linestyle='-')


            # end marker
            if observable.completed is not None:
                ax.scatter(
                    [observable.completed], [plt_y(layer_index)],
                    s=end_area, color='tab:blue', marker='|')
            elif observable.error is not None:
                ax.scatter(
                    [observable.error], [plt_y(layer_index)], 
                    s=end_area, color='tab:blue', marker='x')
            else:
                ax.scatter(
                    [observable.end], [plt_y(layer_index)],
                    s=end_area, color='tab:blue', marker='>')

            # items
            x = []
            y = []
            for item in observable.items:
                x.append(item.at)
                y.append(plt_y(layer_index))
            ax.scatter(x, y, s=area, c=None, edgecolors='navy', color='tab:blue', alpha=1.0)

            # items text
            for item in observable.items:
                text = str(item.item) if type(item) is Item else ''
                ax.text(item.at, plt_y(layer_index), text, horizontalalignment='center', verticalalignment='center')

        elif type(layer) is Operator:
            operator = layer
            y = plt_y(layer_index) - 0.1
            ax.add_patch(Rectangle((operator.start, y), operator.end-operator.start, 0.3, alpha=1, edgecolor='black', facecolor='none'))
            ax.text(operator.start+ (operator.end-operator.start)/2, y + 0.1, operator.text, horizontalalignment='center', verticalalignment='center')

    ax.set_axis_off()
    plt.savefig(filename)
