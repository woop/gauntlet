import hashlib
import os
import sys
import time
from typing import List, Tuple


class Gauntlet:

    def __init__(self, key: str):
        self.key = self._process_key(key)

    @staticmethod
    def _process_key(key: str) -> str:
        return hashlib.sha256(key.encode()).hexdigest()

    @staticmethod
    def _generate_seed(length: int = 64) -> str:
        return os.urandom(length).hex()

    def _generate_signature(self, data: str, seed: str) -> str:
        return hashlib.sha512((data + self.key + seed).encode()).hexdigest()

    def secure_data(self, data: str) -> Tuple[str, str]:
        seed = self._generate_seed()
        signature = self._generate_signature(data, seed)
        return seed, signature

    def verify_data(self, data: str, seed: str, signature: str) -> bool:
        return self._generate_signature(data, seed) == signature


def process_data(data: List[str], key: str) -> List[Tuple[str, str]]:
    gauntlet = Gauntlet(key)
    return [gauntlet.secure_data(d) for d in data]


def verify_processed_data(data: List[str], key: str, seeds: List[str], signatures: List[str]) -> List[bool]:
    gauntlet = Gauntlet(key)
    return [gauntlet.verify_data(d, s, sig) for d, s, sig in zip(data, seeds, signatures)]


def main():
    if len(sys.argv) < 5:
        print("Usage: python gauntlet.py <action> <key> <input_file> <output_file>")
        sys.exit(1)

    action = sys.argv[1].lower()
    key = sys.argv[2]
    input_file = sys.argv[3]
    output_file = sys.argv[4]

    if action not in ["secure", "verify"]:
        print("Invalid action. Use 'secure' or 'verify'.")
        sys.exit(1)

    with open(input_file, "r") as f:
        data = f.readlines()

    if action == "secure":
        secured_data = process_data(data, key)
        with open(output_file, "w") as f:
            for line, (seed, signature) in zip(data, secured_data):
                f.write(f"{line.strip()}|{seed}|{signature}\n")

        print(f"Data secured and saved to {output_file}")

    elif action == "verify":
        seeds = []
        signatures = []
        original_data = []

        for line in data:
            parts = line.strip().split("|")
            original_data.append(parts[0])
            seeds.append(parts[1])
            signatures.append(parts[2])

        verification_results = verify_processed_data(original_data, key, seeds, signatures)

        with open(output_file, "w") as f:
            for line, verified in zip(original_data, verification_results):
                f.write(f"{line} - {'Verified' if verified else 'Not Verified'}\n")

        print(f"Verification results saved to {output_file}")


if __name__ == "__main__":
    main()
