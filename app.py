from flask import Flask, render_template_string, request
from processing import analyze
import os

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>HSK Analyzer</title>
</head>  
<body style="font-family:Arial;padding:20px">
    <h2>HSK Text Analyzer</h2>
    <form method="post">
        <textarea name="text" rows="6" cols="70">{{ text }}</textarea><br><br>
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
    result = None
    text = ""
    if request.method == "POST":
        text = request.form["text"]
        r = analyze(text)
        result = (
            f"Số chữ Hán: {r['characters']}\n"
            f"Số từ: {r['words']}\n"
            f"Phân bố level: {r['level_distribution']}\n"
            f"Ước lượng HSK: {r['estimated_level']}\n"
            f"Cảnh báo: {r['warning']}"
        )
    return render_template_string(HTML, result=result, text=text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
