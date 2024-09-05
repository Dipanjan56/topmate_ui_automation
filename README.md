This is a selenium project using Behave[BDD] Framework using PageObject Model Architecture

To run any feature file locally using behave command:
1. general run [local]-> behave features/login.feature
2. run using tags, url, headless and browser type > behave features/login.feature -D browser=chrome -D headless=true -D url=https://staging2.topmate.io/ --tags=smoke

How to generate Report after execution?

1. We use allure reporting for that
command -> behave features/topmate_login.feature -D url=https://staging2.topmate.io/ -D browser=chrome -D headless=true -f allure_behave.formatter:AllureFormatter -o reports/json_reports/


Now we will try to generate the report
allure generate reports/json_reports -o reports/allure_reports --clean 

Now we will see the report in allure:
command -> allure serve reports

**Project Structure Architecture:**

1. api/

	•	Purpose: This directory contains files related to API automation testing.
	•	Files and Directories:
	•	api_utils/ -> api_requests.py: Includes the code for making API requests (e.g., GET, POST, etc.).
	•	endpoints -> endpoints.py: Holds the API endpoints and routes used in testing.

2. config/

	•	Purpose: Configuration files for the project.
	•	Files:
	•	conf.ini: A configuration file where you store environment-related configurations, URLs, and credentials.

3. features/

	•	Purpose: This directory holds the feature files and the steps related to the UI automation (using BDD/Behavior Driven Development).
	•	Subdirectories:
	•	pageobjects/: multiple pageObjects classes -> Contains page object models (POM), where the web elements and actions are defined.
	•	steps/: page wise steps classes -> Contains the step definitions, i.e., the Python code that corresponds to the feature file steps.
	•	environment.py: A file where environment-specific setup and teardown methods are defined.
	•	Feature Files: *.feature: These are Gherkin-based feature files that describe the test cases in a natural language format.
                                   Each feature file corresponds to different modules like booking, login, video call, webinar, etc.

4. logs/

	•	Purpose: Stores log files for test execution and reporting.

5. test_data/

	•	Purpose: Directory to hold test data like credentials, mock data, etc.
	•	Files:
	•	creds.json: A JSON file containing credentials or test-specific data for mailing purpose of the report.

6. utilities/

	•	Purpose: Helper functions and utility scripts that are reused across the tests.
	•	Files:
	•	configReader.py: A utility to read configurations from files like conf.ini.
	•	log_util.py: Logging utility to manage and create logs.
	•	mail_util.py: used to send email notifications after test completion or failure.
	•	report_util.py: Manages reporting for test cases, either HTML reports or structured logs.
	•	util_helper.py: General utility functions that are used across the project.

7. venv/

	•	Purpose: A virtual environment folder that contains all the dependencies and packages installed for this project. It ensures the environment is isolated and consistent across machines.

8. Miscellaneous Files:

	•	.gitignore: Specifies which files and directories to ignore from version control.
	•	behave.ini: Configuration file for the behave framework (a BDD testing tool for Python).
	•	docker-compose-v3.yml: Docker Compose file for setting up containers to run the tests, probably setting up testing environments (e.g., Selenium Grid, mock services).
	•	Dockerfile: The Dockerfile that builds the image necessary for running the automation suite.
	•	entrypoint_ui_automation.sh: Shell script to define the entry point to run the tests inside the Docker container.
	•	README.md: Documentation for setting up and running the project.
	•	requirements.txt: Lists all the Python dependencies required for the project (like Behave, Selenium, Requests, etc.).
	•	test_login.py: Python file for the test case related to the login functionality.

Summary

This project architecture represents an automated testing framework for UI and API testing using BDD methodology (with Behave or similar tools), and it leverages Docker for environment setup. The modular structure ensures scalability, maintainability, and reusability, while utilities like logging, reporting, and configuration management enhance the robustness of the framework.

Would you like to dive deeper into any particular part of this architecture, or should we go ahead with more detailed implementation guidance?
