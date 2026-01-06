**MULTITHREADED FILE COMPRESSION UTILITY (Python)**

**Project Overview**

This project implements a Multithreaded File Compression and Decompression Utility using Python, designed to efficiently handle large files by leveraging parallel processing. The utility divides a file into smaller chunks, processes each chunk concurrently using multiple threads, and then merges the results while maintaining correct order and data integrity.

A simple yet effective Run-Length Encoding (RLE) algorithm is used for compression, making the project easy to understand while demonstrating core concepts of multithreading, synchronization, and file I/O.

**Objectives**

1.To implement parallel file compression and decompression using multithreading


2.To reduce execution time compared to single-threaded processing

3.To demonstrate thread synchronization and correct data ordering

4.To provide a user-friendly web interface for file upload and download

**Key Concepts Used**

1.Multithreading (Python threading module)

2.File Segmentation (Chunk-based processing)

3.Synchronization (Thread joining and ordered output)

4.Run-Length Encoding (RLE)

5.File I/O Operations

6.Flask Web Framework

 **Technologies Used**

1.Programming Language: Python

2.Framework: Flask



 **System Architecture / Workflow**

1.User uploads a file via web interface

2.File is saved on the server

3.File is split into fixed-size chunks

4.Each chunk is processed in a separate thread

5.Chunks are compressed/decompressed using RLE

6.Threads are synchronized

7.Processed chunks are merged in correct order

8.Final output file is generated and downloaded

**Project Structure**
├── app.py                      
├── multithreaded_compressor.py 
├── templates/
│   └── index.html              
├── uploads/                   
├── output/                     
└── README.md  
