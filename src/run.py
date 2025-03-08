import openai
# import keyboard
from retriever import *

# Initialize the chat messages history
messages = [{"role": "assistant", "content": "How can I help?"}]

# # Function to display the chat history
# def display_chat_history(messages):
#     for message in messages:
#         print(f"{message['role'].capitalize()}: {message['content']}")


def query_expansion(messages, query):
    # print(messages)
    exp_query = '\n'.join([f"'role': {m['role']}, 'content': {m['content']}" for m in messages])

    query_xp = exp_query+f' Now based on previous chat please provide the answer for query: {query}\n Answer:'
    return query_xp

# Main chat loop
if __name__=="__main__":
    while True:
        prompt = input("User: ")
        
        query = query_expansion(messages, prompt)
        # print(query)
        response = query_rag_system(query)
        print(response['content'])

        inp = input("do you want to continue or do you want to start?: ")
        if inp =='start':
            messages = [{"role": "assistant", "content": "How can I help?"}]
        else:
            messages.append(response)
        
        
        