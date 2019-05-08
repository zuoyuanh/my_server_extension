from setuptools import setup, find_packages

setup(
    name='myextension',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('etc/jupyter/jupyter_server_config.d', [
            'jupyter-config/jupyter_server_config.d/myextension.json'
        ])
    ],
    zip_safe=False
)