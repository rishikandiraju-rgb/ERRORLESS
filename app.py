from flask import Flask, render_template, request
import os
from speechtotext import generate_notes

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    notes = None
    if request.method == "POST":
        # Check if a file was actually uploaded
        if 'audio' not in request.files:
            return "No file part"

        file = request.files["audio"]
        if file.filename == '':
            return "No selected file"

        # Save the file
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Currently using your hardcoded text for logic testing
        text = """photosynthesis is the process by which green plants prepare their own food using sunlight
        the chlorophyll present in leaves absorbs light energy carbon dioxide from the air and water
        from the soil are used in this process oxygen is released as a byproduct photosynthesis is
        essential because it provides food and oxygen for almost all living organisms on earth"""

        notes = generate_notes(text)

    return render_template("index.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)