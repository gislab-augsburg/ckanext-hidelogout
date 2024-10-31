from setuptools import setup, find_packages

setup(
    name='ckanext-hidelogout',
    version='0.1',
    description='A CKAN plugin to conditionally hide the logout button.',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [ckan.plugins]
        hidelogout=ckanext.hidelogout.plugin:HideLogoutButtonPlugin
    ''',
)
