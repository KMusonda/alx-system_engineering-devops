#!/usr/bin/python3

"""
a recursive function that queries the Reddit API, 
parses the title of all hot articles, and prints a sorted count of given keywords
"""

import requests
from collections import Counter

def count_words(subreddit, word_list, after=None, word_counter=None):
    if word_counter is None:
        word_counter = Counter()

    try:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'
        headers = {'User-Agent': 'Custom User Agent'}  # Set your custom User-Agent here
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            for post in posts:
                title = post['data']['title']
                for word in word_list:
                    if f' {word.lower()} ' in title.lower():
                        word_counter[word.lower()] += 1
            
            after = data['data']['after']
            if after:
                count_words(subreddit, word_list, after, word_counter)
            else:
                sorted_words = sorted(word_counter.keys(), key=lambda word: (-word_counter[word], word))
                for word in sorted_words:
                    print(f'{word}: {word_counter[word]}')
        else:
            print("None")
    except:
        print("None")

