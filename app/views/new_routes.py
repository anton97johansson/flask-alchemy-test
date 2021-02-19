from .. import app
from flask import jsonify

@app.route('/test2', methods=['GET'])
def get_tasks2():
    return "jsonify({'tasks': tasks})"

# if __name__ == '__main__':
#     app.run(debug=True)