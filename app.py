from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure for storing CNIC records
cnic_data = {
    '12345-1234567-1': {'name': 'John Doe', 'age': 30},
    '98765-9876543-2': {'name': 'Jane Smith', 'age': 25}
}

@app.route('/cnic/search', methods=['GET'])
def search_cnic():
    cnic = request.args.get('cnic')
    if cnic in cnic_data:
        return jsonify(cnic_data[cnic]), 200
    return jsonify({'message': 'CNIC not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)