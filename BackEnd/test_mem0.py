from dotenv import load_dotenv
from mem0 import MemoryClient
import logging
import json


load_dotenv()
user_name = 'Vikas'
mem0 = MemoryClient()

def add_memory():
    
    messages_formatted = [
        {        "role": "user",
            "content": "my fiance / lover name is Karthika."
        },
        {
            "role": "assistant",
            "content": "Ho great nice name , your fiance is lucky to have you."
        },
        {
            "role": "user",
            "content": "I think so too."
        },
        {
            "role": "assistant",
            "content": "What is your favorite song by them?"
        },
         {
            "role": "user",
            "content": "Nee Singam Dhan."
        }
    ]

    mem0.add(messages_formatted, user_id="Vikas")

def get_memory_by_query():
    mem0 = MemoryClient()
    query = "What are {user_name}'s preferences?"
    results = mem0.search(query, user_id=user_name)

    memories = [
            {
                "memory": result["memory"],
                "updated_at": result["updated_at"]
            }
            for result in results
        ]
    memories_str = json.dumps(memories)
    print(f"Memories: {memories_str}")
    return memories_str


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    get_memory_by_query()
