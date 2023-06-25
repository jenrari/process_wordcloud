from functools import reduce
from wordcloud import WordCloud
import matplotlib.pyplot as plot

# Definition of variable for dictionary with frequency table
dict_fre = {}


def create_freq_reduce(tf_list):

    """
    Creates frequency table dictionary from tf column list, it applies function sum dict over tf column. It checks
    word frequency row by row creating the frequency table dictionary to create wordcloud
    :param tf_list: tf column list. Use
    :return: dictionary with frequency table for words
    """

    return reduce(sum_dict, tf_list, {})


def sum_dict(a, b) -> dict:

    """
    Function to check two dictionaries, if keys listed in dictionary b are not in dict a, are added with the existing
    value. If keys from dict b are already in dict a, value for key in dict b is added to value in dict a for that key.
    Function to be used with reduce function to create frequency table.
    :param a: dict a
    :param b: dict b
    :return: dictionary
    """

    for k in b.items():
        if k[0] in a.keys():
            dict_fre[k[0]] = a[k[0]] + k[1]
        else:
            dict_fre[k[0]] = k[1]

    return dict_fre


def generate_wc(tf_dict):
    """
    Function to generate wordcloud having table frequency in a dictionary. It returns a wordcloud object. Background
    color for wordcloud is set up to white
    :param tf_dict: table frequency dictionary, it can be generated by create_freq_reduce funtion on this module.
    :return: wordcloud object
    """
    wordcloud = WordCloud(background_color='white', width=1920, height=1080).generate_from_frequencies(tf_dict)
    return wordcloud


def generate_wf_hist(tf_dict, n=50):
    """

    :param tf_dict:
    :param n:
    :return:
    """
    sorted_wf = dict(sorted(tf_dict.items(), key=lambda item: item[1], reverse=True))
    sorted_wf_keys = list(sorted_wf.keys())
    max_wf_dict = {}
    for i in range(n):
        max_wf_dict[sorted_wf_keys[i]] = sorted_wf[sorted_wf_keys[i]]

    plot.figure(figsize=(28, 6), dpi=100)
    plot.bar(max_wf_dict.keys(), max_wf_dict.values())
    plot.title('Words Frequencies Histogram')
    plot.xlabel('Words')
    plot.ylabel('Frequencies')
    return plot