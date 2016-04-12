class Rating:
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating

    def to_string(self):
        return 'userID: ' + str(self.user_id) + ' movieID: ' + str(self.movie_id) + ' rating: ' + str(self.rating)
