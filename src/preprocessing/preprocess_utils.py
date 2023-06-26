import contractions as contractions
import pandas as pd

# Variable stop_words definition, to be used to removed stop_words using function remove_stop_words(tweets_df)
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
              'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
              'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these',
              'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',
              'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
              'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',
              'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
              'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
              'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than',
              'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']


def preprocess_text(tweets_df: pd.DataFrame) -> pd.DataFrame:
    """
    This function applies several regular expressions to clean the text of words with no meaning.
    :param tweets_df: It gets the dataframe to process
    :return tweets_df: It returns the dataframe after processing the text
    """

    # Remove URLs
    tweets_df['text'].replace(to_replace=r'http[s]?:\/\/\w+\.\w+[/\w]*', value='', regex=True, inplace=True)
    # Remove mentions to users using @
    tweets_df['text'].replace(to_replace=r'@[\w]+', value='', regex=True, inplace=True)
    # Applying function contractions to separate english contractions
    tweets_df['text'] = tweets_df['text'].apply(lambda x: contractions.fix(x.lower()))
    # Remove characters which are not ASCII
    tweets_df['text'].replace(to_replace=r'[^\x00-\x7F]', value='', regex=True, inplace=True)
    # Remove characters which are not alphabetic characters or blank spaces
    tweets_df['text'].replace(to_replace=r'[^a-z\s]', value='', regex=True, inplace=True)
    # Remove characters repeated more than twice in a word ie(aaaa or hhhhhhh)
    tweets_df['text'].replace(to_replace=r'(.{2}?)\1+', value='', regex=True, inplace=True)

    return tweets_df


def remove_stop_words(tweets_df) -> pd.DataFrame:
    """
    This function remove stopwords defined in variable stop_words from 'text' column in the given dataframe
    :param tweets_df: imported dataframe can be passed as argument
    :return tweets_df: it returns tweets_df dataframe after removing stopwords
    """
    tweets_df['text'] = tweets_df['text'].apply(lambda x: ' '.join([word for word in x.split()
                                                                    if word not in stop_words]))
    return tweets_df


def remove_extra_white_space(tweets_df) -> pd.DataFrame:
    """
    This function remove white spaces in words from 'text' column in the given dataframe
    :param tweets_df: imported dataframe can be passed as argument
    :return: it returns tweets_df dataframe after processing
    """
    ds = tweets_df['text']
    tweets_df['text'] = ds.apply(lambda x: ' '.join([word.strip() for word in x.split() if len(word) > 2
                                                     and word[0] != word[1] != word[2]]))
    return tweets_df


def calculate_tf(tweets_df_text) -> list:
    """
    This function gets as a parameter dataframe column text and it calculates the word frequency for every tweet
    stored in 'text' column. Word frequencies are calculated as a dictionary per tweet, all dictionaries are
    stored as a list
    :param tweets_df_text: text column of imported dataframe has be passed as argument
    :return: It returns a list of dictionaries with the word frequencies per tweet
    """
    tf = []
    tweets_df_text.apply(lambda x: tf.append({word: x.split().count(word) for word in x.split()}))
    return tf
