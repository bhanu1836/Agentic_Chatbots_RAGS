from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from langgraph.graph import START,END

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph with the provided LLM.
        """
        self.graph_builder.add_node("chatbot","")
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)