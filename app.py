from flask import Flask, request, render_template, jsonify, flash
from werkzeug.utils import secure_filename
from planner.input_handler import handle_input
from planner.scheduler import build_schedule_for_today, init_db, save_schedule_to_db, get_all_schedules
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
app.secret_key = 'dev_secret'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('data', exist_ok=True)

# Initialize database immediately
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    schedule = []
    if request.method == 'POST':
        text = request.form.get('text_input', '').strip()
        file = request.files.get('file_input')
        file_path = None

        if file and file.filename:
            filename = secure_filename(file.filename)
            ext = filename.rsplit('.', 1)[-1].lower()
            if ext not in app.config['ALLOWED_EXTENSIONS']:
                flash('Unsupported file type.')
            else:
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)
                file_path = path

        try:
            instructions = handle_input(text, file_path)
            schedule = build_schedule_for_today(instructions)
            save_schedule_to_db(schedule)
        except Exception as e:
            flash(str(e))

    schedules = get_all_schedules()
    return render_template('index.html', schedule=schedule, all_schedules=schedules)

@app.route('/api/schedule')
def api_schedule():
    schedules = get_all_schedules()
    return jsonify(schedules)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
