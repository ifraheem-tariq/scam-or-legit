print("       SCAM OR LEGIT?")
print("================================")
print("Check a message for warning signs.")
print("Please enter a sample message.")
print("Do not enter private information.")
print()

message = input("Enter message: ").lower()

warnings = ["urgent", "winner", "prize", "password",
            "click here", "free money"]

found = 0

for word in warnings:
    if word in message:
        print("Warning sign found:", word)
        found = found + 1

print()

if found >= 2:
    print("Result: Suspicious message!")
elif found == 1:
    print("Result: Be careful. Check the message.")
else:
    print("Result: No listed warning signs found.")

print("Warning signs detected:", found)
print("Remember: Always verify the sender!")
