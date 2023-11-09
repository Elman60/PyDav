import pandas as pd

df = pd.read_csv('survey_results_public.csv') #ჩავტვირთეთ CSV ფაილი

selected_columns = ['YearsCode', 'RemoteWork', 'CompTotal'] #ვირჩევთ სასურველ სტრიქონებს და სვეტებს
selected_rows = df[(df['RemoteWork'] == 'Remote') & (df['ResponseId'] < 40)]

selected_rows.set_index('ResponseId', inplace=True) #ერთი სვეტის მიხედვით ვაკეთებთ ინდექსაციას

table = selected_rows[selected_columns]

print(table)

sorted_table = selected_rows.sort_values(by=['Age', 'Employment']) #ორი პარამეტრით ვასორტირებთ ცხრილს

print(sorted_table)

#ვიყენებთ სტატისტიკურ ფუნქციებს
mean_value = sorted_table['ConvertedCompYearly'].mean()
std_dev = sorted_table['ConvertedCompYearly'].std()
median_value = sorted_table['ConvertedCompYearly'].median()
min_value = sorted_table['ConvertedCompYearly'].min()
max_value = sorted_table['ConvertedCompYearly'].max()

print(f"Mean: {mean_value}")
print(f"Standard Deviation: {std_dev}")
print(f"Median: {median_value}")
print(f"Min: {min_value}")
print(f"Max: {max_value}")






