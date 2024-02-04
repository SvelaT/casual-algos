BASE64CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqerstuvwxyz0123456789+/"
BASE64DICT = {character: index for index, character in enumerate(BASE64CHARS)}

def binaryToBase64(input_bytes):
    if type(input_bytes) != bytes:
         raise Exception("The input must be a bytes object")
    output_string = ""
    for i in range(0,len(input_bytes),3):
        output_string += BASE64CHARS[input_bytes[i] >> 2] 
        if i + 1 < len(input_bytes):
            output_string += BASE64CHARS[((input_bytes[i] & 3) << 4) | (input_bytes[i+1] >> 4)]
        else:
            return output_string + BASE64CHARS[(input_bytes[i] & 3) << 4] + "=="
        if i + 2 < len(input_bytes):
            output_string += BASE64CHARS[((input_bytes[i+1] & 15) << 2) | (input_bytes[i+2] >> 6)]
        else:
            return output_string + BASE64CHARS[(input_bytes[i+1] & 15) << 2] + "="
        output_string += BASE64CHARS[input_bytes[i+2] & 63]

    return output_string

def base64ToBinary(input_string):
    if type(input_string) != str:
         raise Exception("The input must be a string")
    output_bytes = b''

    for i in range(0,len(input_string),4):
        bytes_list = []
        bytes_list.append((BASE64DICT[input_string[i]] << 2) | (BASE64DICT[input_string[i+1]] >> 4))
        if input_string[i+2] != '=':
            bytes_list.append(((BASE64DICT[input_string[i+1]] & 15) << 4) | (BASE64DICT[input_string[i+2]] >> 2))
        if input_string[i+3] != '=':    
            bytes_list.append(((BASE64DICT[input_string[i+2]] & 3) << 6) | (BASE64DICT[input_string[i+3]]))
        output_bytes += bytes(bytes_list)

    return output_bytes

