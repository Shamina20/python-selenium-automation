Feature:Test for cart functionality

  Scenario: User can click and verify the cart on Target
    Given Open target main page
    When click on cart icon
    Then Verify Your cart is empty message is shown


Scenario: User can add any Target product into the cart and verify
  Given Open target main page
  When Search for mug
  And  Click on Add to cart icon
  And  Confirm Add to Cart button from navigation menu
  And  Open Cart page
  Then verify cart has 1 item(s)