import sys, os, random
from twython import Twython
from auth_keys import twitter_keys

twitter = Twython(twitter_keys[0], twitter_keys[1], twitter_keys[2], twitter_keys[3])

def main():
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

if __name__ == '__main__':
    main()
