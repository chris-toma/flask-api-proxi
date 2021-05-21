from werkzeug.security import generate_password_hash

users = {
    "nbnotes_no": {"pass": generate_password_hash("nbnotes_no"), "routes": {"/nbnote_invoice"}},
    "nbnotes_en": generate_password_hash("nbnotes_en")
}