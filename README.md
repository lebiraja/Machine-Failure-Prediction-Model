# Machine Failure Prediction Model

## Overview
This project is a **Machine Failure Prediction Model** designed to analyze operational conditions and predict potential failures in an industrial setting. Using **Machine Learning**, this model processes sensor data to forecast **machine failures** and assist in **predictive maintenance** and **quality control**.

## Dataset
The model is trained on a dataset that contains sensor readings and machine parameters. The dataset includes the following features:

| Column Name          | Description |
|----------------------|-------------|
| **Unique ID**        | Unique identifier for each machine instance |
| **Product ID**       | ID of the manufactured product |
| **Quality**          | Quality rating of the product (L = Low, M = Medium, H = High) |
| **Ambient T (°C)**   | Environmental temperature around the machine |
| **Process T (°C)**   | Internal machine temperature while operating |
| **Rotation Speed (RPM)** | Speed at which the machine is running |
| **Torque (Nm)**      | Rotational force applied to machine components |
| **Tool Wear (min)**  | Duration (in minutes) the tool has been in use |
| **Machine Status**   | Status of the machine (0 = Normal, 1 = Failure) |

## Model Performance
The model was trained using **imbalanced learning techniques** to handle cases where failures are rare. The key performance metrics are:
- **Accuracy:** 99%
- **Precision, Recall, F1-score:** Consistently high across classes

## Usage
To use this model:
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/machine-failure-prediction.git
   cd machine-failure-prediction
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the model:
   ```sh
   python model.py
   ```
4. Enter custom input values when prompted:
   ```
   Enter Ambient Temperature (C): 68
   Enter Process Temperature (C): 56
   Enter Rotation Speed (rpm): 7000
   Enter Torque (Nm): 87
   Enter Tool Wear (min): 3
   ```
5. The model will predict whether the machine is likely to fail (`1`) or run normally (`0`).

## Dependencies
- Python 3.12
- Pandas
- NumPy
- Scikit-Learn
- Imbalanced-learn

## Applications
- **Predictive Maintenance**: Reduces downtime by predicting failures early.
- **Quality Control**: Identifies manufacturing conditions affecting product quality.
- **Cost Reduction**: Optimizes machine operations and minimizes maintenance costs.

## Contributing
Feel free to contribute to this project! Fork the repo, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

