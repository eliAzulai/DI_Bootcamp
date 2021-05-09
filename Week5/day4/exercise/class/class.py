import json


try: 
    menu = read_from_menu()
except json.decoder.JSONDecoderError:
    menu = []
    
def add_to_menu