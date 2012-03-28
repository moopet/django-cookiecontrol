from distutils.core import setup

setup(
    name='django-cookiecontrol',
    version='0.1.0',
    author='Ben Sinclair',
    description='Simple CookieControl wrapper as a Django Reusable Application',
    long_description=open('README').read(),
    author_email='ben@moopet.net',
    keywords='django cookiecontrol',
    install_requires=['django'],
    url='http://github.com/DrMegahertz/django-gravatar',
    packages=[
        'cookiecontrol',
        'cookiecontrol.templatetags',
    ],
    package_data={
        'cookiecontrol': [
            'templates/*',
            'static/cookiecontrol/js/*',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
