import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('survey_results_public.csv')

#ამოვიღღეთ ასაკის და ხელფასის სვეტები
age = data['Age'].values
salary = data['ConvertedCompYearly'].values

#ვუწერთ პირველ დიაგრამას პარამეტრებს
plt.figure(figsize=(8, 6))
plt.scatter(age, salary, color='blue', alpha=0.5)
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')

plt.show()

#ვუწერთ მეორე დიაგრამას პარამეტრებს
plt.figure(figsize=(8, 6))
plt.hist(age, bins=20, color='red', edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.show()

