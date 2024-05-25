import logging
from nlp_chatbot import app

# Set up logging
logging.basicConfig(level=logging.INFO)

def handler(event, context):
    try:
        if __name__ == "__main__":
            app.run()
        return {
            'statusCode': 200,
            'body': 'Function executed successfully'
        }
    except Exception as e:
        logging.error(f"Unhandled exception: {e}", exc_info=True)
        return {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }

# Call the handler function
handler({}, {})
