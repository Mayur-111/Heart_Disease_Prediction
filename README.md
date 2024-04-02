# Heart Disease Prediction Web Application

This is a simple web application built using Flask that predicts the likelihood of heart disease based on demographic and health data provided by the user. 
The prediction is made using a logistic regression model trained on heart health data.

## Getting Started

To run this application locally, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```
    python app.py
    ```
5. Open your web browser and go to http://localhost:5000 to access the application.

## Usage

1. Once you access the application in your web browser, you will see a form where you can enter the following information:
   - Age (in years)
   - Resting Blood Pressure (in mm Hg)
   - Cholesterol level (in mm/dl)
   - Maximum Heart Rate Achieved
   - ST Depression (Oldpeak)
2. Enter the values in the respective input fields and click the "Predict" button.
3. The application will then display whether the user is predicted to have heart disease or not based on the input values.

## File Structure

- `app.py`: Flask application containing the routes and logic for the web application.
- `frontend_page.html`: HTML template for the user interface of the web application.
- `heart_disease_prediction_model.py`: Python script containing the code for model training and pickling.
- `heart_model.pkl`: Pickle file containing the trained logistic regression model.
- `requirements.txt`: List of Python dependencies required to run the application.

## Technologies Used

- Python
- Flask
- HTML/CSS
- Scikit-learn
