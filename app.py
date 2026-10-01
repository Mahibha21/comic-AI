from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Please enter a story idea"}), 400

    # Temporary comic panels
    panels = [
        {
            "title": "Panel 1",
            "description": f"Our story begins: {prompt}"
        },
        {
            "title": "Panel 2",
            "description": "The main character discovers something mysterious."
        },
        {
            "title": "Panel 3",
            "description": "An unexpected problem appears."
        },
        {
            "title": "Panel 4",
            "description": "The character decides to solve the problem."
        },
        {
            "title": "Panel 5",
            "description": "The adventure reaches its exciting moment."
        },
        {
            "title": "Panel 6",
            "description": "The story ends with a surprising conclusion."
        }
    ]

    return jsonify({"panels": panels})


if __name__ == "__main__":
    app.run(debug=True)
