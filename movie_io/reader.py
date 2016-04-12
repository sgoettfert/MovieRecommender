import csv
from entities.rating import Rating
from entities.predict import Predict

# define constants
DELIMITER = '\t'
QUOTING = '"'


# parse a line and return Rating object (false on error)
def parse_line_rating(params):
    if len(params) != 3:
        return False
    else:
        return Rating(params[0], params[1], params[2])


# read a file with ratings and return list of parsed Rating entities
def read_file_ratings(filename):
    entities = []
    malformed = 0

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=DELIMITER, quotechar=QUOTING)

        for line in reader:
            entity = parse_line_rating(line)

            if entity:
                entities.append(entity)
            else:
                malformed += 1

    print('Read ' + str(len(entities) - 1) + ' lines')
    print('Encountered ' + str(malformed) + ' malformed lines')

    print(len(entities))

    return entities


# parse a line and return Predict object (false on error)
def parse_line_predict(params):
    if len(params) != 2:
        return False
    else:
        return Predict(params[0], params[1])


# read a file with predicts and return list of parsed Predict entities
def read_file_predicts(filename):
    entities = []
    malformed = 0

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=DELIMITER, quotechar=QUOTING)

        for line in reader:
            entity = parse_line_predict(line)

            if entity:
                entities.append(entity)
            else:
                malformed += 1

    print('Read ' + str(len(entities) - 1) + ' lines')
    print('Encountered ' + str(malformed) + ' malformed lines')

    return entities
