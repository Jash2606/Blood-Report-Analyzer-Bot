from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from crewai import Crew, Process
from agents import blood_report_analyst, researcher
from tasks import report_analyze_task, research_task
import logging
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def read_file_with_fallback(primary_path, fallback_path, min_word_count=100):
    try:
        with open(primary_path, 'r') as f:
            content = f.read()
        
        if len(content.split()) < min_word_count:  
            logging.info(f"Primary file {primary_path} has less than {min_word_count} words, switching to fallback file {fallback_path}.")
            with open(fallback_path, 'r') as f:
                content = f.read()
        
        return content
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return ""

@app.route('/analyze', methods=['POST'])

def analyze_report():
    try:
        if 'blood_report' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['blood_report']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            crew = Crew(
                agents=[blood_report_analyst, researcher],
                tasks=[report_analyze_task, research_task],
                process=Process.sequential,
                verbose=True
            )

            result = crew.kickoff(inputs={'blood_report': file_path})
            
            # Read the output files with fallback logic
            analysis = read_file_with_fallback('blood_report_summary12.md', 'blood_report_summary11.md')
            recommendations = read_file_with_fallback('blood_report_recommendations12.md', 'blood_report_recommendations11.md')

            # Clean up the uploaded file
            os.remove(file_path)

            return jsonify({
                'analysis': analysis,
                'recommendations': recommendations
            })
    except Exception as e:
        logging.error(f"An error occurred during report analysis: {e}")
        return jsonify({'error': 'An internal error occurred.'}), 500


if __name__ == '__main__':
    app.run(debug=True)