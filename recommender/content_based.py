from entities.predict import Predict
from entities.rating import Rating
from entities.user import User
from scipy.stats.stats import pearsonr
from collections import OrderedDict
from itertools import *

import operator
import scipy as sc
import numpy as np


def build_users(ratings: [Rating]):
    users = {}

    for rating in ratings:
        if rating.user_id not in users:
            users[rating.user_id] = User(rating.user_id)
        users[rating.user_id].add_rating(rating.movie_id, int(rating.rating))

    for k, v in users.items():
        v.calc_avg_rating()

    return users


def filter_users(users: [User], movie_id):
    filtered = []

    for user in users:
        if user.get_rating(movie_id):
            filtered.append(user)

    return filtered


def calc_similarity(user_a: User, user_b: User):

    ratings_a = []
    ratings_b = []

    for ratingA in user_a.ratings:
        for ratingB in user_b.ratings:
            if ratingA == ratingB:
                ratings_a.append(user_a.ratings[ratingA])
                ratings_b.append(user_b.ratings[ratingA])

    # omit the p-value which would be at position 1 from result of pearsonr()
    return pearsonr(sc.array(ratings_a).astype(np.float), sc.array(ratings_b).astype(np.float))[0]


def calc_similarities(users: [User], user: User):
    similarities = {}

    for u in users:
        similarities[u.user_id] = calc_similarity(u, user)

    return similarities


def nearest_neighbors(user_similarities, k):
    sorted_users = sorted(user_similarities.items(), key=operator.itemgetter(1))

    return sorted_users[0:k]


def calc_prediction(neighbors, filtered, movie_id):
    denominator = 0.0
    numerator = 0.0

    for k, v in neighbors:
        for user in filtered:
            if k == user.user_id:
                numerator += v * (user.get_rating(movie_id) - user.avg_rating)
                denominator += float(v)

    return numerator / denominator


def recommend(ratings: [Rating], predicts: [Predict]):

    # value for neighbours
    k = 100
    predictions = []

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

        # TODO: handle possible exception, if neighbors is an empty list!

        # calculate a rating by given knowledge
        rating = users[predict.user_id].avg_rating + calc_prediction(neighbors, filtered, predict.movie_id)

        # add prediction to list of predictions
        predictions.append(Rating(predict.user_id, predict.movie_id, rating))

    for predict in predictions:
        print(predict.to_string())

    return predictions
