from src.preprocessing.preprocess_data import prepare_data
from src.utils.file_management.data_writer import wc_to_file, hist_to_file
from src.process_data.generate_wc import generate_wc, generate_wf_hist, create_freq_reduce
from src.preprocessing.preprocess_utils import create_tweet_list
from src.utils.support_functions import check_empty_text, get_clusters, print_list_element

tweets_df = prepare_data('C:\\Users\\juanma\\Desktop\\fp2\\activities\\activity_4\\data\\twitter_reduced.zip')

print("Starting data process")
print("There are {} clusters in this datasets".format(len(get_clusters(tweets_df))))
   # Muestra mensajes del ejercicio
check_empty_text(tweets_df)
print_list_element(create_tweet_list(tweets_df))
for c in get_clusters(tweets_df):
    print("Generating word frequency dictionary")
    tf_list = create_tweet_list(tweets_df.loc[tweets_df["sentiment"] == c])
    tf_dict = create_freq_reduce(tf_list)
    print("Word frequency dictionary generated")

    print("Generating word cloud fro cluster {}".format(c))
    wordcloud = generate_wc(tf_dict)
    wc_to_file(wordcloud, c)
    print("Word cloud for cluster {} generated in data output path".format(c))

    print("Generating word frequency plot for cluster {}".format(c))
    wf_plot = generate_wf_hist(tf_dict)
    hist_to_file(wf_plot, c)
    print("Word frequency plot for cluster {} generated in data output path".format(c))
