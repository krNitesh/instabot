import requests, urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from termcolor import colored
import matplotlib.pyplot as plt
access_token = '4196634019.bdc1e98.2942e406c821424690b58fb62106c035'

base_url = 'https://api.instagram.com/v1/'

#function to get our own post

def own_info():
    request_url = (base_url + 'users/self/?access_token=%s') % (access_token)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'status code is other than 200!'

#function to get the ID of a user

def get_user_id(insta_username):
    request_url = (base_url + 'users/search?q=%s&access_token=%s') % (insta_username, access_token)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'status code is other than 200!'
        exit()

#function to get the info of a user

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does nt exist!'
        exit()
    request_url = (base_url + 'users/%s?access_token=%s') % (user_id, access_token)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'Data for this user not found!'
    else:
        print 'status code is other than 200!'

#function to get your recent post

def get_own_post():
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (access_token)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Image downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code is other than 200!'

#function to find the recent post of a user by his/her username

def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, access_token)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Image has been downloaded successfully!'
        else:
            print 'Post does not exist!'
    else:
        print 'status code is other than 200!'

#function  to get the the recent post of a user by username

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, access_token)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'REcent post of the user not found!'
            exit()
    else:
        print 'Status code is other than 200!'
        exit()

#Function to like a recent post of a user

def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (base_url + 'media/%s/likes') % (media_id)
    payload = {"access_token": access_token}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'like successfully'
    else:
        print 'Unable to like this post'
#function to add a comment on a post
def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": access_token, "text" : comment_text}
    request_url = (base_url + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "comment added"
    else:
        print "can't add a comment"

#function to get popular Hashtags
def popular_hashtag():
    # For fashion hashtag
    tag_name1 = raw_input(
        colored("Choose from the category fashion<>repost,sports,fashion,pop,cultura,photography<>:- ", "blue"))
    request_url = (base_url + 'tags/' + tag_name1 + '?access_token=%s') % (access_token)
    print 'GET request url : %s' % (request_url)
    popular_hash_tag = requests.get(request_url).json()
    if popular_hash_tag['meta']['code'] == 200:
        if len(popular_hash_tag['data']):
            media_count1 = popular_hash_tag["data"]["media_count"]
            print "MEDIA COUNT = " + str(media_count1)
        else:
            return None
    else:
        print 'Status code is other than 200!'

    # FOR BLOGGER HASHTAGS
    tag_name2 = raw_input(colored(
        "Choose from the category blogger<>happy,love ,blogger ,hairstyle ,tumblr ,tumblrgirl<>:- ",
        "magenta"))
    request_url = (base_url + 'tags/' + tag_name2 + '?access_token=%s') % (access_token)
    print 'GET request url : %s' % (request_url)
    popular_hash_tag = requests.get(request_url).json()
    if popular_hash_tag['meta']['code'] == 200:
        if len(popular_hash_tag['data']):
            media_count2 = popular_hash_tag["data"]["media_count"]
            print "MEDIA COUNT=" + str(media_count2)  # To Return the media count
        else:
            return None
    else:
        print 'Status code is other than 200!'

    # FOR FOOD HASHTAGS
    tag_name3 = raw_input(
        colored("Choose from the category food<>foodlove ,chocolate, instafood, foodporn<>:- ", "green"))
    request_url = (base_url + 'tags/' + tag_name3 + '?access_token=%s') % (access_token)
    print 'GET request url : %s' % (request_url)
    popular_hash_tag = requests.get(request_url).json()
    if popular_hash_tag['meta']['code'] == 200:
        if len(popular_hash_tag['data']):
            media_count3 = popular_hash_tag["data"]["media_count"]
            print"MEDIA COUNT =" + str(media_count3)  # To Return the media count
        else:
            return None
    else:
        print 'Status code is other than 200!'

    # FOR TRAVEL HASHTAGS
    tag_name4 = raw_input(colored(
        "Choose from the category travel<>travel ,instatravel ,travelgram ,tourism ,instago,travelblogger ,wanderlust<>:- ",
        "red"))
    request_url = (base_url + 'tags/' + tag_name4 + '?access_token=%s') % (access_token)
    print 'GET request url : %s' % (request_url)
    popular_hash_tag = requests.get(request_url).json()
    if popular_hash_tag['meta']['code'] == 200:
        if len(popular_hash_tag['data']):
            media_count4 = popular_hash_tag["data"]["media_count"]
            print"MEDIA COUNT" + str(media_count4)
        else:
            return None
    else:
        print 'Status code is other than 200!'
    print(colored("~~~~~~~~~~~~The pie-chart will be plotted on the basis of hashtags you chose for the categories~~~~~~~~~","red","on_cyan"))
    print(colored("<>~~~~~~~~~~~~~~~~~~~~~~~~The pie-chart is being plot with perfect counts~~~~~~~~~~~~~~~~~~~~~~~~~~~<>","red", "on_yellow"))
    print "~~~~~~@@~~~~~~~~@@@~~~~~~~~~~~~~@@@@@~~~~~~~~~~~~~~~~~~~~~~~@@@@@@@@@~~~~~~~~~~~~~~~~~~~~~~~~@@@@@@@@@@@@@@@"
    # Data to plot
    labels = 'Fahion'+"("+"#"+tag_name1+")", 'Blogger'+"("+"#"+tag_name2+")", 'Food'+"("+"#"+tag_name3+")", 'Travel'+"("+"#"+tag_name4+")"
    sizes = [media_count1, media_count2, media_count3, media_count4]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    return plt.show()


#menu option for the user
def start_bot():
    while True:
        print '\n'
        print 'Namastey'
        print 'you are welcome to Instabot!'
        print 'These are your menu option:'
        print "1.To get your own details\n"
        print "2.To get detail of a user by username\n"
        print "3.To get your own recent post\n"
        print "4.To get the recent post of a user by username\n"
        print "5.Like the recent post of a user\n"
        print "6.Add a comment on the recent post of a user\n"
        print '7.To get popular hashtags'
        print "8.Exit"

        choice = raw_input("Please enter you choice: ")
        if choice == "1":
            own_info()
        elif choice == "2":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice=="5":
           insta_username = raw_input("Enter the username of the user: ")
           like_a_post(insta_username)
        elif choice=="6":
           insta_username = raw_input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice=="7":
           popular_hashtag()
        elif choice == "8":
            exit()
        else:
            print "Sorry!! you have opt for a wrong choice"
start_bot()