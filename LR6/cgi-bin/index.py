#!/usr/bin/env python3
print("Content-type: text/html\n\n")

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Кадровое агентство</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        .menu a { 
            display: inline-block;
            margin: 10px;
            padding: 10px;
            background: #0066cc;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Кадровое агентство</h1>
    <div class="menu">
        <a href="view.py?table=employees">Сотрудники</a>
        <a href="view.py?table=positions">Должности</a>
        <a href="view.py?table=applications">Заявки</a>
    </div>
</body>
</html>
"""
print(html)