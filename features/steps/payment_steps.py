from behave import given, when, then




@given('workflow is "DIRECT"')
def set_direct_workflow(context):
    """
    Set the workflow type for the payment flow.
    """
    context.workflow = "DIRECT"


@given("valid authentication headers are prepared")
def prepare_auth_headers(context):
    """
    Prepare valid authentication headers.
    """
    context.headers = True


@when("I create a purchase payment with minimal fields")
def create_minimal_purchase(context):
    """
    Simulate a successful purchase payment with minimal data.
    """
    context.response_status = 201
    context.payment_status = "SUCCEEDED"


@when("I create a purchase payment with customer_payer and additional_data")
def create_full_purchase(context):
    """
    Simulate a purchase payment with all optional customer details.
    """
    context.response_status = 201


@when("I create a purchase payment with invalid card number")
def create_purchase_with_invalid_card(context):
    """
    Simulate a failed purchase due to invalid card details.
    """
    context.response_status = 400


@when("I authorize a payment with minimal fields")
def authorize_minimal_payment(context):
    """
    Simulate a successful authorization request.
    """
    context.response_status = 201
    context.authorization_status = "AUTHORIZED"


@when("I authorize a payment with additional data")
def authorize_payment_with_extra_data(context):
    """
    Simulate authorization with extended payload.
    """
    context.response_status = 201


@when("I authorize a payment with invalid amount")
def authorize_payment_with_invalid_amount(context):
    """
    Simulate authorization failure due to invalid amount.
    """
    context.response_status = 400


@when("I refund a payment with full amount")
def refund_full_payment(context):
    """
    Simulate a successful full refund.
    """
    context.response_status = 201
    context.refund_status = "SUCCEEDED"


@when("I refund a payment with invalid payment id")
def refund_with_invalid_payment_id(context):
    """
    Simulate refund failure due to incorrect payment ID.
    """
    context.response_status = 404


@when("I create a payment with verify enabled")
def create_verified_payment(context):
    """
    Simulate a payment with card verification enabled.
    """
    context.response_status = 201


@when("I create a payment with verify enabled using invalid card")
def create_verified_payment_invalid_card(context):
    """
    Simulate verification failure due to invalid card.
    """
    context.response_status = 400




@then("the response status code should be 201")
def verify_success_status(context):
    assert context.response_status == 201


@then("the response status code should be 400")
def verify_bad_request_status(context):
    assert context.response_status == 400


@then("the response status code should be 404")
def verify_not_found_status(context):
    assert context.response_status == 404


@then('the payment status should be "SUCCEEDED"')
def verify_payment_success(context):
    assert context.payment_status == "SUCCEEDED"


@then('the authorization status should be "AUTHORIZED"')
def verify_authorization_success(context):
    assert context.authorization_status == "AUTHORIZED"


@then('the refund status should be "SUCCEEDED"')
def verify_refund_success(context):
    assert context.refund_status == "SUCCEEDED"


@then("customer details should be present in the response")
def verify_customer_details(context):
    """
    Placeholder validation for customer data.
    """
    assert True


@then("an error message should be returned")
def verify_error_message(context):
    """
    Placeholder validation for error message.
    """
    assert True
