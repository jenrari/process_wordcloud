from utils.file_management.data_writer import wc_to_file, hist_to_file
from .generate_wc import generate_wc, generate_wf_hist, create_freq_reduce
from utils.support_functions import check_empty_text, get_clusters, print_list_element, create_tweet_list


def analyze_data(tweets_df):
    """
    This function is processing the dataset with the tweets and creates the word cloud and the histograms
    for each cluster.
    Function is finally exporting wordcloud and histogram with word frequencies as png files to the the output
    data folder
    :param tweets_df: dataset imported and preprocessed as result of function prepare_data
    """
    print("Starting data processing:\n")
    print("There are {} clusters in this datasets\n".format(len(get_clusters(tweets_df))))

    # Muestra mensajes del ejercicio
    check_empty_text(tweets_df)
    print_list_element(create_tweet_list(tweets_df))
    for c in get_clusters(tweets_df):
        print("Generating word frequency dictionary for cluster {}".format(c))
        tf_list = create_tweet_list(tweets_df.loc[tweets_df["sentiment"] == c])
        tf_dict = create_freq_reduce(tf_list)
        print("Word frequency dictionary for cluster {} has been generated\n".format(c))

        print("Generating word cloud for cluster {}".format(c))
        wordcloud = generate_wc(tf_dict)
        wc_to_file(wordcloud, c)
        print("Word cloud for cluster {} generated in data output path\n".format(c))

        print("Generating word frequency plot for cluster {}".format(c))
        wf_plot = generate_wf_hist(tf_dict)
        hist_to_file(wf_plot, c)
        print("Word frequency plot for cluster {} generated in data output path\n".format(c))
