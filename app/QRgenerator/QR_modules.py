import qrcode
from io import BytesIO
import cv2

# Data to encode in the QR code
def gen_and_show_qr(content):
    data = str(content)

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO object
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')

    # Show the image (optional)
    img.show()

# value = {
#     "name" : "sairam",
#     "college" : "ssn"
# }
# gen_and_show_qr(value)


# Function to decode QR code from an image
def decode_qr(image):
    detector = cv2.QRCodeDetector()
    reval, _, _ = detector.detectAndDecode(image)
    return reval

# Function to capture video from laptop camera and decode QR codes in real-time
def decode_qr_from_camera():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale for better QR detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Decode QR code
        decoded_text = decode_qr(gray)

        # If QR code is detected, print the decoded text
        if decoded_text:
            print("Decoded QR code:", decoded_text)
            break

        # Display the frame
        cv2.imshow('frame', frame)

        # Check if 'q' is pressed to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Main function
if __name__ == "__main__":
    # Decode QR code from camera in real-time
    decode_qr_from_camera()

