import hashlib

def calculate_sha256(input_string):
    # Encoding string data into standard byte arrays
    byte_data = input_string.encode('utf-8')
    # Processing through the secure hash engine
    sha256_hash = hashlib.sha256(byte_data)
    # Returning the calculated fixed-length hexadecimal digest
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    print("--- Cryptographic Hashing Demonstration Tool (SHA-256) ---")
    
    # Simulating data integrity verification
    original_message = "SecureDataPayload2026"
    hash_output = calculate_sha256(original_message)
    
    print(f"Original Text input: {original_message}")
    print(f"Generated Fixed-Length Hash (64 Hex chars):\n{hash_output}\n")
    
    # Testing the Avalanche Effect
    altered_message = "SecureDataPayload2026." # Small modification (added a dot)
    altered_hash = calculate_sha256(altered_message)
    
    print(f"Altered Text input:   {altered_message}")
    print(f"Mutated Avalanche Hash:\n{altered_hash}")
