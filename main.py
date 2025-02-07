import sys
import sqlite3
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QSpinBox,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
)


def initDatabase():
    with open("./pizzaria.sql", "r") as file:
        pizzaria = file.read()

    con = sqlite3.connect("./pizzaria.db")
    cur = con.cursor()
    cur.executescript(pizzaria)
    con.commit()
    con.close()


class Worker:
    def __init__(self):
        pass

    def listWorkers(self):
        con = sqlite3.connect("./pizzaria.db")
        cur = con.cursor()
        res = cur.execute("SELECT id, name FROM worker;")
        rows = res.fetchall()
        con.close()

        return [f"{row[0]}. {row[1]}" for row in rows]


class Client:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""

    def listClients(self):
        con = sqlite3.connect("./pizzaria.db")
        cur = con.cursor()
        res = cur.execute("SELECT id, name, phone, address FROM client;")
        rows = res.fetchall()
        con.close()

        return [f"{row[0]}. {row[1]} | {row[2]} | {row[3]}" for row in rows]

    def addClient(self):
        con = sqlite3.connect("./pizzaria.db")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO client (name, phone, address) VALUES(?, ?, ?);",
            (self.name, self.phone, self.address),
        )
        con.commit()
        con.close()


class Pizza:
    def __init__(self):
        self.top = ""
        self.size = ""
        self.quant = ""

    def addPizza(self):
        con = sqlite3.connect("./pizzaria.db")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO pizza (quantity, topping_id, size_id) VALUES
            (?,
            (SELECT id FROM topping WHERE name=?),
            (SELECT id FROM size WHERE name=?));""",
            (self.count, self.top, self.size),
        )
        con.commit()
        con.close()

    def valuePizza(self):
        con = sqlite3.connect("./pizzaria.db")
        cur = con.cursor()
        res = cur.execute(
            """SELECT quantity*price*factor
            FROM pizza, size, topping
            WHERE
            pizza.id=(SELECT MAX(pizza.id) FROM pizza)
            AND
            size.name=?
            AND
            topping.name=?;""",
            (self.size, self.top),
        )
        rows = res.fetchone()
        con.close()

        return f"{rows[0]}"

    def listTop(self):
        con = sqlite3.connect("./pizzaria.db")
        cur = con.cursor()
        res = cur.execute("SELECT name FROM topping;")
        rows = res.fetchall()
        con.close()

        return [f"{row[0]}" for row in rows]

    def listSizes(self):
        con = sqlite3.connect("./pizzaria.db")
        cur = con.cursor()
        res = cur.execute("SELECT name FROM size;")
        rows = res.fetchall()
        con.close()

        return [f"{row[0]}" for row in rows]


class Items:
    def __init__(self):
        pass

    def addOrderItems(self):
        con = sqlite3.connect("./pizzaria.db")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO order_item (order_id, pizza_id) VALUES
            (
            (SELECT MAX(id) FROM orders),
            (SELECT MAX(id) FROM pizza)
            );"""
        )
        con.commit()
        con.close()


