
import click
from api.models import db, User, Inventory, Scheduling, Order

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""

def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    
    @app.cli.command("insert-test-users") # name of our command
    @click.argument("count") # argument of out command
    def insert_test_data(count):
        print("Creating test users")
        for x in range(1, int(count) + 1):
            user = User()
            user.id = x
            user.email = "test_user" + " " + str(x) + "@test.com"
            user.name = "manuel" + " " + str(x)
            user.last_name = "villate" + " " +  str(x) 
            user.password = "123456"
            user.address = "algun lugar" + " " +  str(x)
            user.is_active = True
            user.type = "biker" 
            db.session.add(user)
            db.session.commit()
            print("User: ", user.email, " created.")

        print("All test users created")

        ### Insert the code to populate others tables if needed

    @app.cli.command("insert-test-inventory")
    @click.argument("count")
    def insert_test_inventory(count):
        print("creating test inventory")
        for i in range(1, int(count) + 1):
            inventory = Inventory()
            inventory.id_item = i
            inventory.category = "test inventory" + " " + str(i)
            inventory.product = "test product" + " " + str(i)
            inventory.description = "test description" + " " + str(i)
            inventory.picture = "test picture" + " " + str(i)
            inventory.price = i
            db.session.add(inventory)
            db.session.commit()
        print(" all test inventory created")

    @app.cli.command("insert-test-scheduling")
    @click.argument("count")
    def insert_test_scheduling(count):
        print("creating test scheduling")
        for j in range(1, int(count) + 1):
            scheduling = Scheduling()
            scheduling.id_scheduling = j
            scheduling.start_hour = "8:00 hrs" + " " + str(j)
            scheduling.end_hour = "18:00 hrs" + " " + str(j)
            scheduling.day = "Lunes a Viernes" + " " + str(j)
            db.session.add(scheduling)
            db.session.commit()  
        print(" testing scheduling")      


    @app.cli.command("insert-test-order")
    @click.argument("count")
    def insert_test_order(count):
        print("creating test order")
        for k in range(1, int(count) + 1):
            order = Order()
            order.id_order = k
            order.total_price = k+k+k+k
            order.status_commit = "orden cerrada"
            db.session.add(order)
            db.session.commit()
        print("testing order")
