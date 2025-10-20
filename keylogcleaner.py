def process_keylog(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()
    
    keystrokes = content.split('\n')
    
    cleaned_text = ''
    for key in keystrokes:
        if not key:
            continue
            
        # Special cases Keys with Key. prefix
        if key == 'Key.backspace':
            cleaned_text = cleaned_text[:-1] if cleaned_text else ''
        elif key == 'Key.enter':
            cleaned_text += '\n'
        elif key == 'Key.space':
            cleaned_text += ' '
        elif key == 'Key.tab':
            cleaned_text += '\t'
        elif key == 'Key.shift':
            cleaned_text += '' 
        elif key.startswith('Key.'):
            cleaned_text += " " + key + " "
        else:
            cleaned_text += key
    

    with open(output_file, 'w') as f:
        f.write(cleaned_text)
