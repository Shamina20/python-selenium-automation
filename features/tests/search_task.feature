Feature:Verify search results are shown for product

  Scenario: User can search for tea on Target
  Given Open target main page
  When Search for tea
  Then Verify search results are shown for tea

  Scenario Outline: User can search for an product on Target
    Given Open target main page
    When Search for <product>
    Then Verify search results are shown for <expected_product>
    Examples:
    |product |expected_product|
    |tea     |tea             |
    |toys    |toys            |
    |mug     |mug             |

Scenario: User can verify the product name and images
  Given Open target main page
  When Search for Airpods
  Then verify product name and images


