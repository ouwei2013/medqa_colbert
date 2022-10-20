import random
import gradio as gr
from colbert.data import Queries
from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Searcher


# def init():
searcher = None
with Run().context(RunConfig(nranks=1, experiment="medqa")):
    config = ColBERTConfig(
        root="./experiments",
    )
    searcher = Searcher(index="medqa_idx", config=config)
    

        
def search(query):
    results = searcher.search(query, k=5)
    responses=[]
    # idx = 0 
    for passage_id, _, _ in zip(*results):
          responses.append(searcher.collection[passage_id])
        #   idx = idx+1
    return responses





def chat(question):
    # history = history or []
    # message = message.lower()

    # if message.startswith("how many"):
    #     response = random.randint(1, 10)
    # elif message.startswith("how"):
    #     response = random.choice(["Great", "Good", "Okay", "Bad"])
    # elif message.startswith("where"):
    #     response = random.choice(["Here", "There", "Somewhere"])
    # else:
    #     response = "I don't know"
    responses = search(question)
    # history.append((message, response))
    return responses

chatbot = gr.Chatbot().style(color_map=("green", "pink"))
demo = gr.Interface(
    chat,
    inputs=gr.Textbox(lines=2, placeholder="输入你的问题"),
    outputs =["text", "text","text","text","text"]
)
if __name__ == "__main__":
    demo.launch(share=True)
