class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"
import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario()

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: El ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            if self.guardar_inventario():
                print("Producto añadido exitosamente.")
            else:
                print("Error al guardar el producto en el archivo.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            if self.guardar_inventario():
                print("Producto eliminado exitosamente.")
            else:
                print("Error al guardar los cambios en el archivo.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            if self.guardar_inventario():
                print("Producto actualizado exitosamente.")
            else:
                print("Error al guardar los cambios en el archivo.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
            return True
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el inventario: {e}")
            return False

    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as file:
                    for linea in file:
                        id, nombre, cantidad, precio = linea.strip().split(',')
                        producto = Producto(id, nombre, int(cantidad), float(precio))
                        self.productos[id] = producto
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al cargar el inventario: {e}")
            except Exception as e:
                print(f"Error inesperado al cargar el inventario: {e}")
        else:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al añadir productos.")


def menu():
    #Carga todos los productos existentes
    file = open("inventario.txt", "r")
    print(file.read())

    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opción = input("Seleccione una opción: ")

        if opción == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opción == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opción == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opción == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opción == "5":
            inventario.mostrar_productos()

        elif opción == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
