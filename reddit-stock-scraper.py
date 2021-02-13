#! python3
import praw
import pandas as pd
import configparser

def scrape(name):
    config = configparser.ConfigParser()
    config.read("config.ini")
    client_id = config.get("reddit", "client_id")
    client_secret = config.get("reddit", "client_secret")
    user_agent = config.get("reddit", "user_agent")
    username = config.get("reddit", "username")
    password = config.get("reddit", "password")
    reddit = praw.Reddit(client_id=client_id, 
                        client_secret=client_secret, 
                        user_agent=user_agent, 
                        username=username, 
                        password=password)

    subreddit = reddit.subreddit(name)
    top_subreddit = subreddit.top("day",limit=50)
    topics_dict = { "title":[], 
                    "score":[], 
                    "id":[], "url":[], 
                    "comms_num": [],
                    "created": [], 
                    "body":[]}
    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)
    topics_data = pd.DataFrame(topics_dict)
    print(topics_data)
        
if __name__ == '__main__':
    name = input("What subreddit would you like to scrape for stocks? ")
    scrape(name)