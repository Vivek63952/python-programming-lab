# PROGRAM TO GENERATE 6 DIGIT RANDOM SECURE OTP
import secrets

secretsGenerator = secrets.SystemRandom()

print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000, 999999)

print("Secure random OTP is ", otp)