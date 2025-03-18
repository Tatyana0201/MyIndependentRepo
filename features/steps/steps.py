from behave import given

@given('Open "{url}"')
def open_url(context, url):
    print(f"Opening URL: {url}")
    context.driver.get(url)  # This will now work because context.driver is initialized in environment.py
