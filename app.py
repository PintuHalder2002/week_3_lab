import jinja2
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


#
df = pd.read_csv('data.csv')
    
data = df.to_dict(orient = "records")


student=[]
for x in data:
    student.append(str(x["Student id"]))


course=[]
for x in data:
    course.append(str(x["Course id"]))
    

marks=[]
for x in data:
    marks.append(x["Marks"])


# print(marks) # print(data[5]) # print(type(data[5])) # print(len(data))



def student_course_sum(Student_id):
    sum = 0
    for i in data:
        if str(i["Student id"]) == Student_id:
            sum += i["Marks"]
            
            
    html_content = f"""
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>students Data</title>
    </head>
    <body>
    <h1>Student Details</h1>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr>
                <th>Student id</th>
                <th>Course id</th>
                <th>Marks</th>
            </tr>

            <tr>"""
            

            
    for i in data :
        if str(i["Student id"]) == Student_id :
            html_content += f"""
            <tr>
                <td>{i['Student id']}</td>
                <td>{i['Course id']}</td>
                <td>{i['Marks']}</td>
            <tr>
            """
                        
               
    html_content += f""" 
        <tr>
            <td colspan="2">Total Marks</td>
            <td>{sum}</td>
        </tr>      
        </table>
    </body>
    </html>"""
    
    with open('output.html','w') as f:
        f.write(html_content)   
    
    return html_content



def course_average_max(Course_id):
    course_sum = 0
    count = 0
    for i in data:
        if str(i["Course id"]) == Course_id:
            count+=1
            course_sum += i["Marks"]
    average_marks = course_sum/count
    
    list_marks=[]
    for i in data:
        if str(i["Course id"]) == Course_id:
            list_marks.append(i["Marks"])
    
    maxi = list_marks[0]
    for i in range(len(list_marks)):
        if list_marks[i] >= maxi :
            maxi = list_marks[i]
    
    html_content = f"""
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Course Data</title>
    </head>
    <body>
    <h1>Course Details</h1>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr>
                <th>Average marks</th>
                <th>Maximum Marks</th>
            </tr>

            <tr>
                <td>{average_marks}</td>
                <td>{maxi}</td>    
            </tr>
     
        </table>
    <img src="/histogram.png" alt="histogram"/>
    </body>
    </html>"""
    
    generate_histogram(df)
            
    return html_content


Marks = df["Marks"]
mean = Marks.mean()


def generate_histogram(df):
    #Generate and save a histogram of the marks.
    plt.figure(figsize=(8, 6))
    plt.hist(df['Marks'], bins=5, edgecolor='black')
    
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig('histogram.png')
    plt.close()


generate_error_html="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Something Went Wrong</title>
    </head>
    <body>
        <h1>Wrong Inputs</h1>
        <p>Something went wrong</p>
    </body>
    </html>
    """



def main():
    
    if sys.argv[1] not in ["-s","-c"] :
        with open("output.html","w") as f :
            f.write(generate_error_html)

    if len(sys.argv) == 3 and sys.argv[1] == "-s" and sys.argv[2] in student :
        Student_id = sys.argv[2]
        with open("output.html","w") as f :
            f.write(student_course_sum(Student_id))
    #it will generate the output.html file in file section   not in the console......   


    elif len(sys.argv) == 3 and sys.argv[1] == "-s" and sys.argv[2] not in student :   
        with open("output.html","w") as f :
            f.write(generate_error_html)

        
    elif len(sys.argv) == 3 and sys.argv[1] == "-c" and sys.argv[2] in course :
        Course_id = sys.argv[2]
        with open("output.html","w") as f :
            f.write(course_average_max(Course_id))
        
        
        
    elif len(sys.argv) == 3 and sys.argv[1] == "-c" and sys.argv[2] not in course :  
        with open("output.html","w") as f :
            f.write(generate_error_html)
    
    


if __name__ == "__main__":
    main()
