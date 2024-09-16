# AccuKnox_Assignment
# Django Signals & Custom Classes - Assessment Project

This project is developed as part of the Django Trainee assessment, demonstrating how Django signals work and implementing a custom Python class. The project contains two major components:
1. **Django Signals**: Explores how Django signals behave in terms of synchronous/asynchronous execution, threading, and database transactions.
2. **Custom Python Classes**: Implements a `Rectangle` class in Python that can be iterated over, yielding its length and width.

---

## Table of Contents

- [Django Signals](#django-signals)
  - [Signals Overview](#signals-overview)
  - [Project Structure](#project-structure)
  - [How to Run the Django Project](#how-to-run-the-django-project)
  - [Expected Behavior](#expected-behavior)
- [Custom Python Class](#custom-python-class)
  - [Class Overview](#class-overview)
  - [How to Run the Class Test](#how-to-run-the-class-test)
  - [Expected Output](#expected-output)
- [Conclusion](#conclusion)

---

## Django Signals

### Signals Overview

The Django signals component demonstrates the following:
1. **Synchronous vs. Asynchronous Execution**: Are signals executed synchronously by default?
2. **Thread Execution**: Do signals run in the same thread as the caller?
3. **Database Transaction Handling**: Do signals execute within the same database transaction?

Each signal is registered with the `post_save` event of the `User` model in Django.



Here’s a proper README.md file tailored for your project that includes both Django Signals and Custom Python Classes sections. This version is structured and detailed, suitable for a GitHub repository.

markdown
Copy code
# Django Signals & Custom Classes - Assessment Project

This project is developed as part of the Django Trainee assessment, demonstrating how Django signals work and implementing a custom Python class. The project contains two major components:
1. **Django Signals**: Explores how Django signals behave in terms of synchronous/asynchronous execution, threading, and database transactions.
2. **Custom Python Classes**: Implements a `Rectangle` class in Python that can be iterated over, yielding its length and width.

---

## Table of Contents

- [Django Signals](#django-signals)
  - [Signals Overview](#signals-overview)
  - [Project Structure](#project-structure)
  - [How to Run the Django Project](#how-to-run-the-django-project)
  - [Expected Behavior](#expected-behavior)
- [Custom Python Class](#custom-python-class)
  - [Class Overview](#class-overview)
  - [How to Run the Class Test](#how-to-run-the-class-test)
  - [Expected Output](#expected-output)
- [Conclusion](#conclusion)

---

## Django Signals

### Signals Overview

The Django signals component demonstrates the following:
1. **Synchronous vs. Asynchronous Execution**: Are signals executed synchronously by default?
2. **Thread Execution**: Do signals run in the same thread as the caller?
3. **Database Transaction Handling**: Do signals execute within the same database transaction?

Each signal is registered with the `post_save` event of the `User` model in Django.

#How to Run the Django Project
Clone the repository:

#bash
Copy code
git clone <repository-url>
cd signal_project
Create a virtual environment and install dependencies:

#bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt  # Ensure Django is in requirements.txt
Apply migrations and run the Django development server:

bash
Copy code
python manage.py migrate
python manage.py runserver
Testing Signals:

O#pen the Django shell:
bash
Copy code
python manage.py shell
#reate a user to trigger the post_save signal:
python
Copy code
from django.contrib.auth.models import User
User.objects.create(username="testuser")
Expected Behavior
Synchronous Execution: When a User is created, the signal will start and finish in a synchronous manner.
Thread Execution: The signal runs in the same thread as the caller, and this can be verified by comparing thread IDs.
Transaction Handling: If a transaction is rolled back, any changes made in the signal will also be rolled back.
Custom Python Class
Class Overview
The custom Python class implements a Rectangle with the following features:

The class is initialized with length and width.
The class is iterable, yielding first the length and then the width when iterated over.
Project Structure
bash
Copy code
rectangle_project/
│
├── rectangle.py              # Python file containing the Rectangle class
└── test_rectangle.py         # Test script for the Rectangle class
How to Run the Class Test
Navigate to the project directory:

bash
Copy code
cd rectangle_project
Run the test script:

bash
Copy code
python test_rectangle.py
Expected Output
When the Rectangle class is iterated over, the output should look like this:

bash
Copy code
{'length': 5}
{'width': 3}
The class behaves as expected by yielding the dimensions in sequence.

Conclusion
This project demonstrates fundamental concepts in Django signals and Python class design. The signals are shown to execute synchronously, run in the same thread as the caller, and respect database transactions. The custom Python class is designed to be iterable and returns the expected dimensions.

Feel free to fork, clone, or contribute to this repository.

markdown
Copy code

---

### Key Points of this `README.md`:

- **Overview**: Provides a clear summary of both parts of the project.
- **Table of Contents**: Helps navigate through the `README` file.
- **Project Structure**: Describes how the files are organized in both Django and Python class parts.
- **Step-by-Step Instructions**: Explains how to set up and run both the Django project and the custom Python class.
- **Expected Behavior/Output**: Clearly states what output or behavior the user should expect after running the code.
- **Conclusion**: Wraps up the `README` with a brief recap of what the project demonstrates.

This structure will help others quickly understand your project and run it successfully!


