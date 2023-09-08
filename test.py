import tkinter as tk

class Item:
    def __init__(self, name, price, brand, model_year):
        self.name = name
        self.price = price
        self.brand = brand
        self.model_year = model_year

class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.categories = {
            'Home appliances': [],
            'Electronics': [],
            'Fashion': [],
            'Books': [],
            'Sports': []
        }
        self.cart = []

        self.setup_home_frame()

    def add_to_cart(self, item):
        self.cart.append(item)
        self.display_items('Cart', self.cart)

    def remove_from_cart(self, item):
        self.cart.remove(item)
        self.display_items('Cart', self.cart)

    def update_cart_ui(self):
        if hasattr(self, 'cart_frame'):
            self.cart_frame.destroy()

        self.cart_frame = tk.Frame(self.root)
        self.cart_frame.pack()

        tk.Label(self.cart_frame, text="Shopping Cart", font=('Helvetica', 16)).pack(pady=10)

        for item in self.cart:
            cart_item_frame = tk.Frame(self.cart_frame)
            cart_item_frame.pack(fill='x')

            tk.Label(cart_item_frame, text=item.name).pack(side='left')
            tk.Label(cart_item_frame, text=f"Price: {item.price}").pack(side='left')
            tk.Button(cart_item_frame, text="Remove from Cart", command=lambda i=item: self.remove_from_cart(i)).pack(side='right')

    def setup_home_frame(self):
        if hasattr(self, 'home_frame'):
            self.home_frame.destroy()

        self.home_frame = tk.Frame(self.root)
        self.home_frame.pack()

        tk.Label(self.home_frame, text="Welcome to Online Shopping System", font=('Helvetica', 16)).pack(pady=10)

        for category in self.categories.keys():
            btn = tk.Button(self.home_frame, text=category, command=lambda c=category: self.setup_category_frame(c))
            btn.pack(pady=2)

        tk.Button(self.home_frame, text="View Cart", command=self.update_cart_ui).pack(pady=10)

    def setup_category_frame(self, category):
        if hasattr(self, 'category_frame'):
            self.category_frame.destroy()

        self.category_frame = tk.Frame(self.root)
        self.category_frame.pack()

        tk.Label(self.category_frame, text=f"Category: {category}", font=('Helvetica', 14)).pack(pady=10)

        self.search_var = tk.StringVar()
        tk.Entry(self.category_frame, textvariable=self.search_var).pack(side='left')
        tk.Button(self.category_frame, text="Search", command=lambda: self.search_item(category)).pack(side='left')
        tk.Button(self.category_frame, text="Sort", command=lambda: self.sort_items(category)).pack(side='left')
        tk.Button(self.category_frame, text="Back to Home", command=self.setup_home_frame).pack(side='right')

        self.items_display_frame = tk.Frame(self.category_frame)
        self.items_display_frame.pack()
        self.display_items(category)

    def search_item(self, category):
        target = self.search_var.get()
        items = self.categories[category]

        found_items = [item for item in items if target.lower() in item.name.lower()]

        if found_items:
            self.display_items(category, found_items)
        else:
            tk.Label(self.items_display_frame, text="No items found", fg='red').pack()

    def sort_items(self, category):
        items = self.categories[category]
        attr = 'name'  # Change this to the attribute you want to sort by
        self.quick_sort(items, attr)
        self.display_items(category, items)

    def display_items(self, category, items=None):
        # Destroy previous items display and create new based on updated list
        if hasattr(self, 'items_display_frame'):
            self.items_display_frame.destroy()
        self.items_display_frame = tk.Frame(self.category_frame)
        self.items_display_frame.pack()

        items = items or self.categories[category]
        for item in items:
            item_frame = tk.Frame(self.items_display_frame)
            item_frame.pack(fill='x')

            tk.Label(item_frame, text=item.name).pack(side='left')
            tk.Label(item_frame, text=f"Price: {item.price}").pack(side='left')
            tk.Button(item_frame, text="Add to Cart", command=lambda i=item: self.add_to_cart(i)).pack(side='right')

    def quick_sort(self, items, attr, low=None, high=None):
        if low is None:
            low = 0
        if high is None:
            high = len(items) - 1

        def partition(arr, low, high):
            i = low - 1
            pivot = getattr(arr[high], attr)

            for j in range(low, high):
                if getattr(arr[j], attr) <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        if low < high:
            pi = partition(items, low, high)
            self.quick_sort(items, attr, low, pi - 1)
            self.quick_sort(items, attr, pi + 1, high)

    def binary_search(self, items, target):
        left, right = 0, len(items) - 1
        while left <= right:
            middle = (left + right) // 2
            if items[middle].name == target:
                return items[middle]
            elif items[middle].name < target:
                left = middle + 1
            else:
                right = middle - 1
        return None

# if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    
    electronics_items = [
        Item("Laptop", 799.99, "HP", 2023),
        Item("Smartphone", 499.99, "Samsung", 2023),
        Item("Tablet", 299.99, "Apple", 2023),
        Item("TV", 599.99, "Sony", 2022),
    ]
    
    home_appliances_items = [
        Item("Refrigerator", 699.99, "LG", 2022),
        Item("Washing Machine", 399.99, "Whirlpool", 2022),
        Item("Freezer", 209, "universal", 2023),
        Item("Air Conditioning", 100, "careir", 2023),
        Item("Plower",99, "Spalding", 2023),
        Item("microwave", 2499, "Elaraby", 2023),
        
    ]
    
    fashion_items = [
        Item("T-Shirt", 190.99, "P&G", 2023),
        Item("Jeans", 390.99, "Levi's", 2023),
        Item("Skirt", 209, "Spalding", 2023),
        Item("Dresses", 100, "Spalding", 2023),
        Item("shoes",99, "Nike", 2023),
        Item("Bracelet", 2.499, "Spalding", 2023),
        Item("Boat", 4.99, "Spalding", 2023),
        Item("Casket", 299, "Cottoniel", 2023),
    ]
    
    books_items = [
        Item("Python Programming", 29.99, "O'Reilly", 2023),
        Item("The Great Gatsby", 9.99, "Scribner", 1925),
        Item("الاب الغني والاب الفقير", 209, "Spalding", 2023),
        Item("الاربعون للشقيري", 100, "Spalding", 2023),
        Item("Eat the Forg",99, "Spalding", 2023),
        
    ]
    
    sports_items = [
        Item("Soccer Ball", 14.99, "Adidas", 2023),
        Item("Basketball", 20.99, "Spalding", 2023),
        Item("ball", 29, "Spalding", 2023),
        Item("Basket", 249, "Spalding", 2023),
        Item("Volley", 209, "Spalding", 2023),
        Item("Kung-Fu", 100, "Spalding", 2023),
        Item("Kick-Boxing",99, "Spalding", 2023),  
    ]
    app.categories['Electronics'].extend(electronics_items)
    app.categories['Home appliances'].extend(home_appliances_items)
    app.categories['Fashion'].extend(fashion_items)
    app.categories['Books'].extend(books_items)
    app.categories['Sports'].extend(sports_items)
    

    root.mainloop()