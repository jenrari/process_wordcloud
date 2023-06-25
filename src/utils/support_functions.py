
def print_list_element(input_list: list, num=5, descending=True):

    print_list = []
    if descending:
        for i in range(num):
            print_list.append(input_list[i])
    else:
        for i in range(-1 - num):
            print_list.append(input_list[i])

    return print(print_list)


def get_clusters(tweets_df) -> list:

    return tweets_df['sentiment'].unique().tolist()


def check_empty_text(tweets_df):

    empty_text = tweets_df['text'].isnull().sum()

    if empty_text == 0:
        print("There are no empty values in column \'text\'")
    else:
        print("There are {} empty values in column \'text\'".format(empty_text))
        print("There is a {} % of empty values".format(len(tweets_df['text'])*(empty_text / 100)))



def create_bag_list(tweets_df_text):

    bag = set()
    tweets_df_text.apply(lambda x: bag.update(x.split()))
    bag_list = list(bag)
    bag_list.sort()

    return bag_list
