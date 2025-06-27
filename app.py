from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from profile_analyzer import get_user_profile

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    try:
        name = request.form["name"]
        summary_and_facts, interests, ice_breakers, profile_pic_url = get_user_profile(name)
        return jsonify(
            {
                "summary_and_facts": summary_and_facts.to_dict(),
                "interests": interests.to_dict(),
                "ice_breakers": ice_breakers.to_dict(),
                "picture_url": profile_pic_url,
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)