from src.preprocessing.preprocess_utils import preprocess_text, remove_stop_words, remove_extra_white_space, calculate_tf
from src.utils.file_management.data_reader import read_csv_to_df
from src.utils.file_management.data_writer import dataframe_to_csv
from src.utils.support_functions import create_bag_list, print_list_element


def prepare_data(zip_path: str):

    tweets_df = read_csv_to_df(zip_path)
    tweets_df = preprocess_text(tweets_df)
    tweets_df = remove_extra_white_space(tweets_df)
    tweets_df = remove_stop_words(tweets_df)

    tweets_df = tweets_df.assign(tf=calculate_tf(tweets_df['text']))

    print_list_element(create_bag_list(tweets_df['text']))
    print_list_element(calculate_tf(tweets_df['text']), 10)

    # Print element 20th from dataset
    print(tweets_df.iloc[20])

    dataframe_to_csv(tweets_df)
    return tweets_df
