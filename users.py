from werkzeug.security import generate_password_hash

users = {
    "nbnotes_no": {"pass": generate_password_hash("nbnotes_no"), "routes": {"/nbnote_invoice_no"}},
    "nbnotes_en": {"pass": generate_password_hash("nbnotes_en"), "routes": {"/nbnote_invoice_en"}},
}
