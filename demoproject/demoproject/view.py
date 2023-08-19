#created
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume - A. A Sakib</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .header {
            text-align: center;
        }

        .name {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .job-title {
            font-size: 24px;
            color: #007bff;
            margin-bottom: 20px;
        }

        .section {
            margin-bottom: 30px;
        }

        .section h2 {
            font-size: 24px;
            margin-bottom: 10px;
        }

        .section p {
            font-size: 16px;
            line-height: 1.5;
        }

        /* Style for the Education section */
        .education {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="name">A. A Sakib</div>
            <div class="job-title">Software Business Analyst</div>
        </div>

        <div class="section">
            <h2>Summary</h2>
            <p>Dynamic and results-oriented Software Business Analyst with over 1 year of experience in analyzing, designing, and delivering user-focused software solutions. Proficient in driving projects from inception to timely completion while maintaining a keen focus on quality and effectiveness.</p>
        </div>

        <div class="section">
            <h2>Experience</h2>
            <p><strong>Software Business Analyst</strong><br>
            2023 - Present<br>
            Devwloper Experience Hub, Rajshahi, Bangladesh</p>

            <ul>
                <li>Lead in the development, and implementation of the project, layout, and production communication materials.</li>
                <li>Delegate tasks to the 7 members of the development team and provide counsel on all aspects of the project.</li>
                <li>Supervise the assessment of all software materials in order to ensure quality and accuracy of the product.</li>
                <li>Oversee the efficient use of production project budgets ranging from $2,000 - $25,000.</li>
            </ul>
        </div>

        <div class="section">
            <h2>Education</h2>
            <div class="education">
                <p><strong>M. Engineering of & Computer Science and Engineering</strong><br>
                2023 - Ongoing<br>
                University of Rajshahi, Rajshahi, Bangladesh</p>
                
                <p><strong>B.Sc. Engineering of & Computer Science and Engineering</strong><br>
                2018 - 2023<br>
                Bangladesh Army University of Science and Technology, Saidpur cantonment, Nilphamari</p>
            </div>
        </div>
    </div>
</body>
</html>

    """)
