# Face Recognition API

This is a face recognition API built using Python and Flask.

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/yourrepository.git

2. Navigate to the project directory:
   cd yourrepository

3. Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:
   - For Windows:
     .\venv\Scripts\activate
   - For macOS/Linux:
     source venv/bin/activate

5. Install required dependencies:
   pip install -r requirements.txt

## Usage

Run the Flask application:
   python app.py

The API will be available at http://127.0.0.1:5000.

## API Endpoints

- **POST /verify_faces**
   - Accepts base64-encoded images in the request body and returns a similarity score.
   - Example request body:
     ```json
     {
       "image1": "base64_string_1",
       "image2": "base64_string_2"
     }
     ```

   - Example response:
     ```json
     {
       "verified": true,
       "distance": 0.32,
       "threshold": 0.68
     }
     ```

## License

This project is licensed under the MIT License.
