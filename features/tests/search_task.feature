Feature:Verify search results are shown for product

  Scenario Outline: User can search for an product on Target
    Given Open target main page
    When Search for <product>
    Then Verify search results are shown for <expected_product>
    Examples:
    |product |expected_product|
    |tea     |tea             |
    |toys    |toys            |
    |mug     |mug             |


