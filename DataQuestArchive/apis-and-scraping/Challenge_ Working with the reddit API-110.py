## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}

python_top = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params).json()



## 3. Getting the Most Upvoted Post ##

python_top_articles = python_top["data"]["children"]

highest = None
highest_id = None

for i in range(len(python_top_articles)):
    article = python_top_articles[i]
    article_data = article["data"]
    article_ups = article_data["ups"]
    article_id = article_data["id"]
    if (highest == None) or (highest < article_ups):
        highest = article_ups
        highest_id = article_id

most_upvoted = highest_id



## 4. Getting Post Comments ##

comments = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u",headers=headers).json()


## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]["data"]["children"]
most_upvotes_comment = None
most_upvoted_comment = None

for cm in comments_list:
    ups = cm["data"]["ups"]
    if (most_upvotes_comment == None) or (most_upvotes_comment<ups):
        most_upvotes_comment = ups
        most_upvoted_comment = cm["data"]["id"]
        print(cm["data"]["body"])
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        

    

## 6. Upvoting a Comment ##

payload = {"dir": 1, "id": "{}".format(most_upvoted_comment)}
print(payload)

status = requests.post("https://oauth.reddit.com/api/vote", headers=headers, json=payload).status_code