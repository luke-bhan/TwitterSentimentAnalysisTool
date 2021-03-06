import random


# TweetList Class: This class holds a dictionary of tweets for quick access via index
class TweetList:
    # Default Constructor
    def __init__(self):
        self.data = {}
        self.count = 1

    # Prints every tweet in dictionary
    def __str__(self):
        for attribute in self.data:
            print("ID: " + str(attribute), end=" ")
            print(self.data[attribute])
        return ""

    # Adds a tweet entry and returns the new size of the list, for convinience.
    def insert_data(self, tweet):
        if tweet not in self.data.values():
            self.data[self.count] = tweet
            self.count += 1
        return self.count

    # Removes the last tweet and returns the new size of the list, for
    # convenience.
    def remove_last(self):
        self.data = self.data[:-1]
        self.count -= 1
        return self.count

    def remove_index(self, index):
        del self.data[index]

    def remove_user(self, user):
        for key, value in self.data.items():
            if key['user'] == user:
                del self.data[key]

    def remove_creation_date(self, date):
        for key, value in self.data.items():
            if key['created_at'] == date:
                del self.data[key]

    def remove_tweet(self, text):
        for key, value in self.data.items():
            if key['text'] == text:
                del self.data[key]

    def get_tweet(self, index):
        return self.data[index]

    def get_size(self):
        return len(self.data)

    def insert_list(self, tweet_list):
        for index in tweet_list.data:
            if tweet_list.data[index] not in self.data.values():
                self.insert_data(tweet_list.data[index])

    def __len__(self):
        return self.count

    # Generates a random subset of current list of users designated size
    def generate_random_tweet_list(self, size):
        values = random.sample(range(1, self.count), size)
        tweet_list = TweetList()
        for value in values:
            tweet_list.insert_data(self.data[value])
        return tweet_list

    def get_last(self):
        return self.data[self.count-1]

