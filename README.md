

# **Machine-Failure-Prediction-Model**  

This project is a machine learning model that predicts **machine status** in a factory setting based on various sensor data. The model processes real-time input such as **temperature, speed, torque, and tool wear** to determine whether a machine is functioning properly or failing.  

## **Dataset**  
The dataset used in this project is stored in **`factory_data (classification).csv`**, which contains sensor readings and machine status.  

### **Columns in the dataset:**  
1. **Unique ID** - A unique identifier for each data entry (dropped for modeling).  
2. **Product ID** - Identifier for the product being processed (dropped for modeling).  
3. **Quality** - Categorical variable representing product quality (Low, Medium, High).  
4. **Ambient T (C)** - Ambient temperature in degrees Celsius.  
5. **Process T (C)** - Process temperature in degrees Celsius.  
6. **Rotation Speed (rpm)** - Speed of the machine in revolutions per minute.  
7. **Torque (Nm)** - Torque applied by the machine in Newton-meters.  
8. **Tool Wear (min)** - Duration for which the tool has been used (in minutes).  
9. **Machine Status** - **Target variable** indicating machine health (0 = Normal, 1 = Failure).  

---

## **Project Files**  

- **`mod.py`** → Main Python script that trains the model and allows user input.  
- **`factory_data (classification).csv`** → Dataset containing factory sensor readings and machine status.  
- **`README.md`** → This file, describing the project.  
- **`requirements.txt`** → List of required Python libraries for running the model.  

---

## **Model Overview**  

The model uses **Logistic Regression** for binary classification. It takes machine sensor inputs, scales them, and predicts whether a machine is **operational (0) or failing (1)**.  

### **Steps in Model Training:**  
1. Load and clean the dataset (handle missing values, drop unnecessary columns).  
2. Encode categorical features (convert product quality into numerical values).  
3. Standardize numerical features using **StandardScaler**.  
4. Split the data into training and testing sets.  
5. Train a **Logistic Regression** model.  
6. Evaluate the model using **accuracy score and classification report**.  

---

## **How to Use**  

### **1️⃣ Install Dependencies**  
Run the following command to install required libraries:  
```bash
pip install -r requirements.txt
```  

### **2️⃣ Run the Model**  
Run the script and enter custom inputs when prompted:  
```bash
python mod.py
```  

### **3️⃣ Input Features**  
When prompted, enter values for the following:  
- **Ambient Temperature (°C)**  
- **Process Temperature (°C)**  
- **Rotation Speed (rpm)**  
- **Torque (Nm)**  
- **Tool Wear (min)**  

### **4️⃣ Get Predictions**  
The model will output **0 (Normal) or 1 (Failure)** based on the input data.  

---

## **Example Run**  
```bash
Enter Ambient Temperature (C): 24.5
Enter Process Temperature (C): 36.0
Enter Rotation Speed (rpm): 1400
Enter Torque (Nm): 45.0
Enter Tool Wear (min): 20
```
**Output:**  
```
Predicted Machine Status: Normal (0)
```
or  
```
Predicted Machine Status: Failure (1)
```

---

## **Improvements & Future Enhancements**  
✔️ Implement other classification models (e.g., Random Forest, SVM).  
✔️ Improve feature engineering for better accuracy.  
✔️ Deploy the model as a web application.  

---

## **Contributing**  
Feel free to contribute by improving the model, dataset, or adding new features.  

Happy coding! 🚀  

---
