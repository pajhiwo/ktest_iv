Feature: Market data tests

  Scenario: Check server time
     Given API is accessible
      When we get server time
      Then server time is correct!

  Scenario: Check Asset Pair
     Given API is accessible
      When we retrieve "XXBTZUSD" trading pair
      Then "XXBTZUSD" info is available!
      