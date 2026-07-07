from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    image = None

    if request.method == "POST":
        file = request.files.get("image")

        if file and file.filename:
            filename = file.filename
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)

            image = "/" + save_path.replace("\\", "/")

    return render_template("index.html", image=image)


if __name__ == "__main__":
    app.run(debug=True)
