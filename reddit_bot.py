# -*- coding: utf-8 -*-
"""
Spyder Editor

Let's try  to do a sentiment analysis over posts mentioning Eden Hazard

"""

import praw 
import csv
from praw.models import MoreComments
from secrets import *


def main():
    reddit = praw.Reddit(
            user_agent = tb_user_agent,
            client_id = tb_client_id,
            client_secret = tb_client_secret,
            username = tb_username,
            password = tb_password)
    
if __name__ == "__main__":
    main()
    

# Specific things to look after
hazard_strings = ["hazard","benteke"]

i = 0

with open('players_comments.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(["player","submission_id","submission_url","submission_title","submission_karma","submission_utc_time",
                       "comment_id","comment_utc_time","comment_user","comment_text","comment_karma"])
    for submission in reddit.subreddit('soccer').hot(limit=100):
        normalized_title = submission.title.lower()
        for key_phrase in hazard_strings:
            print("We are now looking for '",key_phrase,"' in the title ",i,": ",normalized_title,"\n")
            if key_phrase in normalized_title:
                # start analyzing comments and check for sentiment.
                print("\n\n WE FOUND",key_phrase.upper()," \n\n")
                for comment in submission.comments:
                    csvwriter.writerow([key_phrase,submission.id,submission.url,submission.title,submission.upvote_ratio,submission.created_utc,
                                       comment.id,comment.created_utc,comment.author,comment.body,comment.score])
                break
        i+=1
    print("All done here")



















