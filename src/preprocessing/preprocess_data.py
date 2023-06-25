from .preprocess_utils import preprocess_text, remove_extra_white_space, remove_stop_words, calculate_tf
from utils.file_management.data_reader import read_csv_to_df
from utils.file_management.data_writer import dataframe_to_csv
from utils.support_functions import create_bag_list, print_list_element


def prepare_data(zip_path: str):
    """
    This function takes the file path of the zip file with the tweets information and applies all functions to
    preprocess the data. First is calling the reader functions passing the zip file path to process the zip file
    and import it as a dataframe. When preprocessing data in the dataframe, it applies several functions
    to clean the text data of tweets. It also adds a new column to the dataset which contains the word frequency for
    each tweet.
    :param zip_path: This is the path of the zip file containing tweeter information
    :return tweets_df: It returns a dataframe which has been preprocessed
    """
    # Unzipping zip file and importing csv file
    print("\nStarting to preprocess data:\n")
    tweets_df = read_csv_to_df(zip_path)

    print("Printing first 5 tweet information from csv file as a dictionary\n")
    print(tweets_df[0:5].to_dict('records'))
    print("------------------------------------------------------------------------------------------------------------"
          "-------------------------------------------------------------------------------\n")
    # Executing functions to clean text data:
    # Applying different regular expressions to remove URLs, removing non ASCII characters and removing some words
    # which do not provide any relevant information.
    # Removing extra white spaces and words with less than 3 characters
    # Removing stopwords
    tweets_df = preprocess_text(tweets_df)
    tweets_df = remove_extra_white_space(tweets_df)
    tweets_df = remove_stop_words(tweets_df)

    print("Printing last 5 rows of dataset after cleaning text and removing stopwords\n")
    print(tweets_df.tail())
    print("------------------------------------------------------------------------------------------------------------"
          "-------------------------------------------------------------------------------\n")
    # Adding column tf to dataset. This column is a word frequency dictionary for each tweet
    tweets_df = tweets_df.assign(tf=calculate_tf(tweets_df['text']))

    print("Printing word frequencies for first 5 tweets")
    print_list_element(calculate_tf(tweets_df['text']))
    print("------------------------------------------------------------------------------------------------------------"
          "-------------------------------------------------------------------------------\n")
    print("Printing bag 10 first elements of bag of words sorted alphabetically")
    print_list_element(create_bag_list(tweets_df['text']), 10)
    print("------------------------------------------------------------------------------------------------------------"
          "-------------------------------------------------------------------------------\n")

    # Print element 20th from dataset
    print(tweets_df.iloc[20])

    # Saving dataset to csv into data output folder
    dataframe_to_csv(tweets_df)
    return tweets_df
