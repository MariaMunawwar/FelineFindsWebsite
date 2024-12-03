# FelineFinds 🐱

FelineFinds is a web-based platform for cat lovers, offering features like browsing and purchasing cats, accessories, and connecting with veterinarians. The platform also integrates a machine learning model for predicting cat illnesses based on symptoms.

## Project Structure

- **FelineFinds**: Contains the HTML, PHP, and assets for the website.
- **FelineProject**: Contains the machine learning model and its dependencies.

## URLs for FelineFinds

- **Main Application**: [http://localhost/felinefinds/main.html](http://localhost/felinefinds/main.html)
- **Database Access (phpMyAdmin)**: [http://localhost/phpmyadmin/index.php](http://localhost/phpmyadmin/index.php)

## Requirements

### Web Part (FelineFinds)
- **XAMPP** (for Apache server and MySQL database)
- Web browser (to access the website)

### Machine Learning Part (FelineProject)
- **Python 3.x**
- **Virtual Environment**
- **Flask** and other dependencies (via `requirements.txt`)

## Installation Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/MariaMunawwar/FelineFindsWebsite.git
cd FelineFindsWebsite
```
### Step 2: Set Up the Web Part (FelineFinds)

1. **Install XAMPP**: Download and install [XAMPP](https://www.apachefriends.org/index.html).

2. **Start XAMPP**: Open **XAMPP Manager OSX**, and ensure that both the **Apache** and **MySQL** servers are running.

   - To access XAMPP:
     - **Apache**: Used to serve the web pages.
     - **MySQL**: Used to manage the database for FelineFinds.

3. **Copy FelineFinds to XAMPP's `htdocs` folder**:
   
   Move the contents of the **felinefinds** folder to your XAMPP `htdocs` directory:

   ```bash
   cp -r felinefinds /Applications/XAMPP/htdocs/
   ```
4. Set Up the Database:
- Go to [phpMyAdmin](http://localhost/phpmyadmin/index.php).
- Create a new database called Felinefinds.
- Import the provided SQL file to set up the necessary tables and data.

### Step 3: Set Up the Machine Learning Model (FelineProject)

1. **Navigate to the Machine Learning Project**:

   ```bash
   cd FelineProject
    ```
2. **Create a Virtual Environment**:

 ```bash
python3 -m venv myenv
source myenv/bin/activate
  ```
3. **Install Dependencies**:
Install the dependencies required for the machine learning model by running:

 ```bash
pip install -r requirements.txt
  ```

5. **Run the Flask Server**:
Start the Flask server to run the machine learning model API:

 ```bash
python app.py
  ```

## Usage Instructions

### Web Part (felinefinds)
- Use the navigation bar to explore the website.
- Cats: Browse available cats.
- Accessories: Explore cat toys, clothes, and food.
- Vets: Find and connect with veterinarians.
- Meow Medic: Upload symptoms to get a prediction from the machine learning model about potential illnesses.

### Machine Learning Part (FelineProject)
- The model is integrated into the Meow Medic section of the website. When you upload symptoms, the web application will send a request to the model running on Flask, and you will receive a prediction on potential cat illnesses.

## Additional Notes
- Ensure that both the XAMPP servers and Flask server are running simultaneously for the full functionality of the system (web and machine learning parts).
- If you encounter any database issues, double-check the MySQL setup in phpMyAdmin to ensure the tables have been imported correctly.

