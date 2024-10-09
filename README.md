\# Assignment Submission Portal - Backend

\## Table of Contents

\- \[Introduction\](#introduction)

\- \[Features\](#features)

\- \[Technologies Used\](#technologies-used)

\- \[Setup and Installation\](#setup-and-installation)

\- \[API Endpoints\](#api-endpoints)

\- \[Sample JSON Data\](#sample-json-data)

\- \[Testing the Application\](#testing-the-application)

\- \[Contributing\](#contributing)

\- \[License\](#license)

\## Introduction

The \*\*Assignment Submission Portal\*\* is a backend application designed to facilitate the submission and management of assignments for users and administrators. Users can upload assignments, and administrators can review, accept, or reject them. This project aims to provide a structured and efficient way to handle assignment submissions in educational or organizational settings.

\## Features

\- \*\*User Registration & Login\*\*: Users can register and log in to the system.

\- \*\*Assignment Upload\*\*: Users can upload assignments with relevant details.

\- \*\*Admin Functions\*\*: Administrators can register, log in, and manage assignments.

\- \*\*Assignment Management\*\*: Admins can view, accept, or reject assignments.

\- \*\*Secure Authentication\*\*: Implements token-based authentication to secure endpoints.

\## Technologies Used

\- \*\*Sanic\*\*: A Python web framework for building APIs.

\- \*\*MongoDB\*\*: A NoSQL database for storing user and assignment data.

\- \*\*JWT (JSON Web Tokens)\*\*: For secure user authentication.

\- \*\*Python 3.10\*\*: Programming language used for the backend logic.

\## Setup and Installation

1\. \*\*Clone the Repository\*\*:

\`\`\`bash

git clone https://github.com/your-username/assignment\_submission\_portal.git

cd assignment\_submission\_portal

2\. \*\*Create a Virtual Environment\*\*:

To create a virtual environment, run:

\`\`\`bash

python -m venv venv

3\. \*\*Install Dependencies\*\*:

Once the virtual environment is activated, install the required packages:

pip install -r requirements.txt

4.\*\* Run the Application\*\*

Finally, run the application using:

sanic app

\*\*The API will be available at http://127.0.0.1:8000\*\*

You can test the API using tools like Postman or curl. Ensure that you include the necessary headers, especially for endpoints that require authentication (Bearer token).
