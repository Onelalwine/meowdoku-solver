from flask import Flask, render_template, request
import os

from detector import load_image
from solver import MeowdokuSolver

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    image = None
    info = None
    hint = None

    if request.method == "POST":
        file = request.files.get("image")

        if file and file.filename:
            filename = file.filename
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)

            image = "/" + save_path.replace("\\", "/")

            info = load_image(save_path)

            solver = MeowdokuSolver()
            solver.load_board(info)
            hint = solver.next_hint()

    return render_template(
        "index.html",
        image=image,
        info=info,
        hint=hint
    )


if __name__ == "__main__":
    app.run(debug=True)
