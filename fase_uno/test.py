from flask import Flask, render_template, request, jsonify  

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
	if 'file' not in request.files:
		return jsonify({'error': 'No file part'})

	file = request.files['file']

	if file.filename == '':
		return jsonify({'error':'No selected file'})

	contenido = file.read().decode('utf-8')	
	
	return jsonify({'content': contenido})
		


if __name__ == '__main__':
	app.run(debug=True)


