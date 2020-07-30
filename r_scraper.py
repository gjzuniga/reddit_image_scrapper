import praw
import requests
import os


def is_image_url(url):
    img_name = url.split('/')[-1]
    pic_format = img_name.split('.')[-1]
    pic_names = ['jpg', 'webp', 'jpeg', 'png', 'gif']
    return pic_format in pic_names


def download_image(url, folder_name):
    if not is_image_url(url):
        print(f"{url} is not a valid image url.")
    else:
        img_name = url.split('/')[-1]
        save_loc = f"Z:\\downloads\\MAIN CODE\\e\\{folder_name}"

        if not os.path.exists(save_loc):
            os.makedirs(save_loc)

        save_path = os.path.join(save_loc, img_name)

        if os.path.exists(save_path):
            print(f"{img_name} already exists.")
        else:
            response = requests.get(url)
            if response.ok:  # verify url request worked
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                print(f"{img_name} has been downloaded")
            else:
                print("That image could not be downloaded.")


reddit = praw.Reddit("bot1")

desired_sub = input("Enter a subreddit name: ")
subreddit = reddit.subreddit(desired_sub)
print(subreddit.display_name)
search_term = input("Enter your search term: ")

for submission in subreddit.hot(limit=50):
    download_image(submission.url, search_term )

# for i in range(10):
#     download_image(subreddit.random().url)
# for sub in subreddit.hot(limit = 10):
#     if sub.link_flair_text == "blank":
#         download_image(sub.url, search_term)
