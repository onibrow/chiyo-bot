import sys, os, random, git, time
from twython import Twython
from auth_keys import twitter_keys

twitter = Twython(twitter_keys[0], twitter_keys[1], twitter_keys[2], twitter_keys[3])
repo = git.cmd.Git('.')

def post():
    repo.pull()
    file_name = random.choice(os.listdir("img/"))
    file_path =  "img/" + file_name
    try:
        open_file = open(file_path, 'rb')
    except FileNotFoundError as c:
        print("Can't find file %s" % file_path)
        return
    response = twitter.upload_media(media=open_file)
    media_id = [response['media_id']]
    message = file_path[4:-4]
    twitter.update_status(status=message, media_ids=media_id)
    print("Tweeted: %s" % message)

def main():
    while (True):
        post()
        time.sleep(600)

if __name__ == '__main__':
    main()

