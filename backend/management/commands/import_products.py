from django.core.management.base import BaseCommand
from backend.import_utils import import_products_from_yaml

class Command(BaseCommand):
    help = 'Импорт товаров из YAML файла'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Путь к YAML файлу для импорта товаров')

    def handle(self, *args, **options):
        file_path = options['file_path']
        try:
            import_products_from_yaml(file_path)
            self.stdout.write(self.style.SUCCESS(f'Импорт товаров из {file_path} завершён успешно!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при импорте товаров: {e}'))
