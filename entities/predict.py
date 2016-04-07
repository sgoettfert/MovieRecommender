class Predict:
    def __init__(self, user_id, movie_id):
        self.user_id = user_id
        self.movie_id = movie_id

    def to_string(self):
        return 'userID: ' + self.user_id + ' movieID: ' + self.movie_id
