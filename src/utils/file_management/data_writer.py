
data_path = ".\data\\"
output_path = data_path + "output\\"


def dataframe_to_csv(tweets_df):
    """

    :rtype: object
    """
    output_csv = data_path + 'twitter_processed.csv'
    return tweets_df.to_csv(output_csv, encoding='utf-8', index=False)


def wc_to_file(wordcloud, cluster):
    wordcloud.to_file(output_path + 'cluster{}.png'.format(cluster))


def hist_to_file(plot, cluster):
    plot.savefig(output_path + "word_frequencies{}.png".format(cluster))
