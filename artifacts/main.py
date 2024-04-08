import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

heart_data=pd.read_csv("D:\Data_Science_velocity\AWS\Heart_Failure_Prediction\Dataset\heart_clean_data.csv")

x=heart_data.drop("HeartDisease",axis=1)
y=heart_data["HeartDisease"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=1)
model=LogisticRegression()
model.fit(x_train,y_train)
trining_accuracy=model.predict(x_train)
testing_accuracy=model.predict(x_test)

print("Model Training accuracy", accuracy_score(y_train,trining_accuracy))
print("Model testing accuracy",accuracy_score(y_test,testing_accuracy))

pickle.dump(model,open("heart_model.pkl","wb"))
