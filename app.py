from flask import Flask, request, render_template_string
from processing import analyze

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>HSK Analyzer</title>
</head>
<body>
<h2>HSK Text Analyzer</h2>

<form method="post">
<textarea name="text" rows="10" cols="80">{{ text }}</textarea><br><br>
<button type="submit">Phân tích</button>
</form>

{% if result %}
<pre>{{ result }}</pre>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    result = None
    if request.method == "POST":
        text = request.form["text"]
        result = analyze(text)
    return render_template_string(HTML, text=text, result=result)

if __name__ == "__main__":
    app.run()
