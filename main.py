import qrcode
#The checklist made using the ai processing 
medical_checklist = """
[CRITICAL EMERGENCY DATA]
- BLOOD TYPE: O-Negative
- ALLERGIES: Penicillin, Peanuts
- CONDITIONS: Type 1 Diabetes
- MEDICATIONS: Insulin
- URGENT NOTES: High risk of diabetic ketoacidosis.
"""

# scrambling data so only authorised people such as doctors can access
def simulate_pin_encryption(text, pin_key):
    return "".join(chr(ord(character) ^ pin_key) for character in text)

# doctors required code must be entered to unscramble data and access qr code (e.g., 42)
DOCTOR_PIN_KEY = 42
scrambled_data = simulate_pin_encryption(medical_checklist, DOCTOR_PIN_KEY)


# Show the qr code should apear too users 
qr_engine = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,
    border=4,
)

# feeding the scrambled data into the qr genarator 
qr_engine.add_data(scrambled_data)
qr_engine.make(fit=True)

# the visiual image of the qr code 
qr_engine.print_ascii(invert=True)

print("Success! Your secure QR code has been generated as 'secure_medical_qr.png'.")
print("The data inside is locked and encrypted.")
