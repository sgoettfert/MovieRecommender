import movie_io.reader as reader
import movie_io.writer as writer
import recommender.content_based as content
import recommender.model_based as model

from entities.predict import Predict

# file configuration
FILE_PATH = '/home/sebastian/'      # change to actual target directory
TRAINING_FILE = 'mytraining.dat'
PREDICT_FILE = 'short.dat'
CONTENT_OUT = 'content.dat'
MODEL_OUT = 'model.dat'

# script configuration
k = 100
percentage = 80     # percentage of training data used as training for cross validation

# read ratings from files
training = reader.read_file_ratings(FILE_PATH + TRAINING_FILE)
predict = []

size = len(training)
training_limit = size * percentage // 100

print("limit: " + str(training_limit))

for train in training[training_limit + 1:]:
    predict.append(Predict(train.user_id, train.movie_id))


# apply content based filtering
content_rec = content.recommend(training, predict, k)

mean_error = []

for i in range(training_limit + 1, len(training) - 1):
    error = float(content_rec[i - training_limit].rating) - float(training[i].rating)
    error **= 2
    mean_error.append(error)
    print("User: " + str(training[i].user_id) + " Movie: " + str(training[i].movie_id) + " Error: " + str(error))

print("mean_error: " + str(len(mean_error)))
print("Average mean error with K = " + str(k) + " : " + str(sum(mean_error) / len(mean_error)))

# writer.write_file(FILE_PATH + CONTENT_OUT, content_rec)

# apply model based filtering
# model_rec = model.recommend(training, predict)
# writer.write_file(FILE_PATH + MODEL_OUT, model_rec)
