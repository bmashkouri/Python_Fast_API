from FastAPI import FastAPI
app=FastAPI()


@app.get("/")


asynce def root():
    return{"massage":"hello pouya son of the moon"}