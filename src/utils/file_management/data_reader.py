import pandas as pd
import os.path
import zipfile as zf

# Definition variable for project data path
data_path = "./data/"


def check_zip_folder(zip_folder):
    if zip_folder is "":

        return False


def read_csv_to_df(zip_path: str) -> pd.DataFrame:
    """
    This function uncompress zip file with twitter information and load content of csv in a dataset.
    Files are uncompressed in project data folder.
    If not argument is entered, input via terminal the zip file´s path
    :param zip_path: Argument passed as string, path of twitter zip file
    :return: Pandas dataframe for twitter csv content
    """
    csv_path = data_path + "twitter_reduced.csv"

    with zf.ZipFile(zip_path, 'r') as zip_f:
        if not os.path.exists(csv_path):
            zip_f.extractall(path=data_path)

    tweets_df = pd.read_csv(csv_path)
    return tweets_df
