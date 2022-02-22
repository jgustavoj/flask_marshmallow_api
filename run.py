import os
from src.app import create_app


# Run server 
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
