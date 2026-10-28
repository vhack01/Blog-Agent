from ..nodes import writer, researcher, image_generator
from ..states import BlogState
from langgraph.graph import StateGraph, START, END

blog_graph = StateGraph(BlogState)

blog_graph.add_node('researcher', researcher)
blog_graph.add_node('writer', writer)
blog_graph.add_node('image_generator', image_generator)


blog_graph.add_edge(START, 'researcher')
blog_graph.add_edge('researcher', 'writer')
blog_graph.add_edge('writer', 'image_generator')
blog_graph.add_edge('image_generator', END)

blog_workflow = blog_graph.compile()

initial_state = {
    'topic': 'What is LangGraph'
}

generator = blog_workflow.stream(initial_state, stream_mode='messages')


for chunk, metadata in generator:
    print(chunk.content, end='')

