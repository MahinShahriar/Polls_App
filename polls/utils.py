from matplotlib import pyplot as plt
from io import BytesIO
import base64

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('Results of the poll :')
    plt.plot(x, y)
    plt.xticks(rotation=60)
    plt.xlabel('question_text')
    plt.ylabel('votes')
    plt.tight_layout()
    graph = get_graph()
    return graph