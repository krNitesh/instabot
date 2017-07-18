import matplotlib.pyplot as plt
from termcolor import colored
import requests
APP_ACCESS_TOKEN='4196634019.bdc1e98.2942e406c821424690b58fb62106c035'
BASE_URL = 'https://api.instagram.com/v1/'
def popular_hashtag():
    # For fashion hashtag
    tag_name1 = raw_input(
        colored("Choose from the category fashion<>repost,sports,fashion,pop,cultura,photography<>:- ", "blue"))
    request_url = (BASE_URL + 'tags/' + tag_name1 + '?access_token=%s') % (APP_ACCESS_TOKEN)
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
    request_url = (BASE_URL + 'tags/' + tag_name2 + '?access_token=%s') % (APP_ACCESS_TOKEN)
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
    request_url = (BASE_URL + 'tags/' + tag_name3 + '?access_token=%s') % (APP_ACCESS_TOKEN)
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
    request_url = (BASE_URL + 'tags/' + tag_name4 + '?access_token=%s') % (APP_ACCESS_TOKEN)
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

popular_hashtag()