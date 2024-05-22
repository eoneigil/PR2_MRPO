import xml.etree.ElementTree as ET
import xml.dom.minidom
from Repository.FakeRepository import FakeRepository
from Models.Product import Product
from Models.Category import Categoryes
from Models.Eating import Eating
from Models.Dish import Dish
import xml.etree.ElementTree as ET
from Repository.FakeRepository import FakeRepository
from Models.User import User
import xml.etree.ElementTree as ET

class XMLUserRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        users = []
        for user_element in self.root.findall(".//users/user"):
            users.append(self._xml_to_user(user_element))
        return users

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, user: User):
        users_element = self.root.find(".//users")
        if users_element is None:
            users_element = ET.SubElement(self.root, "users")
        new_user_element = ET.SubElement(users_element, "user")
        self._user_to_xml(user, new_user_element)
        self._save_xml()
        print(f"User {user.name} added with id={user.id}")

    def remove(self, user: User):
        user_element = self.root.find(".//users/user[id='{}']".format(user.id))
        if user_element is not None:
            self.root.find(".//users").remove(user_element)
            self._save_xml()

    def update(self, user: User):
        user_element = self.get(user.id)
        if user_element is not None:
            self.add(user)
            self.remove(user_element)
            self._save_xml()

    def _xml_to_user(self, user_element) -> User:
        id = int(user_element.find("id").text)
        age = int(user_element.find("age").text)
        gender = user_element.find("gender").text
        weight = float(user_element.find("weight").text)
        height = float(user_element.find("height").text)
        name = user_element.find("name").text
        activity = user_element.find("activity").text
        meals = []  # Пропуск разбора 'meals', потому что класс 'Eating' не определён
        return User(id=id, age=age, gender=gender, weight=weight, height=height, name=name, activity=activity, meals=meals)

    def _user_to_xml(self, user: User, user_element):
        id_element = user_element.find("id")
        if id_element is not None:
            id_element.text = str(user.id)
        else:
            id_element = ET.SubElement(user_element, "id")
            id_element.text = str(user.id)

        age_element = user_element.find("age")
        if age_element is not None:
            age_element.text = str(user.age)
        else:
            age_element = ET.SubElement(user_element, "age")
            age_element.text = str(user.age)

        gender_element = user_element.find("gender")
        if gender_element is not None:
            gender_element.text = user.gender
        else:
            gender_element = ET.SubElement(user_element, "gender")
            gender_element.text = user.gender

        weight_element = user_element.find("weight")
        if weight_element is not None:
            weight_element.text = str(user.weight)
        else:
            weight_element = ET.SubElement(user_element, "weight")
            weight_element.text = str(user.weight)

        height_element = user_element.find("height")
        if height_element is not None:
            height_element.text = str(user.height)
        else:
            height_element = ET.SubElement(user_element, "height")
            height_element.text = str(user.height)

        name_element = user_element.find("name")
        if name_element is not None:
            name_element.text = user.name
        else:
            name_element = ET.SubElement(user_element, "name")
            name_element.text = user.name

        activity_element = user_element.find("activity")
        if activity_element is not None:
            activity_element.text = user.activity
        else:
            activity_element = ET.SubElement(user_element, "activity")
            activity_element.text = user.activity

    def get_by_id(self, user_id):
        for user_element in self.root.findall(".//user"):
            id_element = user_element.find("id")
            if id_element is not None and int(id_element.text) == user_id:
                return self._xml_to_user(user_element)
        return None

