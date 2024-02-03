BASE64CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqerstuvwxyz0123456789+/"

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
         
