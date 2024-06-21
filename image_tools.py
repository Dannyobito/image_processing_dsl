from PIL import Image
import os
import ply.lex as lex
import ply.yacc as yacc

# Lexer definitions for tokens
tokens = [
    'RESIZE', 'CONVERT', 'ROTATE', 'INPATH', 'OUTPATH',
    'INTEGER', 'FORMAT'
]

# Regular expression patterns for tokens
t_RESIZE = r'resize'
t_CONVERT = r'convert'
t_ROTATE = r'rotate'
t_INTEGER = r'\d+'

# Define how to match image format (case-insensitive)
def t_FORMAT(t):
    r'\b(?:JPEG|PNG|TIFF|BMP)\b'  # Match JPEG, PNG, TIFF, BMP in any case
    t.value = t.value.upper()  # Convert to uppercase for consistency
    return t


# Define how to match an input path
def t_INPATH(t):
    r'\".*?\"'  # Match paths enclosed in double quotes
    t.value = t.value.strip('"')  # Remove the quotes
    print(f"INPATH: {t.value}")  # Print the token value
    return t

# Define how to match an output path
def t_OUTPATH(t):
    r'\'[^\']*?\''  # Match paths enclosed in single quotes
    t.value = t.value.strip("'")  # Remove the quotes
    print(f"OUTPATH: {t.value}")  # Print the token value
    return t

# Ignore whitespace characters
t_ignore = ' \t'

# Handle errors during lexing
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parser definitions for grammar rules
def p_statement_resize(p):
    'statement : RESIZE INPATH OUTPATH INTEGER INTEGER'
    operation, inpath, outpath, width, height = p[1], p[2], p[3], int(p[4]), int(p[5])
    process_image(operation, inpath, outpath, width=width, height=height)

def p_statement_convert(p):
    'statement : CONVERT INPATH OUTPATH FORMAT'
    operation, inpath, outpath, new_format = p[1], p[2], p[3], p[4]
    process_image(operation, inpath, outpath, new_format=new_format)

def p_statement_rotate(p):
    'statement : ROTATE INPATH OUTPATH INTEGER'
    operation, inpath, outpath, degrees = p[1], p[2], p[3], int(p[4])
    process_image(operation, inpath, outpath, degrees=degrees)

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Existing image processing functions
def resize(image_path, output_path, width, height):
    """Resize the image to the specified dimensions."""
    try:
        with Image.open(image_path) as img:
            resized_img = img.resize((width, height))
            resized_img.save(output_path)
            print(f"Image resized and saved to {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")

def convert_format(image_path, output_path, new_format):
    """Convert the image to a different format."""
    try:
        with Image.open(image_path) as img:
            img.save(output_path, format=new_format.upper())
            print(f"Image converted to {new_format} and saved to {output_path}")
    except Exception as e:
        print(f"Error converting image format: {e}")

def rotate(image_path, output_path, degrees):
    """Rotate the image by the specified number of degrees."""
    try:
        with Image.open(image_path) as img:
            rotated_img = img.rotate(degrees, expand=True)
            rotated_img.save(output_path)
            print(f"Image rotated by {degrees} degrees and saved to {output_path}")
    except Exception as e:
        print(f"Error rotating image: {e}")

def process_image(operation, image_path, output_path, width=None, height=None, new_format=None, degrees=None):
    """Performs the specified image processing operation based on arguments."""

    # Validate input file existence
    if not os.path.exists(image_path):
        print(f"Error: Input file '{image_path}' does not exist.")
        return

    # Validate output directory and create it if necessary
    output_dir = os.path.dirname(output_path)
    if output_dir != "" and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Output directory '{output_dir}' created.")

    if operation == "resize":
        resize(image_path, output_path, width, height)
    elif operation == "convert":
        convert_format(image_path, output_path, new_format)
    elif operation == "rotate":
        rotate(image_path, output_path, degrees)
    else:
        print(f"Error: Unknown operation '{operation}'.")

# User interaction loop
while True:
    # Prompt the user for input
    user_input = input("Enter image processing command (or 'quit' to exit): ")

    # Check for quit command
    if user_input.lower() == "quit":
        break

    # Parse the user input using the parser
    parser.parse(user_input)

# End of program
print("Exiting image processing tool.")
