from fastapi import FastAPI
from predict_ecom import *

app = FastAPI(title="ECOMM API", description="Predict the category of the comment or text", version="1.0")


@app.post("/query/")
def expose_endpont(text):
    predicted_class = predict_category(text)
    category_mapping = {0: "Books", 1: "Clothing & Accessories", 2: "Electronics", 3: "Household"}

    predicted_category_name = category_mapping[predicted_class]
    return {'category': predicted_category_name}

if __name__=="__main__":
    # text = 'can not buy an item related to earpin'
    # x = expose_endpont(text)
    # print(x)
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)