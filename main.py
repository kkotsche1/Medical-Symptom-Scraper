from bs4 import BeautifulSoup
import requests
import pandas as pd

# alphabet = ["a","b","c","d","e","f","g","h","i","j","k"
#     ,"l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#
# final_list = []
#
# for letter in alphabet:
#
#     URL = f"https://www.medicinenet.com/symptoms_and_signs/alpha_{letter}.htm"
#     html = requests.get(URL).text
#
#     soup = BeautifulSoup(html, "html.parser")
#     results_div = soup.find(class_="AZ_results")
#     results_lists = results_div.find_all("a")
#
#     for result in results_lists:
#         final_list.append(result.text)
#
# df = pd.DataFrame(final_list, columns = ["Symptom"])
# df.to_csv("Symptom_List.csv")

symptoms=[]


df = pd.read_csv("Symptom_List.csv")

for index, row in df.iterrows():
    symptom = row["Symptom"]

    symptoms.append(symptom)

print(symptoms)





