import movie_io.reader as reader
import movie_io.writer as writer
import recommender.content_based as content
import recommender.model_based as model

# configuration values
FILE_PATH = '/home/sebastian/'      # change to actual target directory
TRAINING_FILE = 'training.dat'
PREDICT_FILE = 'predict.dat'
CONTENT_OUT = 'content.dat'
MODEL_OUT = 'model.dat'

# read ratings from files
training = reader.read_file_ratings(FILE_PATH + TRAINING_FILE)
predict = reader.read_file_predicts(FILE_PATH + PREDICT_FILE)

# apply content based filtering
content_rec = content.recommend(training, predict)
# writer.write_file(FILE_PATH + CONTENT_OUT, content_rec)

# apply model based filtering
model_rec = model.recommend(training, predict)
# writer.write_file(FILE_PATH + MODEL_OUT, model_rec)
