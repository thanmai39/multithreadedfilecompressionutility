import os
import threading


class MultithreadedCompressor:
    def __init__(self, chunk_size=1024 * 1024):  # we can change default chunk size from 1mb to other sizes
        self.chunk_size = chunk_size

    def run_length_encode(self, data):
        """Compress data using Run-Length Encoding (RLE)."""
        encoded = []
        prev_char = None
        count = 0

        for char in data.decode():
            if char == prev_char:
                count += 1
            else:
                if prev_char is not None:
                    encoded.append(f"{count}{prev_char}")
                prev_char = char
                count = 1

        # Append the last sequence
        if prev_char is not None:
            encoded.append(f"{count}{prev_char}")

        return ''.join(encoded).encode()

#decompressing function decoding
    def run_length_decode(self, data):
        """Decompress data using Run-Length Encoding (RLE)."""
        decoded = []
        char_count = ""
        prev_char = None  # Initialize prev_char

        for char in data.decode():
            if char.isdigit():
                char_count += char
            else:
                if prev_char and char_count:  # Decode the previous character
                    decoded.append(prev_char * int(char_count))
                prev_char = char
                char_count = ""

        # Decode the last character sequence
        if prev_char and char_count:
            decoded.append(prev_char * int(char_count))

        return ''.join(decoded).encode()

    def process_chunk(self, chunk, operation, results, index):
        """Compress or decompress a chunk."""
        try:
            if operation == "compress":
                results[index] = self.run_length_encode(chunk)
            elif operation == "decompress":
                results[index] = self.run_length_decode(chunk)
        except Exception as e:
            results[index] = None
            print(f"Error processing chunk {index}: {e}")

    def compress_file(self, input_file, output_file):
        """Compress a large file using multithreading."""
        file_size = os.path.getsize(input_file)
        num_chunks = (file_size + self.chunk_size - 1) // self.chunk_size

        with open(input_file, 'rb') as f:
            chunks = [f.read(self.chunk_size) for _ in range(num_chunks)]

        results = [None] * num_chunks
        threads = []

        for i, chunk in enumerate(chunks):
            thread = threading.Thread(target=self.process_chunk, args=(chunk, "compress", results, i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        with open(output_file, 'wb') as f:
            for i, result in enumerate(results):
                if result is None:
                    print(f"Skipping invalid chunk {i}")
                    continue
                f.write(result)

        print(f"File compressed successfully to {output_file}")

    def decompress_file(self, input_file, output_file):
        """Decompress a large file using multithreading."""
        file_size = os.path.getsize(input_file)
        num_chunks = (file_size + self.chunk_size - 1) // self.chunk_size

        with open(input_file, 'rb') as f:
            chunks = [f.read(self.chunk_size) for _ in range(num_chunks)]

        results = [None] * num_chunks
        threads = []

        for i, chunk in enumerate(chunks):
            thread = threading.Thread(target=self.process_chunk, args=(chunk, "decompress", results, i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        with open(output_file, 'wb') as f:
            for i, result in enumerate(results):
                if result is None:
                    print(f"Skipping invalid chunk {i}")
                    continue
                f.write(result)

        print(f"File decompressed successfully to {output_file}")


if __name__ == "__main__":
    compressor = MultithreadedCompressor()

    input_file = "large_file.txt" #this part is not require my dear i will modify😁
    compressed_file = "compressed_file.rle"
    decompressed_file = "decompressed_file.txt"

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
    else:
        # Compress the file
        compressor.compress_file(input_file, compressed_file)

        # Decompress the file
        compressor.decompress_file(compressed_file, decompressed_file)
