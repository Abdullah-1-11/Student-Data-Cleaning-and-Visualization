#libraries
import pandas as pd
import matplotlib.pyplot as plt

#read file
data=pd.read_excel("Final Cleaned Data.xlsx")
#top three students graph
plt.subplot(1,2,1)
top_three=data.sort_values(by="marks",ascending=False).head(3)
top_three_students_names=top_three["name"]
top_three_students=top_three["marks"]
plt.bar(top_three_students_names,top_three_students)
plt.title("Top 3 students")
plt.xlabel("Students Name")
plt.ylabel("Marks of students")

#percentage of fee paid students
plt.subplot(1,2,2)
fee_paid=(data["fees_paid"]=="Yes").sum()
not_fee_paid=(data["fees_paid"]=="No").sum()
plt.pie([fee_paid,not_fee_paid],labels=["Paid","Not paid"],autopct="%1.1f%%")
plt.title("Percentage of fee paid students ")
plt.tight_layout()
plt.show()