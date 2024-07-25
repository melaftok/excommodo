class DatabaseConnection:
    def __init__(self, catalog="staging", schema="lims"):
        self.catalog = catalog
        self.schema = schema
        # Additional initialization code can go here

    def connect(self):
        # Code to establish a database connection using self.catalog and self.schema
        pass

# Creating an instance of the DatabaseConnection class
db_connection = DatabaseConnection(catalog="production")
# The __init__ method is automatically called with catalog="production" and the default schema="lims"
