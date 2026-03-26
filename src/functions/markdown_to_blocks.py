def markdown_to_blocks(markdown):
    text = markdown.split("\n\n")
    new_text = []
    for line in text:
        
        line = line.strip()
        if line == "":
            continue
        
        new_text.append(line)
    
    return new_text
