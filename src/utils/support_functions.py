
def print_list_element(input_list: list, num=5, descending=True):
    """
    This function takes a list ana prints n elements passed as argument in num variable. Default value for num variable
    is 5. Funtion print element in list starting by first element if argument is set by default, if descending value
    is set to False, it will start printing items from last item.
    :param descending: IF set to TRUE(default), start printing from first element, if set to FALSE starting from last
    item
    :param num: Number of itmes to print
    :param input_list: List from which take the items to print
    """
    print_list = []
    if descending:
        for i in range(num):
            print_list.append(input_list[i])
    else:
        for i in range(-1 - num):
            print_list.append(input_list[i])

    print(print_list)


def get_clusters(tweets_df) -> list:
    """
    This function gets tweets_df dataframe and return a list with the clusters contained
    :param tweets_df: dataset imported and preprocessed as result of function prepare_data
    :return tweet_list: List having the different clusters present in dataframe
    """
    return tweets_df['sentiment'].unique().tolist()


def create_tweet_list(tweets_df):
    """
    This function gets tweets_df dataframe, takes the 'tf' column and stored into a list object
    :param tweets_df: dataset imported and preprocessed as result of function prepare_data
    :return tweet_list: List having the content of 'tf' column
    """
    tweet_list = tweets_df['tf'].to_list()
    return tweet_list


def check_empty_text(tweets_df):
    """
    This function checks if there is any value missing on text column
    :param tweets_df: dataset imported and preprocessed as result of function prepare_data
    """
    empty_text = tweets_df['text'].isnull().sum()

    if empty_text == 0:
        print("There are no empty values in column \'text\' \n")
    else:
        print("There are {} empty values in column \'text\' \n".format(empty_text))
        print("There is a {} % of empty values \n".format(len(tweets_df['text'])*(empty_text / 100)))


def create_bag_list(tweets_df_text):
    """
    This function creates the bag of words from the text column of the dataframe and stored into a list
    :param tweets_df_text: text column of imported dataframe has be passed as argument
    :return bag_list: list with unique words of the text column
    """
    bag = set()
    tweets_df_text.apply(lambda x: bag.update(x.split()))
    bag_list = list(bag)
    bag_list.sort()

    return bag_list
