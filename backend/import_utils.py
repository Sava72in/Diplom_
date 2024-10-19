import yaml
from django.core.exceptions import ObjectDoesNotExist
from .models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter


def import_products_from_yaml(file_path):
    """
    Импорт товаров из YAML-файла в базу данных Django.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    shop_name = data.get('shop')
    try:
        shop, created = Shop.objects.get_or_create(name=shop_name)
        if created:
            print(f"Shop '{shop_name}' created")
    except Exception as e:
        print(f"Error creating shop: {e}")
        return

    for category_data in data.get('categories', []):
        category_id = category_data.get('id')
        category_name = category_data.get('name')
        category, created = Category.objects.get_or_create(
            id=category_id,
            defaults={'name': category_name}
        )
        if created:
            print(f"Category '{category_name}' created")

        shop.categories.add(category)

    for product_data in data.get('goods', []):
        category_id = product_data.get('category')
        category = Category.objects.filter(id=category_id).first()

        if category is None:
            print(f"Category with id {category_id} not found for product {product_data.get('name')}")
            continue

        product_name = product_data.get('name')
        product_model = product_data.get('model')
        product, created = Product.objects.get_or_create(
            name=product_name,
            defaults={'category': category}
        )
        if created:
            print(f"Product '{product_name}' created")

        price = product_data.get('price')
        price_rrc = product_data.get('price_rrc')
        quantity = product_data.get('quantity')
        product_info = ProductInfo.objects.create(
            product=product,
            shop=shop,
            price=price,
            price_rrc=price_rrc,
            quantity=quantity
        )
        print(f"ProductInfo for '{product_name}' created")

        parameters = product_data.get('parameters', {})
        for param_name, param_value in parameters.items():
            parameter, created = Parameter.objects.get_or_create(
                name=param_name
            )
            if created:
                print(f"Parameter '{param_name}' created")

            ProductParameter.objects.create(
                product_info=product_info,
                parameter=parameter,
                value=param_value
            )
            print(f"ProductParameter for '{param_name}' added to '{product_name}'")

