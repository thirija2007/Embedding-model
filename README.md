# Embedding model

# Student Helpdesk RAG System

## Overview

The Student Helpdesk RAG System is a simple Retrieval-Augmented Generation (RAG) application that answers student-related questions using information stored in a local student policy document.

The project uses Hugging Face embeddings to convert text into numerical vectors, Chroma to store and retrieve relevant information, and Ollama with Llama 3.2 to generate answers.

## Features

* Converts text into numerical embeddings
* Uses `all-MiniLM-L6-v2` embedding model
* Creates 384-dimensional embeddings
* Splits the student policy into smaller chunks
* Stores document embeddings in Chroma
* Retrieves relevant information using similarity search
* Generates answers using Ollama Llama 3.2
* Answers only using information available in the student policy

## Technologies Used

* Python
* Sentence Transformers
* Scikit-learn
* LangChain
* Chroma
* Hugging Face Embeddings
* Ollama
* Llama 3.2

## Project Structure

```text
Rag_System/
│
├── embedding.py
├── rag.py
├── student_policy.txt
├── requirements.txt
└── README.md
```

## Embedding Process

The `embedding.py` program converts sentences into numerical vectors using the `all-MiniLM-L6-v2` model.

```text
Text
  ↓
Embedding Model
  ↓
Numerical Vector
  ↓
384 Dimensions
```

## RAG Process

The `rag.py` program follows this workflow:

```text
Student Policy
      ↓
Document Loading
      ↓
Text Splitting
      ↓
Embeddings
      ↓
Chroma Vector Database
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
Ollama Llama 3.2
      ↓
Answer
```

## Requirements

* Python 3.x
* Ollama
* Llama 3.2 model
* Internet connection for installing Python packages and downloading the embedding model

## Installation

### 1. Install Python packages

```bash
python -m pip install -r requirements.txt
```

### 2. Install Ollama

Install Ollama on Windows and verify the installation:

```bash
ollama --version
```

### 3. Download Llama 3.2

```bash
ollama pull llama3.2
```

### 4. Run the Embedding Program

```bash
python embedding.py
```

This converts the sample sentences into numerical embeddings.

### 5. Run the RAG Program

```bash
python rag.py
```

Enter a question when prompted.

## Example Questions

```text
What is the minimum attendance required for semester examinations?
```

```text
How many books can a student borrow from the library?
```

```text
How long can students keep library books?
```

```text
How can students apply for leave?
```

## Example Result

For the question:

```text
How many books can a student borrow from the library?
```

The system retrieves the relevant library information and generates an answer based on the student policy.

## Knowledge Base

The knowledge base is stored in:

```text
student_policy.txt
```

It contains information about:

* Attendance
* Leave
* Assignments
* Library
* Examinations
* Laboratory rules

## Conclusion

The Student Helpdesk RAG System demonstrates how embeddings, vector databases, retrieval, and a local Large Language Model can work together to answer questions from a custom knowledge base.
