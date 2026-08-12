import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#####################################################
# Step 1 : Load the Dataset
#####################################################
Border = "_" * 40

print(Border)
print("Play Predictor using KNN")
print(Border)

# Load the dataset
df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print("Dataset :", df)

#####################################################
# Step 2 : Clean, Prepare and Manipulate Data
#####################################################

# Create Label Encoder Object
WetherEncoder = LabelEncoder()
TemperatreEncoder = LabelEncoder()
PlayEncoder = LabelEncoder()

# Convert string values into numeric values
df["Wether"] = WetherEncoder.fit_transform(df["Wether"])
df["Temperature"] = TemperatreEncoder.fit_transform(df["Temperature"])
df["Play"] = PlayEncoder.fit_transform(df["Play"])

print(Border)
print("Encoded Dataset :")
print(Border)

print(df)

# Separate Feature and Target
X = df[["Wether","Temperature"]]
Y = df["Play"]

#####################################################
# Step 3 : Train the Dataset
#####################################################

# k = 3
model = KNeighborsClassifier(n_neighbors=3)

# Train using complete dataset
model.fit(X,Y)

#####################################################
# Step 4 : Test the data
#####################################################

print(Border)
print("Testing the model")
print(Border)

# Sunny = 1
# Hot = 2

WetherValue = WetherEncoder.transform(["Sunny"])[0]
TemperatureValue = TemperatreEncoder.transform(["Hot"])[0]

TestData = pd.DataFrame([[WetherValue, TemperatureValue]], columns=["Wether", "Temperature"])

Result = model.predict(TestData)

ResultLabel = PlayEncoder.inverse_transform(Result)

print("Wether : Sunny")
print("Teperature : Hot")
print("Prediction :",ResultLabel[0])

#####################################################
# Step 5 : Calculate Accuracy 
#####################################################

print(Border)
print("Accuracy Calculation")
print(Border)

# Divide Dataset into two equal parts
X_train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.5, random_state=42)

# Calculate accuracy for different values of k
for k in range(1,11):
    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_train, Y_Train)

    Y_pred = model.predict(X_Test)

    Accuracy = accuracy_score(Y_Test, Y_pred)

    print(f"k = {k}, Accuracy = {Accuracy*100:.2f}%")