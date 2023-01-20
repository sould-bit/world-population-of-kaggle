# %%

import matplotlib.pyplot as plt
def chart_pie(labels, values):
    fig,ax =plt.subplots()
    ax.pie(values, labels=labels )
    ax.axis("equal")
    plt.show()

