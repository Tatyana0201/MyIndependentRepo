from behave import step



BASE_URL = 'https://dev.linkmygear.com/'


@step('Create new record for device with following data')
def add_new_device(context):
    endpoints = 'device-data/airquard/log/v1'
    data = {}
    for row in context.table.rows:
        data[row.cells[0]] = row.cells[1]
