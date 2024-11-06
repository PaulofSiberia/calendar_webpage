from datetime import datetime, timezone, timedelta
def clock():
    months = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ] #обход locale
    time_now = datetime.now(timezone(timedelta(hours=8)))
    month = months[time_now.month - 1]
    return time_now.strftime("%d ") + month + time_now.strftime(" %Y г.\n%X")