# README

```bash
brew install duckdb
```

```bash
docker build . -t hungovercoders/duckstream:latest
docker run -d -p 8501:8501 --name duckstream hungovercoders/duckstream:latest
docker login
docker push hungovercoders/duckstream:latest
```
