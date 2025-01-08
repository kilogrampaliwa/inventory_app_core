import qrcode

def create_qr_code(url, file_name=None):
    """
    Generates a QR code from the given URL.

    Parameters:
        url (str): The HTTPS URL to encode in the QR code.
        file_name (str, optional): The name of the file to save the QR code image. If None, the image is shown instead.

    Returns:
        None
    """
    if not url.startswith("https://"):
        raise ValueError("The URL must start with 'https://'")

    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code; higher numbers = larger code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4)
    )

    qr.add_data(url)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    if file_name:
        img.save(file_name)  # Save the image to a file
        #print(f"QR code saved as {file_name}")
    else:
        img.show()  # Display the image