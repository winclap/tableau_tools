from setuptools import setup

setup(
    name='tableau_tools',
    python_requires='>=3.6',
    version='5.2.0',
    packages=['tableau_tools', 'tableau_tools.tableau_rest_api', 'tableau_tools.tableau_documents',
              'tableau_tools.examples', 'tableau_tools.tableau_rest_api.methods'],
    url='https://github.com/bryantbhowell/tableau_tools',
    license='',
    author='Bryant Howell',
    author_email='bhowell@tableau.com',
    description='A library for programmatically working with Tableau files and Tableau Server, including the REST API',
    install_requires=['requests'],
    # Workaround due to tableau_tools being in one level up
    package_dir={
        'tableau_tools': '../',
        'tableau_tools.tableau_rest_api': '.',
        'tableau_tools.tableau_documents': '.',
        'tableau_tools.examples': '.',
        'tableau_tools.tableau_rest_api.methods': '.'
    }
)
