
import traceback

def handle_error(e: Exception):
    print("\n===== ERROR =====")
    traceback.print_exc()
    print("=================\n")

    return {
        "error": str(e)
    }
