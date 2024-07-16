@app.route('/process', methods=['POST'])
def process_task():
    data = request.json
    task_type = data.get('task_type')
    task_data = data.get('task_data')
    
    if not task_type or not task_data:
        return jsonify({"error": "task_type and task_data are required"}), 400

    try:
        result = integration_layer.process_task(task_type, task_data)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/process', methods=['POST'])
def process_task():
    data = request.json
    task_type = data.get('task_type')
    task_data = data.get('task_data')

    if not task_type or not task_data:
        return jsonify({"error": "task_type and task_data are required"}), 400

    # Sanitize inputs
    if not isinstance(task_type, str) or not isinstance(task_data, dict):
        return jsonify({"error": "Invalid input types"}), 400

    try:
        result = integration_layer.process_task(task_type, task_data)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
