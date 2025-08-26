from app import app
import os


port = int(os.environ.get("PORT", 5000))
# démarrer serveur local
app.run(host="0.0.0.0", port=port, debug=True)
