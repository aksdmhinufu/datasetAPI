from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from bs4 import BeautifulSoup
import requests
import datetime
import yagmail
import pyjokes


app = FastAPI()

FROM_EMAIL = "thestockdude10@gmail.com"
FROM_PWD = "pqnoalssfcodnous"
SMTP_SERVER = "imap.gmail.com"

@app.get('/google/{query_id}')
def run_code(query_id):
    results = []  # create an empty list to store the results

    user_query = query_id.replace("+", " ").replace("search up", "")

    URL = "https://www.google.co.in/search?q=" + user_query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')



    try:
        answer = soup.find(class_='LGOjhe').get_text()
        results.append(answer)
    except Exception:
        try:
            result = soup.find(class_='di3YZe').get_text()
            results.append(result.replace("-", " "))
        except Exception:
            try:
                result = soup.find(class_='kno-rdesc').get_text()
                results.append(result.replace("-", " "))
            except Exception:
                try:
                    result = soup.find(class_='kno-rdesc').get_text()
                    results.append(result.replace("-", " "))
                except Exception:
                    try:
                        result = soup.find(class_='BbbuR uc9Qxb uE1RRc').get_text()
                        results.append(result.replace("-", " "))
                    except Exception:
                        try:
                            result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                            results.append(result.replace("-", " "))
                        except Exception:
                            result = soup.find(class_ = 'LGOjhe').get_text
                            results.append(result)

    # Build HTML response
    html_content = "<html><body>"
    for result in results:
        html_content += "<p>" + result + "</p>"
    html_content += "</body></html>"
    return HTMLResponse(content=html_content)

@app.get('/joke')
def joke():
    results = []
    joke = pyjokes.get_joke()
    results.append(joke)

    html_content = "<html><body>"
    for joke in results:
        html_content += "<p>" + joke + "</p>"
    html_content += "</body></html>"
    return HTMLResponse(content=html_content)

@app.get('/stock/{query}')
def stock_price(query):
   response = []
   try:
        user_query = query

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        if datetime.now().strftime('%I:%M %p') > '9:30' and datetime.now().strftime('%I:%M %p') < '4:00':
            stockprice = soup.find("span", jsname='vWLAgc').text
            stock = soup.find_all('div', {'class': 'oPhL2e'})[0].find('span').text
            percent = soup.find("span", jsname="rfaVEf").text
            UOD = soup.find("span",jsname="qRSVye").text
            #print(UOD)
            if UOD > "0":
                response.append("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up " + percent)
            else:
                response.append("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down " + percent)


            d = datetime.now().date()
            date = str(d.strftime('%w'))
            #print(date)
            if "1" == date:
                if "+" in UOD:
                    response.append("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up " + percent + " from last friday")
                else:
                    response.append("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down " + percent)
        else:
            stockprice = soup.find("span", jsname="wurNO").text
            stock = soup.find_all('div', {'class': 'oPhL2e'})[0].find('span').text
            percent = soup.find("span", jsname="sam3Lb").text
            UOD = soup.find("span", jsname="TmYleb").text
            d = datetime.now().date()
            date = str(d.strftime('%w'))
            #print(date)
            if "1" == date:
                if "+" in UOD:
                    response.append("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up" + percent + " from last friday")
                else:
                    response.append("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down" + percent + " from last friday")
            else:
                if "+" in UOD:
                    response.append("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, up" + percent + " from yesterday")
                else:
                    response.append("As of " + datetime.now().strftime('%I:%M %p') + ", " + stock + " is trading at " + stockprice + " $ per share, down" + percent + " from yesterday")
   except Exception:
        response.append(response)
   html_content = "<html><body>"
   response = str(response)
   for response in response:
       html_content += "<p>" + response + "</p>"
   html_content += "</body></html>"
   return HTMLResponse(content=html_content)

@app.get('/spelling/{query}')
def spelling(query):
    response = []
    try:
        user_query = query.replace("search up", "")

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        spelling = soup.find(class_='MiCl6d').get_text().replace("·", ",   ")
        s1 = spelling.replace(",   ", "")
        response.append(s1 + " is spelled " + spelling)
        response.append()
    except Exception:  # and result == "" or Exception and result == "":
        response.append("Im sorry, I could not find how to spell your word")
    html_content = "<html><body>"
    for response in response:
       html_content += "<p>" + response + "</p>"
    html_content += "</body></html>"
    return HTMLResponse(content=html_content)

@app.get('/timer/{query}')
def countdown(query):
    response = []
    global my_timer
    URL = "https://www.google.co.in/search?q=" + query
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    time4timer = soup.find(jsname="VQs5Rb").text.replace("h", " Hour ").replace("m", " minute ").replace("s", " seconds ").split()
    time4timer.pop(5)
    time4timer.pop(4)
    if "00" in time4timer[0]:
        time4timer.pop(0)
        time4timer.pop(0)
        if "00" in time4timer[0]:
            time4timer.pop(0)
            time4timer.pop(0)
    queryy = str(time4timer).replace("[", "").replace("'", "").replace(",", "").replace("]", "")
    #print(queryy)
    URL = "https://www.google.co.in/search?q=" + "Convert " + queryy + " to seconds"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    time = soup.find(id="NotFQb")
    #print(time)
    timer = str(time)
    #print(timer)
    timey = timer.split(" ")
    time4timer = int(timey[9].replace('"', "").replace("/", "").replace(">", "").replace("value=", ""))
    my_timer = time4timer

    response.append(my_timer)

    html_content = "<html><body>"
    for my_timer in response:
        html_content += "<p>" + str(my_timer) + "</p>"
    html_content += "</body></html>"
    return HTMLResponse(content=html_content)

@app.get('/email/write/{to_email}/{subject}/{content}')
def send_email(to_email, subject, content):
    response = []
    if "dad" in to_email or "Dad" in to_email:
        yag = yagmail.SMTP("thestockdude10@gmail.com", "pqnoalssfcodnous")
        yag.send('bipulkarki@gmail.com', subject.replace("+", " "), content.replace("+", " "))
        response.append("Email sent sucessfully")
    else:
        response.append("Im sorry, I cant sent that email")

    html_content = "<html><body>"
    for response in response:
        html_content += "<p>" + response + "</p>"
    html_content += "</body></html>"
    return HTMLResponse(content=html_content)

@app.get('/joke')
def joke():
    results = []
    joke = pyjokes.get_joke()
    results.append(joke)

    html_content = "<html><body>"
    for joke in results:
        html_content += "<p>" + joke + "</p>"
    html_content += "</body></html>"
    return HTMLResponse(content=html_content)

