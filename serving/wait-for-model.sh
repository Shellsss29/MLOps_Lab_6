MODEL_PATH="/model/model.pkl"

echo "Waiting for model file to be created..."

# Wait until file exists and is non-empty
while [ ! -s "$MODEL_PATH" ]; do
    sleep 1
done

echo "Model found! Starting API..."
uvicorn app:app --host 0.0.0.0 --port 8000
