import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pizzaria Giorno Giovanna")
        # testando atualizacao QGroupBox
        self.clients = []

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
        self.workerID.addItems(["Augusto", "Marco", "Cícero"])

        layout = QVBoxLayout()
        layout.addWidget(self.workerID)

        groupBox.setLayout(layout)
        return groupBox

    def newClient(self):
        groupBox = QGroupBox("Novo Cliente")

        self.clientName = QLineEdit()
        self.clientPhone = QLineEdit()
        self.clientAddress = QLineEdit()
        saveClientButton = QPushButton("Salvar Cliente")
        saveClientButton.clicked.connect(self.saveClient)

        layout = QFormLayout()
        layout.addRow("Nome:", self.clientName)
        layout.addRow("Telefone:", self.clientPhone)
        layout.addRow("Endereço:", self.clientAddress)
        layout.addRow(saveClientButton)

        groupBox.setLayout(layout)
        return groupBox

    def newOrder(self):
        groupBox = QGroupBox("Novo Pedido")

        self.clientID = QComboBox()
        self.clientID.addItems(self.clients)  # testando atualizacao
        self.pizzaFlavor = QComboBox()
        self.pizzaFlavor.addItems(["Margherita", "Pepperoni", "Abacaxi"])
        self.pizzaSize = QComboBox()
        self.pizzaSize.addItems(["Pequena", "Média", "Grande"])
        self.pizzaCount = QComboBox()
        self.pizzaCount.addItems(["1", "2", "3"])
        savePizzaButton = QPushButton("Salvar Pizza")
        savePizzaButton.clicked.connect(self.savePizza)
        saveOrderButton = QPushButton("Salvar Pedido")
        saveOrderButton.clicked.connect(self.saveOrder)

        layout = QFormLayout()
        layout.addRow("Cliente:", self.clientID)
        layout.addRow("Sabor:", self.pizzaFlavor)
        layout.addRow("Tamanho:", self.pizzaSize)
        layout.addRow("Quantidade:", self.pizzaCount)
        layout.addRow(savePizzaButton)
        layout.addRow(saveOrderButton)

        groupBox.setLayout(layout)
        return groupBox

    def orderFinish(self):
        groupBox = QGroupBox("Pedidos")

        self.orderList = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.orderList)

        groupBox.setLayout(layout)
        return groupBox

    @Slot()
    def saveClient(self):
        name = self.clientName.text()
        phone = self.clientPhone.text()
        address = self.clientAddress.text()

        if name and phone and address:
            # testando update QGroupBox
            self.clients.append(phone)
            self.clientID.clear()
            self.clientID.addItems(self.clients)
            print(self.clients)

            print(f"{name}, {phone}, {address}")
            self.clientName.clear()
            self.clientPhone.clear()
            self.clientAddress.clear()
        else:
            print("Preencha todos os campos do cliente!")

    @Slot()
    def savePizza(self):
        flavor = self.pizzaFlavor.currentText()
        size = self.pizzaSize.currentText()
        count = self.pizzaCount.currentText()

        if flavor and size and count:
            print(f"{flavor}, {size}, {count}")
            self.orderList.addItem(flavor)
            self.orderList.addItem(size)
            self.orderList.addItem(count)
        else:
            print("Preencha todos os campos da pizza!")

    @Slot()
    def saveOrder(self):
        client = self.clientID.currentText()
        worker = self.workerID.currentText()

        if client and worker:
            print(f"{worker}, {client}")
            self.orderList.addItem(client)
            self.orderList.addItem(worker)
        else:
            print("Preencha todos os campos do pedido!")


if __name__ == "__main__":
    app = QApplication([])

    widget = MainWidget()
    widget.show()

    sys.exit(app.exec())
