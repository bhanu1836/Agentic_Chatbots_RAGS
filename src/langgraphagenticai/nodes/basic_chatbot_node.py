from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    BasicChatbotNode is a simple chatbot node that can be used to interact with users.
    """
    def __init__(self, model):
        self.llm = model

    def process(self,state:State)-> dict:
        """
        Process the state and return a response.
        """
        return {"messages":self.llm.invoke(state["messages"])}
