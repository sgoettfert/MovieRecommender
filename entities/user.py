class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.ratings = {}
        self.avg_rating = False

    def add_rating(self, movie_id, rating):
        self.ratings[movie_id] = rating

    def get_rating(self, movie_id):
        if movie_id in self.ratings:
            return self.ratings[movie_id]
        else:
            return False

    def calc_avg_rating(self):
        sum_ratings = sum(self.ratings.values())
        count_ratings = len(self.ratings.keys())
        self.avg_rating = sum_ratings / count_ratings
