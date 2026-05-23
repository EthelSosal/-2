from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Калькулятор 100-летия</title>
    <style>
        body {
            font-family: Arial;
            margin: 40px;
            background: #f0f0f0;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            max-width: 500px;
            margin: auto;
        }
        h1 {
            color: #3776AB;
            text-align: center;
        }
        input[type="text"],
        input[type="number"] {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            box-sizing: border-box;
            outline: none;
            transition: 0.3s;
        }
        input[type="text"]:focus,
        input[type="number"]:focus {
            border-color: #3776AB;
            box-shadow: 0 0 8px rgba(55, 118, 171, 0.3);
        }
        button {
            width: 100%;
            padding: 12px 20px;
            background-color: #3776AB;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 10px;
        }
        button:hover {
            background-color: #2b5d8a;
        }
        .error {
            color: red;
            margin-top: 15px;
        }
        .result {
            margin-top: 20px;
            background-color: #fff8e1;
            border-left: 4px solid #ffd343;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Калькулятор 100-летия</h1>
        <form method="post">
            <input name="name" placeholder="Ваше имя" required>
            <input name="age" placeholder="Ваш возраст" type="number" required>
            <button type="submit">Рассчитать</button>
        </form>
        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}
        {% if name %}
            <div class="result">
                <p>Привет, {{ name }}!</p>
                <p>Вам {{ age }} лет.</p>
                {% if age < 100 %}
                    <p>Вы достигнете 100 лет в {{ year_to_100 }} году.</p>
                {% elif age == 100 %}
                    <p>Вам уже 100 лет! Поздравляю!</p>
                {% else %}
                    <p>Вам больше 100 лет. Вы достигли этого в {{ year_to_100 }} году.</p>
                {% endif %}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age_str = request.form.get('age', '')

        if not name:
            return render_template_string(HTML, error="Пожалуйста, введите имя.")

        try:
            age = int(age_str)
            if age < 0 or age > 150:
                raise ValueError
        except ValueError:
            return render_template_string(HTML, error="Ошибка: возраст должен быть целым числом от 0 до 150.")

        current_year = datetime.now().year
        year_to_100 = current_year + (100 - age)

        return render_template_string(
            HTML,
            name=name,
            age=age,
            year_to_100=year_to_100,
            error=None
        )

    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
