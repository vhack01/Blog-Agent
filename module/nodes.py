from langchain_openai import ChatOpenAI
from .states import BlogState
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatOpenAI(model="gpt-5.5")
image_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def researcher(state: BlogState):
    topic = state['topic']

    prompt = f'''
        You are a expert researcher on blog writing. 
        You have to research on the topic {topic}.
    '''

    response = llm.invoke(prompt)
    return {'research': response.content}

def writer(state: BlogState):
    topic = state['topic']
    research = state['research']

    prompt = f'''Your are a expert blog writter. Write a blog based on the research and topic provided below. 
                Topic : {topic}
                Research : {research}
    '''
    response = llm.invoke(prompt)
    return {'blog': response.content}

def image_generator(state: BlogState):
    topic = state['topic']
    blog = state['blog']


    prompt = f'''
        You are a expert image generator for blog.
        Based on the blog:{blog}, generate the images for that where you feel its needed.
        After image generation put the correct image at correct places and return final blog with images
    '''

    response = image_llm.invoke(prompt)
    return {'blog_with_images': response.content}
