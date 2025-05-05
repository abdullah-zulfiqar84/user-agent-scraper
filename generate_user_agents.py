import random
from fake_useragent import UserAgent

ua = UserAgent()

def generate_user_agents(count=1000, filename="user_agents.txt"):
    user_agents = [ua.random for _ in range(count)]

    # Save to a text file
    with open(filename, "w") as file:
        for agent in user_agents:
            file.write(agent + "\n")
    
    print(f" Saved {count} user agents to {filename}")

generate_user_agents(1000, "user_agents.txt")
