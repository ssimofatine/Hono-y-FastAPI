from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
from models import obtener_productos, obtener_producto, buscar_productos

app = FastAPI(title="TechStore API")

@app.get("/")
def inicio():
    return FileResponse("public/index.html")

@app.get("/api/productos")
def listar_productos():
    return {"productos": obtener_productos()}

@app.get("/api/productos/{id}")
def obtener_prod(id: int):
    producto = obtener_producto(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"producto": producto}

@app.get("/api/buscar")
def buscar(texto: str = ""):
    return {"productos": buscar_productos(texto)}

@app.get("/producto")
def redirigir_producto(id: int):
    return RedirectResponse(f"/api/productos/{id}")