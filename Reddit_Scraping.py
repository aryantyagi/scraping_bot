# Importing required packages
import praw # Python Reddit API Wrapper
import pandas as pd # useful for dataframe generation
import datetime as dt # useful for timestamp generation

# Assign the praw.Reddit function to a variable
reddit = praw.Reddit(client_id = '3ZNRdvAwE5ELKw', # enter your personal reddit client_id
                     client_secret = '8yYbJjQoj4zQ3OGW3u1aW1JgAYM', # enter your personal reddit client_secret
                     username = 'aryan_tyagi', # enter your personal reddit username
                     password = '19apr1999', # enter your personal reddit password
                     user_agent = 'prawtutorialv1')

# Accept the url of the reddit submission you wish to scrape
submission = reddit.submission(url = 'https://www.reddit.com/r/Python/comments/cq53v4/i_made_a_program_that_will_help_you_find_deep/')

# Create a dictionary to store the desired parameters of the scraped comments
comment_dict = {"Author":[], "Score":[], "ID":[], "Created (Unix Time)": [], "Comment Body":[]}

# Scrape the desired data by iterating over the features mentioned in the dictionary
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    comment_dict["Author"].append(comment.author)
    comment_dict["Score"].append(comment.score)
    comment_dict["ID"].append(comment.id)
    comment_dict["Created (Unix Time)"].append(comment.created)
    comment_dict["Comment Body"].append(comment.body)

# Use Pandas to create a dataframe from the python dictionary for easy comprehension
scraped_data = pd.DataFrame(comment_dict)

# Reddit uses UNIX timestamps to store date and time.
# The following function converts the UNIX timestamps to the standard timestamps
def get_date(created):
    return dt.datetime.fromtimestamp(created)

# Adds a standard timestamp collumn to the dataframe by calling the conversion function
standard_timestamp = scraped_data["Created (Unix Time)"].apply(get_date)
scraped_data = scraped_data.assign(Timestamp = standard_timestamp )

# Saves the scraped data as a csv file ("Why_is_Fluoride_in_water_so_bad.csv")
scraped_data.to_csv("Why_is_Fluoride_in_water_so_bad.csv", index = False)

# Notes:
# 1. Double click on a cell in the Comment Body column to view the complete comment
# 2. If an author has replied to their own comment, duplicate representation in the Author column has been avoided
# 3. The column width needs to be adjusted for proper visualization of the timestamps in the CSV file. A formatted Excel file has been attached for convenience.
# 4. Feedback is appreciated: tyagi5@purdue.edu