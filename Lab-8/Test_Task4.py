from Task4 import ShoppingCart

def test_cart_initially_empty():
    cart = ShoppingCart()
    assert cart.total_cost() == 0

def test_add_single_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0)
    assert cart.total_cost() == 1.0
    assert cart.items["apple"]["quantity"] == 1

def test_add_multiple_items():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0)
    cart.add_item("banana", 0.5)
    assert cart.total_cost() == 1.5
    assert cart.items["banana"]["quantity"] == 1

def test_add_same_item_multiple_times():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0)
    cart.add_item("apple", 1.0)
    assert cart.items["apple"]["quantity"] == 2
    assert cart.total_cost() == 2.0

def test_remove_item_decreases_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0)
    cart.add_item("apple", 1.0)
    cart.remove_item("apple")
    assert cart.items["apple"]["quantity"] == 1
    assert cart.total_cost() == 1.0

def test_remove_item_removes_when_quantity_one():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0)
    cart.remove_item("apple")
    assert "apple" not in cart.items
    assert cart.total_cost() == 0

def test_remove_item_not_in_cart():
    cart = ShoppingCart()
    cart.remove_item("banana")  # Should not raise
    assert cart.total_cost() == 0