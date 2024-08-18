# Blood Report analysis using crewAI
This project leverages CrewAI to analyze blood reports, search the web according to the report summary, and provide recommendations to the patient along with relevant links to articles. It includes a backend server for processing and a front-end interface for easy access.

## Approach


To tackle this AI Internship Assignment, I followed these steps:


1. **Understanding the Task**: 
   Broke down the assignment into main parts: reading the report, analyzing it, researching health info, and making recommendations.

2. **Framework Setup**: 
   Used the CrewAI framework as required. Learned how it works through documentation and tutorials.

3. **Creating AI Helpers**: 
   Made two AI agents:
   - One to understand blood test results
   - Another to search for health articles

4. **Defining Jobs**: 
   Set up two main tasks:
   - Analyzing the blood report
   - Researching health info and making recommendations



5. **Work-flow**

    1. **PDF Reading**: Extracts text from blood test reports using PyPDF2.
    2. **Web Search**: Uses SerperDevTool for internet searches related to the report findings.
    3. **Input Handling**: A Flask server manages file uploads for the blood test reports.
    4. **Report Analysis**: Utilizes Google Gemini to summarize key points from the report.
    5. **Research**: Searches for relevant health articles based on the report summary.
    6. **Recommendations**: Combines analysis and research to provide health advice.
    7. **Result Delivery**: The server returns the analysis and recommendations as a JSON response to the client.


6. **Error Handling**: 
    
   - I implemented error handling throughout the process to manage potential issues like file reading errors or processing failures.
   - A fallback mechanism was added to ensure that even if the latest output files are not available, the system can still provide useful information from previous runs.

7. **Testing and Improving**: 
    Repeatedly tested the system and made improvements to make it work better.

This approach allowed me to create a comprehensive system that takes a blood test report as input, analyzes it, performs relevant research, and provides health recommendations, all while leveraging the power of the CrewAI framework.

 ## Front-End Interface

A user-friendly front-end interface is available to interact with the system: [Blood Report Analysis Front-End](https://wingify-frontend.vercel.app/).

This interface allows users to upload blood reports and receive analysis and recommendations directly from the web.
## 
The project has the following structure:

- `server`: Contains the backend server code.
- `agents`: Contains the agents responsible for different parts of the analysis.
- `tools`: Contains the tools for web scraping, PDF processing, and more.
- `tasks`: Contains tasks to be performed by the agents.
- `crew`: Contains the main CrewAI configuration and setup files.
- `requirement.txt`: Lists all the dependencies required for the project.

## Setup Instructions

### 1. Create the Environment

First, create a virtual environment for the project. This helps to manage dependencies and keep the project isolated from other projects on your system.

### 2. Download all the dependencies
```pip install -r requirement.txt```

### 3. Setup the Environment variables
```GOOGLE_API_KEY```,
```EXA_API_KEY```

### 4. Run the project
```python -m waitress --host=0.0.0.0 --port=5000 server:app.py``` 




