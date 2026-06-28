from flask import Flask, render_template, request, jsonify
import json, re
import os

app = Flask(__name__)

# Function to load settings from the JSON file
def load_settings():
    with open('settings.json') as f:
        return json.load(f)

# Function to save settings to the JSON file
def save_settings(settings):
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

# Route for the home page (index)
@app.route('/')
def index():
    return render_template('home.html',chal_name="No WAF Version",chal_p="You cannot use the word 'flag'")

# Route for WAN Setup
@app.route('/wan_setup', methods=['GET', 'POST'])
def wan_setup():
    settings = load_settings()
    if request.method == 'POST':
        mode = request.form.get('mode')
        settings['WAN']['Mode'] = mode
        save_settings(settings)
    return render_template('wan_setup.html', settings=settings['WAN'])

# Route for LAN Setup
@app.route('/lan_setup', methods=['GET', 'POST'])
def lan_setup():
    settings = load_settings()
    if request.method == 'POST':
        dhcp_server = request.form.get('dhcp_server')
        settings['LAN']['DHCP_Server'] = dhcp_server
        save_settings(settings)
    return render_template('lan_setup.html', settings=settings['LAN'])

BLACKLIST = [
    r"[f|F][l|L][a|A][g|G]"
]


# BLACKLIST = [
#     r"[;]",           # Semicolon
#     r"[&]",           # Ampersand
#     r"[|]",           # Pipe
#     r"[\']",          # Single quote
#     r'["]',           # Double quote
#     r"[\s]+",         # Whitespace (if you want to prevent it)
# ]

def is_input_clean(user_input):
    for pattern in BLACKLIST:
        if re.search(pattern, user_input):
            return False
    return True



# Route for Ping Tool (GET)
@app.route('/ping_tool', methods=['GET'])
def ping_tool_page():
    return render_template('ping_tool.html')

# Route for Ping Tool (POST)
@app.route('/ping_tool', methods=['POST'])
def ping_tool():
    ip = request.json.get('ip')
    if not is_input_clean(ip):
        return jsonify({"error": "Invalid input detected."}), 400  # Bad request
    try:
        output = os.popen(f"ping -c 4 {ip}").read()
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "Ha4ker!!!"})

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