class Order:
    def __init__(self):
        self.workerID = ""
        self.clientID = ""

    def addOrder(self):
        con = sqlite3.connect("./pizzaria.db")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO orders (worker_id, client_id) VALUES
            (?, ?);""",
            (self.workerID[0], self.clientID[0]),
        )
        con.commit()
        con.close()


class MainWidget(QWidget):
    def __init__(self, myWorker, myClient, myPizza, myItems, myOrder):
        super().__init__()

        self.myWorker = myWorker
        self.myClient = myClient
        self.myPizza = myPizza
        self.myItems = myItems
        self.myOrder = myOrder

        self.setWindowTitle("Pizzaria Giorno Giovanna")

        self.active = 0
        self.value = []

        selectWorker = self.selectWorker()
        newClient = self.newClient()
        newOrder = self.newOrder()
        orderFinish = self.orderFinish()

        layout = QHBoxLayout(self)
        layout.addWidget(selectWorker)
        layout.addWidget(newClient)
        layout.addWidget(newOrder)
        layout.addWidget(orderFinish)

    def selectWorker(self):
        groupBox = QGroupBox("Atendente")

        self.workerID = QComboBox()
        self.workerID.addItems(self.myWorker.listWorkers())

        layout = QVBoxLayout()
        layout.addWidget(self.workerID)

        groupBox.setLayout(layout)
        return groupBox

    def newClient(self):
        groupBox = QGroupBox("Novo Cliente")

        self.newClientName = QLineEdit()
        self.newClientPhone = QLineEdit()
        self.newClientAddress = QLineEdit()
        saveClientButton = QPushButton("Salvar Cliente")
        saveClientButton.clicked.connect(self.saveClient)

        layout = QFormLayout()
        layout.addRow("Nome:", self.newClientName)
        layout.addRow("Telefone:", self.newClientPhone)
        layout.addRow("Endereço:", self.newClientAddress)
        layout.addRow(saveClientButton)

        groupBox.setLayout(layout)
        groupBox.setMinimumSize(300, 500)
        return groupBox

    def newOrder(self):
        groupBox = QGroupBox("Novo Pedido")

        self.clientID = QComboBox()
        self.clientID.addItems(self.myClient.listClients())
        activeOrderButton = QPushButton("Iniciar Pedido")
        activeOrderButton.clicked.connect(self.activeOrder)
        self.pizzaTop = QComboBox()
        self.pizzaTop.addItems(self.myPizza.listTop())
        self.pizzaSize = QComboBox()
        self.pizzaSize.addItems(self.myPizza.listSizes())
        self.pizzaCount = QSpinBox()
        self.pizzaCount.setValue(1)
        savePizzaButton = QPushButton("Salvar Pizza")
        savePizzaButton.clicked.connect(self.savePizza)
        saveOrderButton = QPushButton("Salvar Pedido")
        saveOrderButton.clicked.connect(self.saveOrder)

        layout = QFormLayout()
        layout.addRow("Cliente:", self.clientID)
        layout.addRow(activeOrderButton)
        layout.addRow("Sabor:", self.pizzaTop)
        layout.addRow("Tamanho:", self.pizzaSize)
        layout.addRow("Quantidade:", self.pizzaCount)
        layout.addRow(savePizzaButton)
        layout.addRow(saveOrderButton)

        groupBox.setLayout(layout)
        groupBox.setMinimumSize(300, 500)
        return groupBox

    def orderFinish(self):
        groupBox = QGroupBox("Pedidos")

        self.orderText = QTextEdit()
        self.orderText.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.orderText)

        groupBox.setLayout(layout)
        groupBox.setMinimumSize(500, 500)
        return groupBox

    @Slot()
    def saveClient(self):
        self.myClient.name = self.newClientName.text()
        self.myClient.phone = self.newClientPhone.text()
        self.myClient.address = self.newClientAddress.text()

        if self.myClient.name and self.myClient.phone and self.myClient.address:
            self.myClient.addClient()
            self.clientID.clear()
            self.clientID.addItems(self.myClient.listClients())
            self.newClientName.clear()
            self.newClientPhone.clear()
            self.newClientAddress.clear()
            print("Novo cliente cadastrado!")
        else:
            print("Preencha todos os campos do cliente!")

    @Slot()
    def activeOrder(self):
        self.myOrder.workerID = self.workerID.currentText()
        self.myOrder.clientID = self.clientID.currentText()

        if self.myOrder.workerID and self.myOrder.clientID and not self.active:
            self.active = 1
            self.orderText.clear()
            self.myOrder.addOrder()
            self.orderText.append(f"#### Cliente ####\n{self.myOrder.clientID}\n")
            self.orderText.append(f"#### Atendente ####\n{self.myOrder.workerID}\n")
            self.orderText.append("Sabor | Tamanho | Quantidade | Valor")
        else:
            print("Preencha todos os campos do pedido! Ou finalize o pedido ativo!")

    @Slot()
    def savePizza(self):
        self.myPizza.top = self.pizzaTop.currentText()
        self.myPizza.size = self.pizzaSize.currentText()
        self.myPizza.count = self.pizzaCount.cleanText()

        if (
            self.active
            and self.myPizza.top
            and self.myPizza.size
            and float(self.myPizza.count) > 0
        ):
            self.myPizza.addPizza()
            self.value.append(float(self.myPizza.valuePizza()))
            self.myItems.addOrderItems()

            self.orderText.append(
                f"{self.myPizza.top} | {self.myPizza.size} | {self.myPizza.count} | {self.value[-1]}"
            )
        else:
            print("Inicie um pedido! Ou preencha todos os campos da pizza!")

    @Slot()
    def saveOrder(self):
        if self.active:
            self.active = 0
            self.orderText.append(f"\n#### TOTAL ####\n{sum(self.value)}")
            self.value.clear()
        else:
            print("Preencha todos os campos do pedido! Ou inicie um novo pedido!")


if __name__ == "__main__":
    initDatabase()

    app = QApplication([])

    myWorker = Worker()
    myClient = Client()
    myPizza = Pizza()
    myItems = Items()
    myOrder = Order()

    widget = MainWidget(myWorker, myClient, myPizza, myItems, myOrder)
    widget.show()

    sys.exit(app.exec())
