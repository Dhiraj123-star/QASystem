
# QASystem  
A question-answering system that processes CSV files containing questions, stores embeddings in Chroma, generates answers using OpenAI, and persists question-answer pairs in a relational database. Query answers are enhanced with vector similarity search.  

✨ **Features**  
- **Fast CSV Parsing**: Uses Polars for efficient CSV processing.  
- **Vector Search**: Chroma for storing and querying question embeddings.  
- **AI-Powered Answers**: OpenAI for embeddings (text-embedding-3-small) and answers 
(gpt-4o-mini).  
- **Database Storage**: SQLAlchemy with SQLite (dev) or Postgres (prod) for question-answer persistence.  
- **REST API**: FastAPI for uploading CSVs and querying answers.  
- **Containerized**: Docker with Gunicorn/Uvicorn for deployment.  
- **Secure Configuration**: Environment variables managed with python-dotenv.  


📊 **Tech Stack**

* FastAPI: REST API framework
* Polars: Fast CSV parsing
* OpenAI API: Embeddings and answer generation
* Chroma: Vector database
* SQLAlchemy: ORM for SQLite/Postgres
* python-dotenv: Environment variable management
* Gunicorn/Uvicorn: Production-ready server
* Docker: Containerization

