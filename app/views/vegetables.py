from .. import app
from .. import db
from ..models.vegetables import Vegetables
from flask import jsonify, request

@app.route('/veggies', methods=['GET'])
def veggiesGET():
    # firstVeg = Vegetables(name="banana", colour="yellow", flavour="banana")
    # db.session.add(firstVeg)
    # db.session.commit()
    veggies = Vegetables.query.all()
    return jsonify([{"_id": vegetable.id, "name": vegetable.name, "flavour": vegetable.flavour} for vegetable in veggies])
# @app.route('/veggies', methods=['POST'])
# def create_veggie():
#     data = request.get_json()
#     if not 'name' in data or not
#     firstVeg = Vegetables(name, colour, flavour)
#     db.session.add(firstVeg)
#     db.session.commit()
#     return "ADDED"

# if __name__ == '__main__':
#     app.run(debug=True)