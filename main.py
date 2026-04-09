fromfastapiimportFastAPI
importtime

app=FastAPI()

@app.get("/hello")
defhello():
return {"message":"hello"}

@app.get("/slow")
defslow():
time.sleep(2)
return {"message":"slow"}
