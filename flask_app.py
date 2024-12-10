from flask import Flask, render_template_string, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

events = []

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
        if event_time and event_name:
            events.append({"time": event_time, "event": event_name})
            return redirect(url_for('home'))

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
            input[type="text"] {
                padding: 5px;
                margin: 5px;
            }
            input[type="submit"] {
                padding: 5px 10px;
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

        <form method="POST">
            <input type="text" name="event_time" placeholder="Время (например, 16:00)" required>
            <input type="text" name="event_name" placeholder="Название мероприятия" required>
            <input type="submit" value="Добавить мероприятие">
        </form>

    </body>
    </html>
    """
    return render_template_string(html_template, datetime=formatted_date, events=events)

if __name__ == "__main__":
    app.run(debug=True)
