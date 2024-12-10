from flask import Flask, render_template_string, request, redirect, url_for
from datetime import datetime, timedelta
import re

app = Flask(__name__)

events = []
PASSWORD = "CHANGED_FOR_GITHUB"  #замена пароля

@app.route("/", methods=["GET", "POST"])
def home():
    months = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]

    utc_now = datetime.utcnow()
    utc_plus_8 = utc_now + timedelta(hours=8)

    day = utc_plus_8.day
    month = months[utc_plus_8.month - 1]
    time = utc_plus_8.strftime("%H:%M")

    formatted_date = f"{day} {month}, {time}"

    if request.method == "POST":
        event_time = request.form.get("event_time")
        event_name = request.form.get("event_name")
        input_password = request.form.get("password")
        
        if input_password == PASSWORD:
            if event_time and event_name and re.match(r'^\d{2}:\d{2}$', event_time):
                events.append({"time": event_time, "event": event_name})
                return redirect(url_for('home'))
            else:
                error_message = "Неверный формат времени!"
        else:
            error_message = "Неверный пароль!"

    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Календарь студента ИрНИТУ</title>
        <style>
            body, html {
                margin: 0;
                padding: 0;
                height: 100%;
                font-family: Tahoma;
                display: flex;
                flex-direction: column;
            }
            header {
                color: #ffffff;
                background-color: #0012a4;
                border-bottom: 1px solid #ddd;
                text-align: center;
            }
            #datetime {
                background-color: #ffffff;
                text-align: center;
                padding: 10px;
                font-size: 20px;
                border-bottom: 1px solid #ccc;
            }
            #dynamic-list {
                flex-grow: 1;
                padding: 20px;
                overflow-y: auto;
                background-color: #3444c3;
            }
            #dynamic-list ul {
                list-style-type: none;
                padding: 0;
            }
            #dynamic-list ul li {
                padding: 10px;
                margin-bottom: 5px;
                background-color: #ffffff;
                border-radius: 5px;
            }
            form {
                text-align: center;
                margin: 20px 0;
            }
            input[type="time"], input[type="text"], input[type="password"] {
                padding: 5px;
                margin: 5px;
            }
            input[type="submit"] {
                padding: 5px 10px;
            }
            .error {
                color: red;
                text-align: center;
            }
        </style>
    </head>
    <body>

        <header>
            <h1>Календарь студента ИрНИТУ</h1>
        </header>

        <div id="datetime">
            {{ datetime }}
        </div>

        <div id="dynamic-list">
            <ul>
                {% for event in events %}
                <li>{{ event.time }} - {{ event.event }}</li>
                {% endfor %}
            </ul>
        </div>

        {% if error_message %}
        <div class="error">{{ error_message }}</div>
        {% endif %}

        <form method="POST">
            <input type="time" name="event_time" required>
            <input type="text" name="event_name" placeholder="Название мероприятия" required>
            <input type="password" name="password" placeholder="Пароль" required>
            <input type="submit" value="Добавить мероприятие">
        </form>

    </body>
    </html>
    """
    return render_template_string(html_template, datetime=formatted_date, events=events, error_message=locals().get('error_message', ''))

if __name__ == "__main__":
    app.run(debug=True)
