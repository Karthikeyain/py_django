from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    data = '''
    <html> 
        <head> 
            <title>
            WELCOME TO SAMPLE 
            </title>
        </head>
        <body>
            <div> 
            WELCOME TO THE DJANGO ANOTHER NEW CONFUSION OF PYTHON 
            </div>
                <marquee>
                Thank You 
                </marquee>
        </body>
    </html>  '''
    return HttpResponse(data)

def helloworld(request):
    data = "hello world"
    return HttpResponse(data)

def resume(request):
    code = '''
    <html>
    <head>
        <title>
            RESUME KARATHIKEYA
        </title>
         <div >
               <h3>phone:8765434567 </h3> 
                <h3>email:@gmail.com</h3>
            </div>
    </head>
        <body>
        <div>
            <h1> Career Objective: </h1>
            <p> I would like to work with very enthusiastic and effectively do the my job. And I will put my all efforts in the job</p>
        </div>
        <div>
             <h2>Educational Qualifications:</h2>
            <table border =" box">
                <tr>
                    <td> YOP</td>
                    <td> College/Board</td>
                    <td> Branch/Subject/Group</td>
                    <td> Percentage</td>
                </tr>
                <tr>
                    <td> 2023</td>
                    <td> Pallavi EC </td>
                    <td> B.tech CSE</td>
                    <td> 68</td>
                </tr>
                 <tr> 
                    <td> 2019</td>
                    <td> Kakatiya JC</td>
                    <td> INTERMEDIATE MPC </td>
                    <td> 94</td>
                </tr>
                <tr> 
                    <td> 2017</td>
                    <td> ZPHS Chelpur</td>
                    <td> SSC</td>
                    <td> 88</td>
                </tr>
            </table>

        </div>
        </body>
    </html>'''
    return HttpResponse(code)

def opened(request):
    return render(request,'opened.html')
