from textnode import TextType, TextNode



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text

        if delimiter not in text:
            new_nodes.append(old_node)
            continue

        start_index = text.find(delimiter)

        end_index = text.find(delimiter, start_index + len(delimiter))

        if end_index == -1:
            raise Exception(f"No closing delimiter found for {delimiter}")
        
        before_text = text[:start_index]

        delimiter_text = text[start_index + len(delimiter):end_index]


        after_text = text[end_index + len(delimiter):]

        if before_text:
            new_nodes.append(TextNode(before_text, TextType.TEXT))
        
        if delimiter_text:
            new_nodes.append(TextNode(delimiter_text, text_type))
        
        if after_text:
            result = split_nodes_delimiter([TextNode(after_text, TextType.TEXT)], delimiter, text_type)
            new_nodes.extend(result)
    
    
    return new_nodes















