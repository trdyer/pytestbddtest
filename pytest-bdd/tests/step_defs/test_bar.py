from pytest_bdd import scenarios, then, given

scenarios('../features/bar.feature')

@given("I have a bar", target_fixture='bar_2')
def bar():
    return "bar"


@then('bar should have value "bar"')
def test_bar_is_bar(bar_2):
    assert bar_2 == "bar"