class XMLDishRepository(FakeRepository):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        dishes = []
        for dish_element in self.root.findall(".//dishes/dish"):
            dishes.append(self._xml_to_dish(dish_element))
        return dishes

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, dish):
        dish_element = self.root.find(".//dishes")
        if dish_element is None:
            dish_element = ET.SubElement(self.root, "dishes")
        new_dish_element = ET.SubElement(dish_element, "dish")
        self._dish_to_xml(dish, new_dish_element)
        self._save_xml()

    def remove(self, dish: Dish):
        dish_element = self.root.find(".//dishes/dish[id='{}']".format(dish.id))
        if dish_element is not None:
            self.root.find(".//dishes").remove(dish_element)
            self._save_xml()

    def update(self, dish: Dish):
        dish_element = self.get(dish.id)
        if dish_element is not None:
            self.add(dish)
            self.remove(dish_element)
            self._save_xml()

    def _xml_to_dish(self, dish_element):
        id = int(dish_element.find("id").text)
        name = dish_element.find("name").text
        calorifik = float(dish_element.find("calorifik").text)
        protein = float(dish_element.find("protein").text)
        fat = float(dish_element.find("fat").text)
        carb = float(dish_element.find("carb").text)

        products_element = dish_element.find("products")
        products = {int(p.find("product_id").text): float(p.find("amount").text) for p in
                    products_element.findall("product")}

        category_element = dish_element.find("category")
        if category_element is not None:
            category = int(category_element.text)
        else:
            category = None  # Или любое другое значение по умолчанию, если категория отсутствует

        return Dish(id=id, name=name, calorifik=calorifik, protein=protein, fat=fat, carb=carb, products=products,
                    category=category)

    def _dish_to_xml(self, dish, dish_element):
        id_element = ET.SubElement(dish_element, "id")
        id_element.text = str(dish.id)

        name_element = ET.SubElement(dish_element, "name")
        name_element.text = dish.name

        calorifik_element = ET.SubElement(dish_element, "calorifik")
        calorifik_element.text = str(dish.calorifik)

        protein_element = ET.SubElement(dish_element, "protein")
        protein_element.text = str(dish.protein)

        fat_element = ET.SubElement(dish_element, "fat")
        fat_element.text = str(dish.fat)

        carb_element = ET.SubElement(dish_element, "carb")
        carb_element.text = str(dish.carb)

        products_element = ET.SubElement(dish_element, "products")
        for product_id, amount in dish.products.items():
            product_element = ET.SubElement(products_element, "product")
            product_id_element = ET.SubElement(product_element, "product_id")
            product_id_element.text = str(product_id)
            amount_element = ET.SubElement(product_element, "amount")
            amount_element.text = str(amount)

        category_element = ET.SubElement(dish_element, "category")
        category_element.text = str(dish.category)

    def get_by_id(self, dish_id):
        for dish_element in self.root.findall(".//dish"):
            id_element = dish_element.find("id")
            if id_element is not None and int(id_element.text) == dish_id:
                return self._xml_to_dish(dish_element)
        return None

    def get_by_name(self, name):
        for dish_element in self.root.findall(".//dish"):
            name_element = dish_element.find("name")
            if name_element is not None and name_element.text == name:
                return self._xml_to_dish(dish_element)
        return None

class XMLEatingRepository(FakeRepository):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        eatings = []
        for eating_element in self.root.findall(".//eatings/eating"):
            eatings.append(self._xml_to_eating(eating_element))
        return eatings

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, eating: Eating):
        eatings_element = self.root.find(".//eatings")
        if eatings_element is None:
            eatings_element = ET.SubElement(self.root, "eatings")
        new_eating_element = ET.SubElement(eatings_element, "eating")
        self._eating_to_xml(eating, new_eating_element)
        self._save_xml()

    def remove(self, eating: Eating):
        eating_element = self.root.find(".//eatings/eating[id='{}']".format(eating.id))
        if eating_element is not None:
            self.root.find(".//eatings").remove(eating_element)
            self._save_xml()

    def _xml_to_eating(self, eating_element) -> Eating:
        id = int(eating_element.find("id").text)
        user_id = int(eating_element.find("user_id").text)
        name = eating_element.find("name").text
        dish = eating_element.find("dish").text
        return Eating(id=id, user_id=user_id, name=name, dish=dish)

    def _eating_to_xml(self, eating: Eating, eating_element):
        id_element = eating_element.find("id")
        if id_element is not None:
            id_element.text = str(eating.id)
        else:
            id_element = ET.SubElement(eating_element, "id")
            id_element.text = str(eating.id)

        user_id_element = eating_element.find("user_id")
        if user_id_element is not None:
            user_id_element.text = str(eating.user_id)
        else:
            user_id_element = ET.SubElement(eating_element, "user_id")
            user_id_element.text = str(eating.user_id)

        name_element = eating_element.find("name")
        if name_element is not None:
            name_element.text = eating.name
        else:
            name_element = ET.SubElement(eating_element, "name")
            name_element.text = eating.name

        dish_element = eating_element.find("dish")
        if dish_element is not None:
            dish_element.text = str(eating.dish)
        else:
            dish_element = ET.SubElement(eating_element, "dish")
            dish_element.text = str(eating.dish)

    # def get_by_id(self, user_id):
    #     for user_element in self.root.findall(".//eating"):
    #         if user_element.attrib.get("id") == str(user_id):
    #             user = {
    #                 "id": int(user_element.attrib.get("id")),
    #                 "age": int(user_element.attrib.get("age")),
    #                 "gender": user_element.attrib.get("gender"),
    #                 "weight": float(user_element.attrib.get("weight")),
    #                 "height": float(user_element.attrib.get("height")),
    #                 "name": user_element.attrib.get("name"),
    #                 "activity": user_element.attrib.get("activity")
    #             }
    #             return user
    #     return None

class XMLCategoryRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = self._load_xml()
        self.categories = self._load_categories()

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("categories")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        return root

    def _load_categories(self):
        categories = []
        for category_element in self.root.findall("category"):
            categories.append(self._xml_to_category(category_element))
        return categories

    def _save_categories(self):
        root = ET.Element("categories")
        for category in self.categories:
            category_element = ET.SubElement(root, "category")
            self._category_to_xml(category, category_element)
        tree = ET.ElementTree(root)
        self._indent(root)
        tree.write(self.file_path, encoding="utf-8", xml_declaration=True)

    def _xml_to_category(self, category_element):
        category_id = int(category_element.find("id").text)
        category_name = category_element.find("name").text
        return {"id": category_id, "name": category_name}

    def _category_to_xml(self, category, category_element):
        id_element = ET.SubElement(category_element, "id")
        id_element.text = str(category["id"])
        name_element = ET.SubElement(category_element, "name")
        name_element.text = category["name"]

    def add(self, category_name):
        if not any(category["name"] == category_name for category in self.categories):
            new_id = max(category["id"] for category in self.categories) + 1 if self.categories else 1
            self.categories.append({"id": new_id, "name": category_name})
            self._save_categories()

    def remove(self, category_name):
        self.categories = [category for category in self.categories if category["name"] != category_name]
        self._save_categories()

    def get_by_id(self, category_id):
        for category in self.categories:
            if category["id"] == category_id:
                return category
        return None

    def get_all(self):
        return self.categories
class XMLProductRepository(FakeRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        products = []
        for product_element in self.root.findall(".//products/product"):
            products.append(self._xml_to_product(product_element))
        return products

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, product: Product):
        products_element = self.root.find(".//products")
        if products_element is None:
            products_element = ET.SubElement(self.root, "products")
        new_product_element = ET.SubElement(products_element, "product")
        self._product_to_xml(product, new_product_element)
        self._save_xml()

    def remove(self, product_name):
        self.products = [product for product in self.products if product["name"] != product_name]
        self._save_products()

    def _xml_to_product(self, product_element) -> Product:
        id = int(product_element.find("id").text)
        name = product_element.find("name").text
        return Product(id=id, name=name)

    def _product_to_xml(self, product: Product, product_element):
        id_element = product_element.find("id")
        if id_element is not None:
            id_element.text = str(product.id)
        else:
            id_element = ET.SubElement(product_element, "id")
            id_element.text = str(product.id)

        name_element = product_element.find("name")
        if name_element is not None:
            name_element.text = product.name
        else:
            name_element = ET.SubElement(product_element, "name")
            name_element.text = product.name

    def get_by_id(self, product_id):
        for product_element in self.root.findall(".//product"):
            if product_element.find("id").text == str(product_id):
                return self._xml_to_product(product_element)
        return None

    def get_by_name(self, name):
        for product_element in self.root.findall(".//product"):
            if product_element.find("name").text == name:
                return self._xml_to_product(product_element)
        return None