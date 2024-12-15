import os

def run(args):
    try:
        items = os.listdir('.')
        if items:
            for item in items:
                print(item)
        else:
            print("The directory is empty.")
    except Exception as e:
        print(f"Error: {e}")
