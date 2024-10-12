from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_homepage():
    # logger.info("homepage successful")
    return render_template("webpage_garage.html",
                           filename="static/work_from_home.jpg", organization="static/organization.jpg",
                           logo="static/logo.jpg", techshuttle="static/Spaceship.jpg"
                           )



if __name__ == "__main__":
    # logging.info('App started and is running successfully')
    app.run(debug=True)