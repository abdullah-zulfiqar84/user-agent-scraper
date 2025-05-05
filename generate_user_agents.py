import random
from fake_useragent import UserAgent

# Initialize the UserAgent object to generate random user agents
ua = UserAgent()

# Define a function to generate and save user-agent strings
def generate_user_agents(count=1000, filename="user_agents.txt"):
    user_agents = [ua.random for _ in range(count)]

    # Save to a text file (one user-agent per line)
    with open(filename, "w") as file:
        for agent in user_agents:
            file.write(agent + "\n")
    
    print(f"✅ Saved {count} user agents to {filename}")

# Call the function to generate 1000 user agents and save them to a file
generate_user_agents(1000, "user_agents.txt")
