import os
import logging
from flask import Flask, render_template, request, jsonify
from utils.validators import (
    validate_and_format_cpf, 
    validate_and_format_cnpj, 
    detect_document_type, 
    format_cpf_cnpj
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-dev-secret")

@app.route('/', methods=['GET'])
def index():
    """Render the main page with the CPF/CNPJ validation form."""
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    """API endpoint to validate and format CPF/CNPJ."""
    document = request.form.get('document', '').strip()
    
    # Remove any non-digit characters for validation
    document_digits = ''.join(filter(str.isdigit, document))
    
    # Detect document type based on length
    doc_type = detect_document_type(document_digits)
    
    if doc_type == 'CPF':
        is_valid, formatted = validate_and_format_cpf(document_digits)
    elif doc_type == 'CNPJ':
        is_valid, formatted = validate_and_format_cnpj(document_digits)
    else:
        is_valid = False
        formatted = format_cpf_cnpj(document_digits)  # Tenta formatar mesmo sem validar
    
    response = {
        'valid': is_valid,
        'formatted': formatted,
        'type': doc_type if doc_type else None,
        'message': get_response_message(is_valid, doc_type)
    }
    
    return jsonify(response)

@app.route('/format', methods=['POST'])
def format_document():
    """API endpoint que apenas formata o CPF/CNPJ sem validar."""
    document = request.form.get('document', '').strip()
    formatted = format_cpf_cnpj(document)
    
    doc_type = detect_document_type(''.join(filter(str.isdigit, document)))
    
    response = {
        'formatted': formatted,
        'type': doc_type,
        'success': formatted is not None
    }
    
    return jsonify(response)

def get_response_message(is_valid, doc_type):
    """Generate appropriate response message based on validation result."""
    if not doc_type:
        return "Número de dígitos inválido. CPF deve ter 11 dígitos e CNPJ 14 dígitos."
    
    if is_valid:
        return f"{doc_type} válido!"
    else:
        return f"{doc_type} inválido. Verifique os dígitos informados."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
