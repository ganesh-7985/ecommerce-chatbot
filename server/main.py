from app import create_app
from app.utils.database import init_db, populate_mock_data

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        init_db()
        populate_mock_data()
    app.run(debug=True, host='0.0.0.0', port=5000)
