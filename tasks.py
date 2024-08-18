from crewai import Task
from tools import search_tool, PDFSearchTool
from agents import blood_report_analyst, researcher

report_analyze_task = Task(
    description=(
        "Thoroughly analyze the provided {blood_report}. Focus on all key parameters, biomarkers, and potential health issues. "
        "For each parameter, explain its significance, normal range, and any deviations observed. "
        "Summarize the potential health implications, making sure to explain each in an accessible manner."
    ),
    expected_output=(
        "The output should be a comprehensive and structured summary that includes:\n"
        "1. **Introduction**: Brief overview of the report.\n"
        "2. **Key Parameters**: Detailed analysis of each parameter, including normal ranges and explanations.\n"
        "3. **Abnormal Findings**: Specific sections highlighting any abnormalities with detailed descriptions.\n"
        "4. **Health Implications**: Explanation of potential health issues based on the findings.\n"
        "5. **Critical Alerts**: Identification of any critical issues that need immediate attention.\n"
        "The final report should be professional, clear, and accessible to non-experts."
    ),
    tools=[PDFSearchTool],
    agent=blood_report_analyst,
    output_file='blood_report_summary12.md'
)

research_task = Task(
    description=(
        "Conduct thorough research based on the {blood_report} analysis to provide targeted health recommendations and relevant resources. "
        "The research should be comprehensive, evidence-based, and directly related to the critical health issues identified in the blood report.\n"
        "Steps to follow:\n"
        "1. Carefully review the blood report summary to identify the most critical health issues and abnormalities.\n"
        "2. For each identified issue, research and compile a list of specific, actionable health recommendations that address these issues.\n"
        "3. Locate credible, peer-reviewed articles, medical guidelines, or authoritative resources that support each recommendation.\n"
        "4. Summarize each resource, explaining its content, relevance, and how it supports the recommendation based on the blood report findings.\n"
        "5. Ensure all recommendations are practical and easy for the patient to implement."
    ),
    expected_output=(
        "The final output should be a detailed, well-structured report that includes:\n"
        "1. **Critical Health Issues**: A list of key health issues identified from the blood report, with a brief explanation for each.\n"
        "2. **Health Recommendations**: Specific, evidence-based health recommendations for each issue, presented in a clear, actionable format.\n"
        "3. **Supporting Resources**: For each recommendation, provide 1-3 high-quality, credible resources, including:\n"
        "   - A direct link to the article or resource\n"
        "   - A concise summary of the article’s content\n"
        "   - An explanation of the article’s relevance to the patient’s blood report findings and the corresponding recommendation\n"
        "4. **Conclusion**: A final summary highlighting the key actions the patient should prioritize based on the research findings."
    ),
    agent=researcher,
    tools=[PDFSearchTool, search_tool],
    output_file='blood_report_recommendations12.md'
)
