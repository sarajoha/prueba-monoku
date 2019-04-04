from polls.models import Product, Consumption

def run():
    products = Product.objects.all()
    quantities = [4, 8, 12, 16, 20] #should add 24 and 32

    for product in products:
        for value in quantities:
            Consumption.objects.create(quantity=value, product=product)
