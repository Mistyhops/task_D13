from django.core.management.base import BaseCommand, CommandError

from news.models import Post, Category


class Command(BaseCommand):
    help = 'Add category name to clear all posts from selected category'

    def add_arguments(self, parser):
        parser.add_argument('categories_name', nargs='+', type=str)

    def handle(self, *args, **options):
        for category in options['categories_name']:
            try:
                selected_category_posts = Post.objects.filter(category=Category.objects.get(name_category=category))
                selected_category_posts.delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted all post from {category} category'))
            except Category.DoesNotExist:
                raise CommandError(f'Category {category} does not exist')
