from preprocessing.preprocess_data import prepare_data
from process_data.analyze_data import analyze_data

tweets_df = prepare_data('C:\\Users\\juanma\\Desktop\\fp2\\activities\\activity_4\\data\\twitter_reduced.zip')
analyze_data(tweets_df)
