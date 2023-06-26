import sys
from preprocessing.preprocess_data import prepare_data
from process_data.analyze_data import analyze_data
from utils.file_management.data_reader import check_zip_folder

"""
This is the main function of the program. It calls the preprocess_data module passing as argument the zip file
path.
Then this function executes the analyze_data module which holds all the functionalities to process the information once
it is cleaned and prepared for processing
Finally, analize_data module store the output information of the program into the output data folder
"""

zip_folder = "/home/datasci/prog_datasci_2/activities/activity_4/data/tweeter_reduced.zip"

if not check_zip_folder(zip_folder):
    print("\nIt is needed to use zip_folder variable to process file with tweets information. Please enter a valid"
          "zip file. In this project it is available a README file which you could find interesting to read\n ")
    sys. exit()


tweets_df = prepare_data(zip_folder)
analyze_data(tweets_df)
print("------------------------------------------------------------------------------------------------------------"
      "-------------------------------------------------------------------------------\n")
print("------------------------------------------------------------------------------------------------------------"
      "-------------------------------------------------------------------------------\n")

print("Check data output folder to consult wordcloud and histograms with word frequencies for "
      "different clusters\n")
print("------------------------------------------------------------------------------------------------------------"
      "-------------------------------------------------------------------------------\n")
print("a) Las palabras más repetidas en las críticas positivas son: going, day, get, like, work, got, today"
      ", cannot, back, time, want, one, now \n")
print("b) Las palabras más repetidas en las críticas negativas son: work, going, get, cannot, day, want, today"
      ", back, like, got, really, still, time \n")
print("c) Sí, existen palabras que aparecen tanto en las críticas positivas como en las negativas, de hecho hay muchas "
      "que incluso ocupan un lugar ordinal parecido \n")
print("d) En el primer grupo llama la atención la existencia de palabras asociadas a sentimientos negativos que también"
      "aparecen en el otro grupo, pero sin embargo, con mucha menos frecuencia. En cambio, en el cluster 4 palabras "
      "como love, son mucho más frecuentes. En general todas las palabras se encuentran en ambos grupos, pero en el "
      "grupo 4 las palabras asociadas a sentimientos positivos se dan con más frecuencia. LLama la atención que"
      " la palabra work sea la más frecuente en el grupo 0")
