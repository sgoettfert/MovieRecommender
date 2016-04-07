import csv
from entities.rating import Rating

# define constants
DELIMITER = '\t'
QUOTING = '"'


# write predicted ratings to file
def write_file(filename, entities: [Rating]):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=DELIMITER, quotechar=QUOTING, quoting=csv.QUOTE_MINIMAL)

        for entity in entities:
            writer.writerow([entity.user_id, entity.movie_id, entity.rating])
