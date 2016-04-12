from entities.predict import Predict
from entities.rating import Rating
from entities.user import User
from scipy.stats.stats import pearsonr
from collections import OrderedDict
from itertools import *


def build_users(ratings: [Rating]):
    users = {}

    for rating in ratings:
        if not (users.has_key(rating.user_id)):
            users[rating.user_id] = User(rating.user_id)
        users.get(rating.user_id).add_rating(rating.movie_id, rating)



    # TODO: fill dict users with key-value pairs of user_id and the user object with its ratings
    # goal: user should later be accessible by its ID
    # after users is completely filled, call 'calc_avg_rating' on each User object

    return users


def filter_users(users: [User], movie_id):
    filtered = [User]

    for user in users:
        if not user.get_rating(movie_id):
            filtered.append(user)

    # TODO: filter users by whether they have rated the given movie

    return filtered


def calc_similarity(user_a: [User], user_b: [User]):

    ratings_a = {}
    ratings_b = {}

    for ratingA in user_a.ratings:
        for ratingB in user_b.ratings:
            if ratingA.movie_id == ratingB.movie_id:
                ratings_a = ratingA.rating
                ratings_b = ratingB.rating

    # TODO: calculate pearson coefficient and return the coefficient
    # see 'pearson correlation' in scipy

    return pearsonr(ratings_a, ratings_b)


def calc_similarities(users: [User], user: [User]):
    similarities = {}

    for u in users:
        similarities[u.user_id] = calc_similarity(u, user)

    # TODO: fill 'similarities' with pairs of user_id and similarity to the given user
    # e.g. { user_1 : 0.87, user_2 : 0.34, ... }
    # actual calculation is done in 'calc_similarity()'

    return similarities


def nearest_neighbors(user_similarities, k):

    sorted_user_sims = OrderedDict(sorted(user_similarities.items(), key=lambda x: x[1]))

    # TODO: sort users according to similarity and return sorted dictionary containing the k most similar
    # look for built-in function

    return OrderedDict(islice(sorted_user_sims.iteritems(), k))


def calc_prediction(neighbors, filtered):
    # TODO: calculate the rating by given information about similarities

    return 0


def recommend(ratings: [Rating], predicts: [Predict]):

    # value for neighbours
    k = 100
    predictions = [Rating]

    # build user objects from bare ratings
    users = build_users(ratings)

    # predict rating for each user-movie-pair
    for predict in predicts:

        # filter users which have rated the correspondent movie
        filtered = filter_users(users.values(), predict.movie_id)

        # calculate similarities with the current user
        similarities = calc_similarities(filtered, users[predict.user_id])

        # get k nearest neighbors
        neighbors = nearest_neighbors(similarities, k)

        # calculate a rating by given knowledge
        rating = (neighbors, filtered)

        predictions.append(Rating(predict.user_id, predict.movie_id, rating))

    return predictions
