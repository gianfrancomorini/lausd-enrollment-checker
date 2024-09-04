LAUSD Enrollment Checker
<!-- Optional banner image, replace with a real link if available -->

A user-friendly tool to help parents easily check when their child is eligible for enrollment in Los Angeles Unified School District (LAUSD) programs based on their birth date.

Key Features ✨
🏫 LAUSD Enrollment Programs: Get personalized information on which LAUSD programs are available based on your child’s birth date.
⏳ Quick and Easy: Input your child’s birthday, and the tool will instantly tell you which programs are open for them.
🔍 Accurate Data: Using up-to-date LAUSD guidelines to ensure accurate results.
📱 Mobile Friendly: Fully responsive for easy use on any device.
How It Works 🚀
Input your child’s birth date into the simple form.
Receive a list of programs and dates they are eligible for based on LAUSD enrollment criteria.
Explore the recommended programs and plan ahead!
Getting Started 🛠️
1. Clone the Repository 📂
bash
Copy code
git clone https://github.com/gianfrancomorini/lausd-enrollment-checker.git
cd lausd-enrollment-checker
2. Set Up Your Virtual Environment 🐍
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
3. Install Dependencies 📦
bash
Copy code
pip install -r requirements.txt
4. Create a .env File 📝
Create a .env file in the root directory with the following:

bash
Copy code
FLASK_ENV=development
SECRET_KEY=your-secret-key
5. Run the Application ▶️
bash
Copy code
python app.py
Now, you can access the application at http://127.0.0.1:5000.

API Endpoints 🔗
1. Check Enrollment Programs /check-enrollment
Method: POST
Content-Type: application/json
Body Parameters:
birthday: Child's birth date (string in YYYY-MM-DD format)
Example Request:

json
Copy code
{
  "birthday": "2019-05-22"
}
Example Response:

json
Copy code
{
  "programs": [
    "Kindergarten (August 2024)",
    "Pre-Kindergarten (August 2023)"
  ]
}
Built With 🛠️
Flask: Lightweight web framework for Python
Python: Core language used
dotenv: For environment variable management
HTML5/CSS3: For the front-end
Future Improvements 🌟
Add more detailed information about each enrollment program.
Implement multi-language support for broader accessibility.
Add a notification system to remind parents of upcoming enrollment deadlines.
Contributing 🤝
Contributions are welcome! If you’d like to improve this project, feel free to:

Fork this repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add cool feature').
Push to the branch (git push origin feature-branch).
Create a pull request.
License 📄
This project is licensed under the MIT License – see the LICENSE file for details.

Contact 📧
If you have any questions or suggestions, feel free to reach out via email.

Footnote 🌟
This project is not officially associated with the Los Angeles Unified School District (LAUSD) but aims to simplify enrollment date tracking for parents.
