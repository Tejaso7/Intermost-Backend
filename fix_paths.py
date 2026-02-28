"""Fix image paths in MongoDB by adding leading slashes."""
import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import django
django.setup()
from apps.mongodb import get_collection

# Fix image paths in countries
countries = get_collection('countries')
for country in countries.find():
    updates = {}
    if country.get('hero_image') and not country['hero_image'].startswith('/') and not country['hero_image'].startswith('http'):
        updates['hero_image'] = '/' + country['hero_image']
    if country.get('banner_image') and not country['banner_image'].startswith('/') and not country['banner_image'].startswith('http'):
        updates['banner_image'] = '/' + country['banner_image']
    if country.get('hero_video') and not country['hero_video'].startswith('/') and not country['hero_video'].startswith('http'):
        updates['hero_video'] = '/' + country['hero_video']
    if updates:
        countries.update_one({'_id': country['_id']}, {'$set': updates})
        print(f'Fixed: {country["name"]}')

# Fix image paths in colleges
colleges = get_collection('colleges')
for college in colleges.find():
    updates = {}
    if college.get('images', {}).get('main') and not college['images']['main'].startswith('/') and not college['images']['main'].startswith('http'):
        updates['images.main'] = '/' + college['images']['main']
    if college.get('images', {}).get('banner') and not college['images']['banner'].startswith('/') and not college['images']['banner'].startswith('http'):
        updates['images.banner'] = '/' + college['images']['banner']
    if updates:
        colleges.update_one({'_id': college['_id']}, {'$set': updates})
        print(f'Fixed college: {college["name"]}')

print('Done fixing image paths!')
