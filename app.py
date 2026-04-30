from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = request.form.get("input_data")

        try:
            number = int(user_input)
            result = f"Square: {number ** 2}"
        except:
            result = f"Reversed: {user_input[::-1]}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)