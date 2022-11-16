productos={ 1001: ["Producto 1", 10 , 100], 
            1002: ["Producto 2", 15 , 100],  
            1003: ["Producto 3", 12 , 100], 
            1004: ["Producto 4", 20 , 100], 
            1005: ["Producto 5", 22 , 100], 
}

def existe_producto(codigo):

    return codigo in productos
      
def ver_stock(codigo):
    if existe_producto(codigo):
        producto = productos[codigo]
        return producto[2]
    return None

def hay_stock(codigo, cantidad):
    stock = ver_stock(codigo)
    if stock is not None:
        if cantidad <= stock:
            return True
    return False

def comprar(codigo, cantidad):
    productos[codigo][2]= productos[codigo][2] - cantidad
    return productos[codigo]

def devolver(codigo, cantidad):
    productos[codigo][2]= productos[codigo][2] + cantidad
    return productos[codigo]

def ver_productos():
    return productos
               
    

