class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User(1, "issei2019")
user2 = User(2, "Killer bie")

user1.follow(user2)
user1.follow(user2)
print(user1.following)