from flask import Flask, render_template_string
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def home():
    # Список названий месяцев в родительном падеже
    months = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]

    # Рассчитаем текущее время UTC+8
    utc_now = datetime.utcnow()
    utc_plus_8 = utc_now + timedelta(hours=8)

    # Получим текущий день, месяц и время
    day = utc_plus_8.day
    month = months[utc_plus_8.month - 1]  # Название месяца (индекс с 0)
    time = utc_plus_8.strftime("%H:%M")

    # Сформатируем дату
    formatted_date = f"{day} {month}, {time}"

    # Пример списка мероприятий
    events = [
        {"time": "09:00", "event": "Мероприятие 1"},
        {"time": "11:00", "event": "Мероприятие 2"},
        {"time": "15:00", "event": "Мероприятие 3"},
    ]

    # Встроенный HTML и CSS
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

    </body>
    </html>
    """
    return render_template_string(html_template, datetime=formatted_date, events=events)

if __name__ == "__main__":
    app.run(debug=True)
