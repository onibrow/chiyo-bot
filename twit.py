import sys, os, random
from twython import Twython
from auth_keys import twitter_keys

twitter = Twython(twitter_keys[0], twitter_keys[1], twitter_keys[2], twitter_keys[3])

cons_key = '2QYC8BipkGErbXI1wV4jUNMjV'
cons_sec = 'V7PZksPzZxgUbGH2O3W8BkyjpZ8UcWfkkjZsGWSUDjrTlvCb7f'
toke_key = '1128381792883363840-hvCWFrakC9ko2ZICl2gklQ1eIuvaft'
toke_sec = 'm06Z4PaeP2RULvQ5X09KknmCUDhTB9QzKxt9RTTz0dWkd'

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
