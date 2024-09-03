import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
# Importing custom functions from your modules
from semantic_search_2 import extract_text_from_pdf, generate_summary, store_summary_in_chroma
from semantic_chat_boat_3 import answer_question
from extract_product_attributes_4 import get_product_details
from product_review_summary_5 import get_product_review
from code_optimisation_10 import optimize_code
from code_conversion_11 import convert_code
from Text_Language_Translator_13 import perform_translation
from image_to_text_6 import image_to_detailed_description
from QA_img_8 import answer_question_based_on_image
from code_Comment_16 import comment_code
from Proofread_Correct_Content_14 import process_text

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your React frontend
 
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
# Ensure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
 
# Route for summarization and semantic search
@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'pdf_file' not in request.files:
        return jsonify({"error": "No file part"}), 400
 
    file = request.files['pdf_file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
 
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(file_path)
 
    pdf_text = extract_text_from_pdf(file_path)
    summary = generate_summary(pdf_text)
    store_summary_in_chroma(pdf_text, summary)
    return jsonify({"summary": summary})
 
# Route for asking questions (Semantic Search)
@app.route('/ask-question', methods=['POST'])
def ask_question_route():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    answer = answer_question(question)
    return jsonify({"answer": answer})
 
# Route for extracting product attributes
@app.route('/product-name', methods=['POST'])
def extract_product():
    data = request.json
    product_name = data.get("product", "")
    model = data.get("model", "")
 
    if not product_name or not model:
        return jsonify({"error": "Model or Product name is missing"}), 400
 
    product_details = get_product_details(product_name, model)
    return jsonify({"product_details": product_details})
 
# Route for product review summary
@app.route('/product-review', methods=['POST'])
def review_product():
    data = request.json
    product_name = data.get("product", "")
    model = data.get("model", "")
 
    if not product_name or not model:
        return jsonify({"error": "Model or Product name is missing"}), 400
 
    product_details = get_product_review(product_name, model)
    return jsonify({"product_details": product_details})
 
# Route for code optimization
@app.route("/optimize", methods=["POST"])
def optimize_code_endpoint():
    code = request.form.get("code")
    model = request.form.get("model")
    if not code or not model:
        return jsonify({"error": "Code or model selection is missing"}), 400
    try:
        optimized_code = optimize_code(code, model)
        return jsonify({"optimized_code": optimized_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
# Route for code commenting
@app.route("/comment", methods=["POST"])
def comment_code_route():
    code = request.form.get("code")
    model = request.form.get("model")
 
    if not code or not model:
        return jsonify({"error": "Code or model selection is missing"}), 400
 
    try:
        commented_code = comment_code(code, model)
        return jsonify({"commented_code": commented_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
# Route for code conversion
@app.route('/convert', methods=['POST'])
def convert_code_route():
    data = request.get_json()
    model = data.get('model')
    from_language = data.get('fromLanguage')
    to_language = data.get('toLanguage')
    code = data.get('code')
 
    if not model or not from_language or not to_language or not code:
        return jsonify({"error": "Missing parameters"}), 400
 
    converted_code = convert_code(model, from_language, to_language, code)
    return jsonify({"convertedCode": converted_code})
 
# Route for text language translation
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    model = data.get('model')
    source_lang = data.get('sourceLanguage')
    target_lang = data.get('targetLanguage')
    text = data.get('text')
 
    if not model or not source_lang or not target_lang or not text:
        return jsonify({"error": "Missing parameters"}), 400
 
    translated_text = perform_translation(model, source_lang, target_lang, text)
    return jsonify({"translated_text": translated_text})
 
# Route for image-to-text conversion
@app.route('/uploadimg', methods=['POST'])
def upload_img():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
 
    text = image_to_detailed_description(file_path)
    return jsonify({'text': text}), 200
 
# Route for image-based question answering
@app.route('/ask-question-image', methods=['POST'])
def ask_question_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
 
    file = request.files['image']
    question = request.form.get('question')
 
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
 
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
 
    answer = answer_question_based_on_image(question, file_path)
    return jsonify({'answer': answer}), 200
 
# Route for processing text
@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    action = data.get('action')
    text = data.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    try:
        result = process_text(action, text)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
if __name__ == "__main__":
    app.run(debug=True)


















# import os
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from werkzeug.utils import secure_filename
 
# # Importing custom functions from your modules
# from semantic_search_2 import extract_text_from_pdf, answer_question, generate_summary, store_summary_in_chroma
# from semantic_chat_boat_3 import extract_text_from_pdf, answer_question, generate_summary, store_summary_in_chroma
# from extract_product_attributes_4 import get_product_details
# from product_review_summary_5 import get_product_review
# from code_optimisation_10 import optimize_code
# from code_conversion_11 import convert_code
# from Text_Language_Translator_13 import perform_translation
# from image_to_text_6 import image_to_detailed_description
# from QA_img_8 import answer_question_based_on_image
# from code_Comment_16 import comment_code
# from Proofread_Correct_Content_14 import process_text


# app = Flask(__name__)
# CORS(app)  # Enable CORS to allow requests from your React frontend
 
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
# # Ensure the uploads folder exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
 
# # Route for summarization and semantic search
# @app.route('/upload-pdf', methods=['POST'])
# def search():
#     if 'pdf_file' not in request.files:
#         return jsonify({"error": "No file part"}), 400
 
#     file = request.files['pdf_file']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400
 
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
#     file.save(file_path)
 
#     pdf_text = extract_text_from_pdf(file_path)
#     summary = generate_summary(pdf_text)
#     store_summary_in_chroma(pdf_text, summary)
#     return jsonify({"summary": summary})
 
# # Route for asking questions (Semantic Search)
# @app.route('/ask-question', methods=['POST'])
# def ask():
#     data = request.json
#     question = data.get('question', '')
#     if not question:
#         return jsonify({"error": "No question provided"}), 400
#     answer = answer_question(question)
#     return jsonify({"answer": answer})
 
# # Route for extracting product attributes
# @app.route('/product-name', methods=['POST'])
# def extract_product():
#     data = request.json
#     product_name = data.get("product", "")
#     model = data.get("model", "")
 
#     if not product_name or not model:
#         return jsonify({"error": "Model or Product name is missing"}), 400
 
#     product_details = get_product_details(product_name, model)
#     return jsonify({"product_details": product_details})

# # Route for product review summary
# @app.route('/product-review', methods=['POST'])
# def review_product():
#     data = request.json
#     product_name = data.get("product", "")
#     model = data.get("model", "")
 
#     if not product_name or not model:
#         return jsonify({"error": "Model or Product name is missing"}), 400
 
#     product_details = get_product_review(product_name, model)
#     return jsonify({"product_details": product_details})
 
# # Route for code optimization
# @app.route("/optimize", methods=["POST"])
# def optimize_code_endpoint():
#     code = request.form.get("code")
#     model = request.form.get("model")
#     if not code or not model:
#         return jsonify({"error": "Code or model selection is missing"}), 400
#     try:
#         optimized_code = optimize_code(code, model)
#         return jsonify({"optimized_code": optimized_code})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    

# # Route for code comment
# @app.route("/comment", methods=["POST"])
# def comment_code_route():
#     code = request.form.get("code")
#     model = request.form.get("model")
 
#     if not code or not model:
#         return jsonify({"error": "Code or model selection is missing"}), 400
 
#     try:
#         commented_code = comment_code(code, model)
#         print(f"Commented code: {commented_code}")  # Debug print
#         return jsonify({"commented_code": commented_code})
#     except Exception as e:
#         print(f"Error occurred: {str(e)}")  # Debug print
#         return jsonify({"error": str(e)}), 500
    
 
# # Route for code conversion
# @app.route('/convert', methods=['POST'])
# def convert_code_route():
#     data = request.get_json()
#     model = data.get('model')
#     from_language = data.get('fromLanguage')
#     to_language = data.get('toLanguage')
#     code = data.get('code')
 
#     converted_code = convert_code(model, from_language, to_language, code)
#     return jsonify({"convertedCode": converted_code})
 
# # Route for text language translation
# @app.route('/translate', methods=['POST'])
# def translate():
#     data = request.get_json()
#     model = data.get('model')
#     source_lang = data.get('sourceLanguage')
#     target_lang = data.get('targetLanguage')
#     text = data.get('text')
 
#     translated_text = perform_translation(model, source_lang, target_lang, text)
#     return jsonify({"translated_text": translated_text})
 
# # Route for image-to-text conversion
# @app.route('/uploadimg', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     file.save(file_path)
 
#     text = image_to_detailed_description(file_path)
#     return jsonify({'text': text}), 200
 
# # Route for image-based question answering
# @app.route('/ask-question-image', methods=['POST'])
# def ask_question_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
 
#     file = request.files['image']
#     question = request.form.get('question')
 
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
 
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     file.save(file_path)
 
#     # Call the function from main_code.py to process the image and answer the question
#     answer = answer_question_based_on_image(question, file_path)
 
#     return jsonify({'answer': answer}), 200
 

# @app.route('/api/submit', methods=['POST'])
# def submit():
#     data = request.get_json()
#     action = data.get('action')
#     text = data.get('text')
#     if not text:
#         return jsonify({"error": "No text provided"}), 400
#     try:
#         # Call the appropriate function from the main backend file
#         result = process_text(action, text)
#         return jsonify({"result": result})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(debug=True)