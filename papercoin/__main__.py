import threading

import run
import endpoint

def start_flask():
    endpoint.app.run(debug=False)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()
    
    run.main()