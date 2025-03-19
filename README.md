

---

# **Machine-Failure-Prediction-Model**  

This project is a machine learning model that predicts **machine status** in a factory setting based on various sensor data. The model processes real-time input such as **temperature, speed, torque, and tool wear** to determine whether a machine is functioning properly or failing.  

---

## **Dataset**  

The dataset used in this project is stored in **`factory_data (classification).csv`**, which contains sensor readings and machine status.  

### **Columns in the dataset:**  
| Feature Name          | Description |
|----------------------|-------------|
| **Unique ID**        | Unique identifier for each entry (dropped for modeling). |
| **Product ID**       | Identifier for the product being processed (dropped for modeling). |
| **Quality**          | Product quality (Low, Medium, High). |
| **Ambient T (C)**    | Ambient temperature in degrees Celsius. |
| **Process T (C)**    | Process temperature in degrees Celsius. |
| **Rotation Speed (rpm)** | Speed of the machine in revolutions per minute. |
| **Torque (Nm)**      | Torque applied by the machine in Newton-meters. |
| **Tool Wear (min)**  | Duration the tool has been used (in minutes). |
| **Machine Status**   | **Target variable:** (0 = Normal, 1 = Failure). |

---

## **📂 Project Files**  

- **`mod.py`** → Main Python script that trains the model and allows user input.  
- **`factory_data (classification).csv`** → Dataset containing factory sensor readings and machine status.  
- **`requirements.txt`** → List of required Python libraries for running the model.  
- **`README.md`** → This file, describing the project.  

---

## **🛠 Model Overview**  

The model uses **Logistic Regression** for binary classification. It takes machine sensor inputs, scales them, and predicts whether a machine is **operational (0) or failing (1)**.  

### **🔹 Steps in Model Training:**  
1️⃣ Load and clean the dataset (handle missing values, drop unnecessary columns).  
2️⃣ Encode categorical features (convert product quality into numerical values).  
3️⃣ Standardize numerical features using **StandardScaler**.  
4️⃣ Split the data into training and testing sets.  
5️⃣ Train a **Logistic Regression** model.  
6️⃣ Evaluate the model using **accuracy score and classification report**.  

---

## **🚀 Usage**  

To use this model:  

### **1️⃣ Clone this repository**  
```sh
git clone https://github.com/yourusername/machine-failure-prediction.git
cd machine-failure-prediction
```

### **2️⃣ Install dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the model**  
```sh
python mod.py
```  

### **4️⃣ Input Features**  
When prompted, enter values for the following:  
- **Ambient Temperature (°C)**  
- **Process Temperature (°C)**  
- **Rotation Speed (rpm)**  
- **Torque (Nm)**  
- **Tool Wear (min)**  

### **5️⃣ Get Predictions**  
The model will output **0 (Normal) or 1 (Failure)** based on the input data.  

---

## **📌 Example Run**  
```sh
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

## **🔧 Future Improvements**  
✔️ Implement other classification models (e.g., **Random Forest, SVM**).  
✔️ Improve feature engineering for better accuracy.  
✔️ Deploy the model as a **web application** with a dashboard.  

---

## **🤝 Contributing**  
Feel free to contribute by improving the model, dataset, or adding new features.  

Happy coding! 🚀  

---
