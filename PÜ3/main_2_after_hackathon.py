# UC 2.0

## Benötigte Pakete importieren

import os
import pandas as pd
import neurokit2 as nk
import json


#%% UC 2.1 Einlesen der Daten
# Software importiert die Datensätze
# Code filtert die vorgegeben Daten heraus

list_of_new_tests = [] #Erstellt eine leere liste der später Werte zugeordnet werden 

## Überprüfen ob Dateien vorhanden sind


folder_current = os.path.dirname(__file__) #os.path.dirname() auslesen des Pfades des directorys indem wir gerade arbeiten
print(folder_current)
folder_input_data = os.path.join(folder_current, 'input_data') #os.path.join() fügt mehrere Pfade zusammen
print(folder_input_data) 
for file in os.listdir(folder_input_data): #os.listdir() listet alle dateien auf, die sich in() befinden

#Es sollen nur .csv Dateien beachtet werden, die dann am Ende des Pfades angehängt werden
    if file.endswith(".csv"): 
        file_name = os.path.join(folder_input_data, file)
        print(file_name)
        subject_id = file_name.split()
        new_ecg_data= pd.read_csv(file_name)
        list_of_new_tests.append(new_ecg_data)#Der vormals leeren Liste werden die ecg Werte übergeben


new_ecg_data["Subject_3"].plot() #Die Daten werden geplottet
print(new_ecg_data)
#%% UC 2.2 Vorverarbeiten der Daten

## Anlegen einer Zeitreihe der Herzfrequenz aus den EKG-Daten


ekg_data=pd.DataFrame()
ekg_data["ECG"] = new_ecg_data["Subject_3"]

# Find peaks
peaks, info = nk.ecg_peaks(ekg_data["ECG"], sampling_rate=1000)

number_of_heartbeats = peaks["ECG_R_Peaks"].sum()

duration_test_min = ekg_data.size/1000/60

average_hr_test = number_of_heartbeats / duration_test_min

## Calculate heart rate moving average

peaks['average_HR_10s'] = peaks.rolling(window=10000).mean()*60*1000
peaks['average_HR_10s'].plot()


#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium

termination = False


## Vergleich der Maximalen Herzfrequenz mit Alter des Patienten

folder_input_data = os.path.join(folder_current, 'input_data')


# Opening JSON file

file_name = folder_input_data = os.path.join(folder_input_data, 'subject_3.json')

f = open(file_name)
 
# returns JSON object as
# a dictionary

subject_data = json.load(f)


maximum_hr = peaks['average_HR_10s'].max()

subject_max_hr = 220 - (2022 - subject_data["birth_year"])

if maximum_hr > subject_max_hr*0.90:
    termination = True

#%% UC 2.4 Erstellen einer Zusammenfassung
##Alles so geändert, sodass print nur einmal ausgeführt werden muss

print("Summary for Subject " + str(subject_data["subject_id"]) 
+ "\nYear of birth:  " + str(subject_data["birth_year"]) 
+ "\nTest level power in W:  " + str(subject_data["test_power_w"]) 
+ " \n\n" 
+ "Maximum HR was: " + str(maximum_hr) 
+ "\nWas test terminated because exceeding HR " + str(termination))

## Ausgabe einer Zusammenfassung

#%% UC 2.5 Visualisierung der Daten

## Öffnen der Leistungsdaten

# Opening JSON file
folder_input_data = os.path.join(folder_current, 'input_data')
file_name =  os.path.join(folder_input_data, 'power_data_3.txt')
power_data_watts = open(file_name).read().split("\n")
power_data_watts.pop(-1)
len(power_data_watts)


# %%
## Erstellung eines Plots


#peaks['average_HR_10s'].plot()

peaks_downsampled = peaks[peaks.index % 1000 == 0]  

peaks_downsampled = peaks_downsampled.reset_index(drop=True)
peaks_downsampled = peaks_downsampled.drop(["ECG_R_Peaks"],axis=1)



peaks_downsampled["Power (Watt)"] = pd.to_numeric(power_data_watts)
#peaks_downsampled["Power (Watt)"] = peaks_downsampled["Power (Watt)"]
peaks_downsampled.plot()

#peaks_downsampled["Power (Watt)"].plot()

#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums

## Abfrage an Nutzer:in, ob Abgebrochen werden soll

manual_termination = False
manual_termination = input("Is this test invalid? (leave blank if valid): ")

if manual_termination != False:
    termination = True


#%% UC 2.7 Speichern der Daten


# Speichern der Daten
data = {"User ID": subject_data["subject_id"], "Reason for test termation": manual_termination, "Average Heart Rate": average_hr_test, "Maximum Heart Rate": subject_max_hr, "Test Length (s)": len(power_data_watts), "Test Power (W)": subject_data["test_power_w"], "Average Power": peaks_downsampled["Power (Watt)"].mean()}

json_data_to_save = json.dumps(data)

folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'result_data')
results_file = os.path.join(folder_input_data, 'data.json')

with open(results_file, 'w', encoding='utf-8') as f:
    json.dump(json_data_to_save, f, ensure_ascii=False, indent=4)
# %%
